from actions_manager.common_actions import find_and_click_image, reset_position_in_city
import time
def starting(device):
     find_and_click_image(device, 'base_data\\img\\starting_but\\claim.png')
     find_and_click_image(device, 'base_data\\img\\starting_but\\claim.png')
     device.shell("input keyevent 4")
     device.shell("input keyevent 4")
     time.sleep(3)
     device.shell("input keyevent 4")
     device.shell("input keyevent 4")
     time.sleep(3)
     device.shell("input keyevent 4")
     device.shell("input click 140 166")
     time.sleep(3)
     device.shell("input keyevent 4")