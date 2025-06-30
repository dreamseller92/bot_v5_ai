import random
import threading

import time
import os
import json
import tkinter as tk
from tkinter import messagebox, ttk
from ppadb.client import Client as AdbClient
import concurrent.futures
from icecream import ic

from ppadb.client import Client as AdbClient
import concurrent.futures
from datetime import datetime
from icecream import ic

from misc import run_and_kill_instances as raki
from misc.common_scripts import where_i_am, get_instance_dict, this_fucking_game_run_or_not
from actions_manager.common_actions import find_and_click_image
from misc.ports_ex.get_bluestack_adb_ports import get_instanses_data
from actions_manager.dig import dig
from actions_manager.comander_skills import harvest, al_tech
import actions_manager.common_actions as ca
import actions_manager.colect_res as cr



# Добавим файл для хранения групп
groups_file = 'groups.json'

def save_groups(groups):
    with open(groups_file, 'w') as f:
        json.dump(groups, f)

def load_groups():
    if os.path.exists(groups_file):
        with open(groups_file, 'r') as f:
            return json.load(f)
    return {}

def select_instances(instance_dict, instance_queue_1143, instance_queue_1220):
    def on_submit():
        nonlocal selected_instances
        selected_instances = [instance for var, instance in vars if var.get()]
        root.destroy()

    def save_group():
        group_name = group_entry.get()
        if group_name:
            groups[group_name] = [instance for var, instance in vars if var.get()]
            save_groups(groups)
            messagebox.showinfo("Success", f"Group '{group_name}' saved!")

    def load_group(group_name):
        for var, instance in vars:
            var.set(instance in groups.get(group_name, []))

    selected_instances = []
    groups = load_groups()

    root = tk.Tk()
    root.title("Select Instances")

    vars_1143 = create_scrollable_list(root, instance_queue_1143, instance_dict, last_run)
    vars_1220 = create_scrollable_list(root, instance_queue_1220, instance_dict, last_run)

    vars = vars_1143 + vars_1220

    group_entry = tk.Entry(root)
    group_entry.pack(pady=5)

    tk.Button(root, text="Save Group", command=save_group).pack(pady=5)

    for group_name in groups.keys():
        tk.Button(root, text=f"Load {group_name}", command=lambda name=group_name: load_group(name)).pack(pady=5)

    tk.Button(root, text="Submit", command=on_submit).pack(pady=10)
    root.mainloop()
    return selected_instances

# Part 2: Функции для сохранения и загрузки состояния
state_file = 'state.json'
def save_state(state):
    with open(state_file, 'w') as f:
        json.dump(state, f)

def load_state():
    if os.path.exists(state_file):
        with open(state_file, 'r') as f:
            return json.load(f)
    return {"instances_done": []}

last_run_file = 'last_run.json'

def save_last_run(last_run):
    with open(last_run_file, 'w') as f:
        json.dump(last_run, f)

def load_last_run():
    if os.path.exists(last_run_file):
        with open(last_run_file, 'r') as f:
            return json.load(f)
    return {}


# Part 3: Диалоговые окна с помощью tkinter
def ask_to_continue():
    def on_continue():
        nonlocal choice
        choice = "continue"
        root.destroy()

    def on_startover():
        nonlocal choice
        choice = "startover"
        root.destroy()

    choice = None

    root = tk.Tk()
    root.title("Choose Action")

    label = tk.Label(root, text="Continue from last stop or start over?")
    label.pack(padx=20, pady=10)

    tk.Button(root, text="Continue", command=on_continue).pack(side=tk.LEFT, padx=10, pady=10)
    tk.Button(root, text="Start Over", command=on_startover).pack(side=tk.RIGHT, padx=10, pady=10)

    root.mainloop()
    return choice


def create_scrollable_list(frame, canvas, scrollable_frame, instance_queue, instance_dict, last_run):
    # Настройка холста и области прокрутки
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Обновление области прокрутки
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    vars = []  # Хранение переменных для checkbox

    # Создание списка экземпляров
    for row_counter, instance in enumerate(instance_queue, start=1):
        var = tk.BooleanVar()
        last_run_time = last_run.get(instance_dict[instance]["Name"], "Never")
        chk = tk.Checkbutton(scrollable_frame, text=f'{instance_dict[instance]["Name"]} (Last run: {last_run_time})', variable=var)
        chk.grid(row=row_counter, column=0, sticky="w")
        vars.append((var, instance))

    return vars

# Part 4: Основная логика выполнения действий

get_instanses_data()
client = AdbClient(host="127.0.0.1", port=5037)
max_workers = 2

instance_dict = get_instance_dict()
# print(instance_dict)  # Добавьте это для отладки
instances = list(instance_dict.keys())

instance_queue_1143_steel = [inst for inst in instances if "1143" in instance_dict[inst]["Name"]]
instance_queue_1220_oil = [inst for inst in instances if "1220" in instance_dict[inst]["Name"]]
# print(instance_queue_1143_steel, instance_queue_1220_oil)  # Добавьте это для отладки



from datetime import datetime

def perform_actions(instance):
    name, port = instance_dict[instance]["Name"], instance_dict[instance]["port"]
    last_run[name] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    save_last_run(last_run)

    time.sleep(random.randint(1, 3))
    raki.run_instance(instance)

    while True:
        time.sleep(10)
        try:
            os.system("adb connect 127.0.0.1:" + port)
            device = client.device(f'127.0.0.1:{port}')
            screenshot = device.screencap()
            if this_fucking_game_run_or_not(screenshot):
                template_path = 'main_ico.png'
                find_and_click_image(device, template_path)

            if where_i_am(screenshot):
                break
        except Exception as e:
            print(e)

    random.randint(1, 15)
    harvest(device)
    time.sleep(5)
    cr.collect_res(device)
    time.sleep(5)
    al_tech(device)
    time.sleep(5)
    dig(device)

    raki.kill_instance(name)
    state["instances_done"].append(instance)
    save_state(state)



def main():
    global state, last_run
    state = load_state()
    last_run = load_last_run()

    if ask_to_continue() == "startover":
        state = {"instances_done": []}
        selected_instances = select_instances(instance_dict, instance_queue_1143_steel, instance_queue_1220_oil)
        state["selected_instances"] = selected_instances
        save_state(state)
        instance_queue = selected_instances
    else:
        instance_queue = state.get("selected_instances", [])
        instance_queue = [i for i in instance_queue if i not in state["instances_done"]]

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(perform_actions, instance) for instance in instance_queue[:max_workers]}
        instance_queue = instance_queue[max_workers:]

        while futures:
            done, _ = concurrent.futures.wait(futures, return_when=concurrent.futures.FIRST_COMPLETED)

            for future in done:
                try:
                    future.result()
                except Exception as exc:
                    print(f'Task raised an exception: {exc}')
                    return

                futures.remove(future)

                if instance_queue:
                    instance = instance_queue.pop(0)
                    futures.add(executor.submit(perform_actions, instance))

    print("All instances completed")

if __name__ == "__main__":
    main()
