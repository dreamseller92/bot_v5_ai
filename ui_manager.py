import json
import os
import tkinter as tk
from tkinter import ttk

preset_file = "presets.json"

# --- Темы оформления ---
styles = {
    "dark": {
        "bg": "#2E2E2E",
        "fg": "white",
        "btn_bg": "#5A5A5A",
        "btn_fg": "white",
        "entry_bg": "#3A3A3A",
        "entry_fg": "white"
    },
    "gray": {
        "bg": "#D3D3D3",
        "fg": "black",
        "btn_bg": "#A9A9A9",
        "btn_fg": "black",
        "entry_bg": "#C0C0C0",
        "entry_fg": "black"
    }
}

# Выбранный стиль
current_style = styles["dark"]  # можно заменить на styles["gray"]

def save_preset(name, instances):
    presets = load_presets()
    presets[name] = instances
    with open(preset_file, 'w') as f:
        json.dump(presets, f)

def load_presets():
    if not os.path.exists(preset_file):
        return {}
    with open(preset_file, 'r') as f:
        return json.load(f)

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
    root.title("Выберите действие")
    root.configure(bg=current_style["bg"])

    tk.Label(root, text="Продолжить с последнего места или начать заново?",
             font=("Arial", 13), bg=current_style["bg"], fg=current_style["fg"]).pack(padx=20, pady=10)

    button_frame = tk.Frame(root, bg=current_style["bg"])
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Продолжить", command=on_continue,
              bg=current_style["btn_bg"], fg=current_style["btn_fg"],
              font=("Arial", 11), width=15).grid(row=0, column=0, padx=10)

    tk.Button(button_frame, text="Начать заново", command=on_startover,
              bg=current_style["btn_bg"], fg=current_style["btn_fg"],
              font=("Arial", 11), width=15).grid(row=0, column=1, padx=10)

    root.mainloop()
    return choice

def create_scrollable_list(frame, canvas, scrollable_frame, instance_queue, instance_dict, last_run):
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    vars = []
    for row_counter, instance in enumerate(instance_queue, start=1):
        var = tk.BooleanVar()
        last_run_time = last_run.get(instance_dict[instance]["Name"], "Never")
        chk = tk.Checkbutton(
            scrollable_frame,
            text=f'{instance_dict[instance]["Name"]} (Последний запуск: {last_run_time})',
            variable=var,
            bg=current_style["bg"],
            fg=current_style["fg"],
            selectcolor=current_style["bg"],
            font=("Arial", 10),
            anchor="w",
            padx=10
        )
        chk.grid(row=row_counter, column=0, sticky="w")
        vars.append((var, instance))
    return vars

def select_instances(instance_dict, instance_queue_1143, instance_queue_1220):
    def on_submit():
        nonlocal selected_instances
        selected_instances = [instance for var, instance in vars if var.get()]
        if preset_name_entry.get().strip():
            save_preset(preset_name_entry.get().strip(), selected_instances)
        root.destroy()

    def select_preset(name):
        nonlocal selected_instances
        selected_instances = load_presets().get(name, [])
        root.destroy()

    selected_instances = []
    root = tk.Tk()
    root.title("Выбор экземпляров")
    root.configure(bg=current_style["bg"])

    # Scroll Frames
    frame_1143 = ttk.Frame(root)
    canvas_1143 = tk.Canvas(frame_1143, bg=current_style["bg"], highlightthickness=0)
    scrollable_frame_1143 = ttk.Frame(canvas_1143)

    frame_1220 = ttk.Frame(root)
    canvas_1220 = tk.Canvas(frame_1220, bg=current_style["bg"], highlightthickness=0)
    scrollable_frame_1220 = ttk.Frame(canvas_1220)

    frame_1143.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    canvas_1143.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    frame_1220.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    canvas_1220.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    vars_1143 = create_scrollable_list(frame_1143, canvas_1143, scrollable_frame_1143,
                                       instance_queue_1143, instance_dict, {})
    vars_1220 = create_scrollable_list(frame_1220, canvas_1220, scrollable_frame_1220,
                                       instance_queue_1220, instance_dict, {})
    vars = vars_1143 + vars_1220

    # Preset
    tk.Label(root, text="Название пресета для сохранения:", font=("Arial", 12),
             bg=current_style["bg"], fg=current_style["fg"]).pack(pady=(10, 0))
    preset_name_entry = tk.Entry(root, bg=current_style["entry_bg"], fg=current_style["entry_fg"],
                                 font=("Arial", 12), width=30)
    preset_name_entry.pack(pady=5)

    tk.Button(root, text="Сохранить и продолжить", command=on_submit,
              bg=current_style["btn_bg"], fg=current_style["btn_fg"],
              font=("Arial", 11), width=25).pack(pady=10)

    # Preset quick launch
    presets = load_presets()
    if presets:
        tk.Label(root, text="Или выберите готовый пресет:", font=("Arial", 12),
                 bg=current_style["bg"], fg=current_style["fg"]).pack(pady=(10, 0))
        for name in presets:
            tk.Button(root, text=name, command=lambda n=name: select_preset(n),
                      bg=current_style["btn_bg"], fg=current_style["btn_fg"],
                      font=("Arial", 11), width=25).pack(pady=3)

    root.mainloop()
    return selected_instances