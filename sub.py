import ctypes
import subprocess

application_path = "Z:\\Program Files\\AOO2\\GAME\\Age.of.Origins_0.exe"

# Проверка, запущен ли скрипт от имени администратора
def is_admin():
    return ctypes.windll.shell32.IsUserAnAdmin() != 0

if is_admin():
    # Запуск приложения
    subprocess.Popen(application_path, shell=True)
else:
    # Перезапуск скрипта с правами администратора
    ctypes.windll.shell32.ShellExecuteW(None, "runas", "python", __file__, None, 1)
