import time
from misc.common_scripts import where_i_am
from actions_manager.common_actions import find_and_click_image, reset_position_in_city

def harvest(device):
    screenshot = device.screencap()
    if not where_i_am(screenshot):
        device.shell(f"input tap 69 910")

    time.sleep(2)
    device.shell(f"input tap 500 759")
    time.sleep(2)
    device.shell(f"input tap 76 759")
    time.sleep(2)
    device.shell(f"input tap 447 463")
    device.shell(f"input tap 150 136")
    time.sleep(2)
    device.shell(f"input tap 150 136")
    device.shell(f"input tap 150 136")
    device.shell(f"input tap 150 136")

def al_tech(device):
    screenshot = device.screencap()
    if not where_i_am(screenshot):
        device.shell(f"input tap 69 910")

    device.shell("input tap 18 382")
    time.sleep(0.5)

    device.shell("input tap 297 580")
    time.sleep(0.5)

    device.shell("input tap 102 235")
    time.sleep(0.5)

    device.shell("input tap 69 613")
    time.sleep(0.5)

    device.shell("input tap 69 613")
    time.sleep(0.5)

    device.shell("input tap 69 613")
    time.sleep(0.5)

    device.shell("input tap 69 613")
    time.sleep(0.5)

    device.shell("input tap 58 538")
    time.sleep(0.5)

    device.shell("input keyevent 4")
    device.shell("input keyevent 4")
    device.shell("input keyevent 4")
    device.shell(f"input tap 150 136")
    device.shell(f"input tap 150 136")
    device.shell(f"input tap 150 136")

    reset_position_in_city(device)
