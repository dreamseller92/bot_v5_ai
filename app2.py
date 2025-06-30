import json
import os
import random
import time
from datetime import datetime
import concurrent.futures
from ppadb.client import Client as AdbClient

from misc import run_and_kill_instances as raki
from misc.common_scripts import where_i_am, get_instance_dict, this_fucking_game_run_or_not
from actions_manager.common_actions import find_and_click_image
from misc.ports_ex.get_bluestack_adb_ports import get_instanses_data
from actions_manager.dig import dig
from actions_manager.comander_skills import harvest, al_tech
import actions_manager.common_actions as ca
import actions_manager.colect_res as cr
from actions_manager.start import starting

from ui_manager import ask_to_continue, select_instances

# Файл сохранения состояния
state_file = 'state.json'
selected_instances_file = 'selected_instances.json'

def save_data(filename, data):
    """Сохранение данных в JSON файл."""
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_data(filename, default_value):
    """Загрузка данных из JSON файла."""
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return default_value

# Загрузка состояний
state = load_data(state_file, {"instances_done": []})
last_run = load_data('last_run.json', {})
selected_instances = load_data(selected_instances_file, [])

# Получаем данные об инстансах
get_instanses_data()
client = AdbClient(host="127.0.0.1", port=5037)
max_workers = 2
instance_dict = get_instance_dict()
instances = list(instance_dict.keys())

instance_queue_1143_steel = [inst for inst in instances if "1143" in instance_dict[inst]["Name"]]
instance_queue_1220_oil = [inst for inst in instances if "1220" in instance_dict[inst]["Name"]]


def perform_actions(instance):
    """Выполнение действий для конкретного экземпляра и отображение информации в чате."""
    name, port = instance_dict[instance]["Name"], instance_dict[instance]["port"]

    print(f"🔄 Запускаем инстанс: {name} (порт {port})")  # Отображение в консоли
    last_run[name] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    save_data('last_run.json', last_run)

    time.sleep(random.randint(1, 3))
    raki.run_instance(instance)

    while True:
        time.sleep(10)
        try:
            os.system(f"adb connect 127.0.0.1:{port}")
            device = client.device(f'127.0.0.1:{port}')
            screenshot = device.screencap()

            if this_fucking_game_run_or_not(screenshot):
                print(f"✅ {name}: Игра запущена, ищем иконку...")
                find_and_click_image(device, 'main_ico.png')

            if where_i_am(screenshot):
                print(f"🎮 {name}: В игре, начинаем выполнение действий")
                break
        except Exception as e:
            print(f"⚠️ Ошибка с {name}: {e}")

    print(f"⏳ {name}: Выполняем сбор ресурсов и задания...")

    starting(device)
    harvest(device)
    time.sleep(5)
    cr.collect_res(device)
    al_tech(device)
    dig(device)

    print(f"✅ {name}: Завершено, закрываем инстанс")
    raki.kill_instance(name)

    state["instances_done"].append(instance)
    save_data(state_file, state)
def main():
    global selected_instances

    choice = ask_to_continue()

    if choice == "startover":
        state["instances_done"] = []
        selected_instances = select_instances(instance_dict, instance_queue_1143_steel, instance_queue_1220_oil)
        save_data(selected_instances_file, selected_instances)  # Сохранение выбранных инстансов
    else:
        selected_instances = load_data(selected_instances_file, [])  # Загрузка ранее выбранных инстансов

    # Запускаем только те, которые еще не выполнены
    instance_queue = [i for i in selected_instances if i not in state["instances_done"]]

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(perform_actions, instance_queue)

if __name__ == "__main__":
    main()