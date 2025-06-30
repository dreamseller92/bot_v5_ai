import time
from misc.common_scripts import where_i_am
from actions_manager.common_actions import find_and_click_image, reset_position_in_city

def find_and_click_all_images(device, images):
    for image in images:
        find_and_click_image(device, image)

def collect_res(device):
    screenshot = device.screencap()
    if where_i_am(screenshot):
        device.shell("input swipe 392 723 90 708")
        time.sleep(2)
        device.shell("input swipe 90 708 90 408")
        time.sleep(2)
        corn_images = ['base_data\\img\\res_in_city\\corn.png', 'base_data\\img\\res_in_city\\corn2.png', 'base_data\\img\\res_in_city\\corn3.png']
        oil_images = ['base_data\\img\\res_in_city\\oil.png', 'base_data\\img\\res_in_city\\oil2.png', 'base_data\\img\\res_in_city\\oil3.png']
        steel_images = ['base_data\\img\\res_in_city\\steel.png', 'base_data\\img\\res_in_city\\steel2.png', 'base_data\\img\\res_in_city\\steel3.png']
        mineral_images = ['base_data\\img\\res_in_city\\mineral.png', 'base_data\\img\\res_in_city\\mineral2.png', 'base_data\\img\\res_in_city\\mineral3.png']

        find_and_click_all_images(device, corn_images)
        find_and_click_all_images(device, oil_images)
        find_and_click_all_images(device, steel_images)
        find_and_click_all_images(device, mineral_images)

        reset_position_in_city(device)
        time.sleep(3)
        device.shell("input keyevent 4")
        device.shell("input keyevent 4")
        # time.sleep(1)
        # reset_position_in_city(device)
