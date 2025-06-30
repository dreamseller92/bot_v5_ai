import subprocess
import csv
import os

def get_pid_by_label(app_name, label):
    result = subprocess.run(['tasklist', '/v', '/fo', 'csv'], capture_output=True, text=True, encoding='utf-8', errors='ignore')
    output = result.stdout  
    reader = csv.reader(output.splitlines())
    for row in reader:
        if row[0].strip('"') == app_name and row[-1].strip('"') == label:
            return int(row[1].strip('"'))
    return None

def kill_instance(name):
    pid = get_pid_by_label('HD-Player.exe', name)
    if pid:
        subprocess.run(['taskkill', '/PID', str(pid), '/F'])

def run_instance(instance):
    command = f'start /realtime "" "C:\\Program Files\\BlueStacks_nxt\\HD-Player.exe" --instance {instance} --cmd launchAppWithBsx --package "com.camelgames.aoz" --source desktop_shortcut'
    os.system(command)