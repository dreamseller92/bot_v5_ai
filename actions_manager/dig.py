import time
from misc.common_scripts import where_i_am, full_or_not, full_or_not_2
from actions_manager.common_actions import find_and_click_image, reset_position_in_city

def dig(device):
    screenshot = device.screencap()
    if where_i_am(screenshot):
        time.sleep(2)
        device.shell(f"input tap 60 899")
    # radar 3 var
    time.sleep(1)
    find_and_click_image(device, 'base_data\\img\\dig\\radar.png')
    time.sleep(1)
    find_and_click_image(device, 'base_data\\img\\dig\\radar2.png')
    time.sleep(1)
    find_and_click_image(device, 'base_data\\img\\dig\\radar3.png')
    time.sleep(1)

    find_and_click_image(device, 'base_data\\img\\dig\\plus.png')
    time.sleep(0.1)
    find_and_click_image(device, 'base_data\\img\\dig\\plus.png')
    time.sleep(0.1)
    find_and_click_image(device, 'base_data\\img\\dig\\plus.png')
    time.sleep(0.1)
    find_and_click_image(device, 'base_data\\img\\dig\\plus.png')
    time.sleep(0.1)
    find_and_click_image(device, 'base_data\\img\\dig\\plus.png')
    time.sleep(0.5)
    find_and_click_image(device, 'base_data\\img\\dig\\minus.png')
    time.sleep(0.5)
    find_and_click_image(device, 'base_data\\img\\dig\\go1.png')
    time.sleep(0.5)

    k = 5

    while k > 0:
        screenshot = device.screencap()
        # Выход на карту мира если в городе
        if where_i_am(screenshot):
            time.sleep(2)
            device.shell(f"input tap 60 899")
        # кнопка радара
        time.sleep(1)
        find_and_click_image(device, 'base_data\\img\\dig\\radar.png')
        time.sleep(1)
        find_and_click_image(device, 'base_data\\img\\dig\\radar2.png')
        time.sleep(1)
        find_and_click_image(device, 'base_data\\img\\dig\\radar3.png')
        # кнопка поиска
        time.sleep(1)
        find_and_click_image(device, 'base_data\\img\\dig\\go1.png')
        # кнопка копать
        time.sleep(1)
        find_and_click_image(device, 'base_data\\img\\dig\\dig.png')
        find_and_click_image(device, 'base_data\\img\\dig\\dig.png')

        # проверка заполненности походных отрядов
        screenshot = device.screencap()
        if full_or_not(screenshot):
            time.sleep(2)
            device.shell(f"input tap 60 899")
            k = False
        if full_or_not_2(screenshot):
            time.sleep(2)
            device.shell(f"input tap 60 899")
            k = False

        # отправка отряда на рудник
        time.sleep(0.5)
        find_and_click_image(device, 'base_data\\img\\dig\\set_out.png')
        k -= 1
        print(k)
        if k == 1:
            find_and_click_image(device, 'base_data\\img\\dig\\minus.png')
            k = 5



    time.sleep(2)
    device.shell(f"input tap 60 899")


import time
from misc.common_scripts import where_i_am, full_or_not, full_or_not_2
from actions_manager.common_actions import find_and_click_image, reset_position_in_city

import time
from misc.common_scripts import where_i_am, full_or_not, full_or_not_2
from actions_manager.common_actions import find_and_click_image, reset_position_in_city


def dig2(device):
    # Поднимаем уровень рудника в начале скрипта
    device.shell(f"input tap 2 2")
    k = True

    while k:
        screenshot = device.screencap()

        # Выход на карту мира если в городе
        if where_i_am(screenshot):
            time.sleep(2)
            device.shell(f"input tap 60 899")

        # кнопка радара
        time.sleep(1)
        find_and_click_image(device, 'base_data\\img\\dig\\radar.png')

        attempts = 0
        while attempts < 10:
            # кнопка поиска
            time.sleep(1)
            find_and_click_image(device, 'base_data\\img\\dig\\go1.png')

            # Проверка наличия кнопки "копать"
            time.sleep(2)
            if find_and_click_image(device, 'base_data\\img\\dig\\dig.png'):
                # Если кнопка "копать" появилась, второй клик на неё
                find_and_click_image(device, 'base_data\\img\\dig\\dig.png')
                break
            else:
                attempts += 1

        # Если после 10 попыток кнопка "копать" не появилась, снижаем уровень рудника
        if attempts == 10:
            device.shell(f"input tap 1 1")

        # Проверка заполненности походных отрядов
        screenshot = device.screencap()
        if full_or_not(screenshot):
            time.sleep(2)
            device.shell(f"input tap 60 899")
            k = False
        if full_or_not_2(screenshot):
            time.sleep(2)
            device.shell(f"input tap 60 899")
            k = False

        # Отправка отряда на рудник
        time.sleep(0.5)
        find_and_click_image(device, 'base_data\\img\\dig\\set_out.png')

    # Выход на карту мира после завершения цикла
    time.sleep(2)
    device.shell(f"input tap 60 899")

