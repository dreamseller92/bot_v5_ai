import random

from ppadb.client import Client as AdbClient
import time
import os
from icecream import ic

import concurrent.futures

from misc import run_and_kill_instances as raki
from misc.common_scripts import where_i_am, get_instance_dict, this_fucking_game_run_or_not
from actions_manager.common_actions import find_and_click_image
from misc.ports_ex.get_bluestack_adb_ports import get_instanses_data
from actions_manager.dig import dig
from actions_manager.comander_skills import harvest, al_tech
import actions_manager.common_actions as ca
import actions_manager.colect_res as cr



from ppadb.client import Client as AdbClient
import os

from ppadb.client import Client as AdbClient

from ppadb.client import Client as AdbClient


class AdbClicks:
    def __init__(self, host='127.0.0.1', port=5037):
        self.client = AdbClient(host=host, port=port)
        self.device = self.client.devices()[0]

    def tap(self, x, y):
        self.device.shell(f'input tap {x} {y}')

    def tap_tasks(self):
        self.tap(100, 1800)

    def tap_bag(self):
        self.tap(300, 1800)

    def tap_mail(self):
        self.tap(500, 1800)

    def tap_alliance(self):
        self.tap(700, 1800)

    def tap_profile(self):
        self.tap(900, 1800)

    def tap_side_arrow(self):
        self.tap(50, 1000)

    def tap_skills_menu(self):
        self.tap(150, 1600)

    # Новые методы для кнопок из скриншота
    def tap_bonus_pack(self):
        self.tap(100, 800)  # Координаты для Бонус Пак

    def tap_newbie_pack(self):
        self.tap(200, 800)  # Координаты для Набор Новичка

    def tap_specials(self):
        self.tap(300, 800)  # Координаты для Специальные Предложения

    def tap_camp_1(self):
        self.tap(400, 800)  # Координаты для Лагерь (Уровень 1)

    def tap_camp_2(self):
        self.tap(500, 800)  # Координаты для Лагерь (Уровень 10)

    def tap_factory_1(self):
        self.tap(600, 800)  # Координаты для Фабрика (Уровень 11)

    def tap_factory_2(self):
        self.tap(700, 800)  # Координаты для Фабрика (Уровень 3)

    def tap_workshop(self):
        self.tap(800, 800)  # Координаты для Мастерская (Уровень 13)

    def tap_troop_promotion(self):
        self.tap(900, 800)  # Координаты для Промоция Войск

    def tap_academy(self):
        self.tap(1000, 800)  # Координаты для Академия

    def tap_hospital(self):
        self.tap(1100, 800)  # Координаты для Госпиталь

    def tap_command_center(self):
        self.tap(1200, 800)  # Координаты для Центр Командования

    def tap_biochemical_lab(self):
        self.tap(1300, 800)  # Координаты для Биохимическая Лаборатория

    def tap_benefits_center(self):
        self.tap(1400, 800)  # Координаты для Центр Льгот

    def tap_alliance_contribution(self):
        self.tap(1500, 800)  # Координаты для Вклад в Альянс

    def tap_gather_processing_1(self):
        self.tap(1600, 800)  # Координаты для Процесс Сбора 1

    def tap_gather_processing_2(self):
        self.tap(1700, 800)  # Координаты для Процесс Сбора 2

    def tap_gather_processing_3(self):
        self.tap(1800, 800)  # Координаты для Процесс Сбора 3


# Пример использования класса
adb_clicks = AdbClicks()
# adb_clicks.tap_tasks()
# adb_clicks.tap_bag()
# adb_clicks.tap_mail()
# adb_clicks.tap_alliance()
# adb_clicks.tap_profile()
# adb_clicks.tap_side_arrow()
# adb_clicks.tap_skills_menu()
# adb_clicks.tap_bonus_pack()
# adb_clicks.tap_newbie_pack()
# adb_clicks.tap_specials()
# adb_clicks.tap_camp_1()
# adb_clicks.tap_camp_2()
# adb_clicks.tap_factory_1()
# adb_clicks.tap_factory_2()
# adb_clicks.tap_workshop()
# adb_clicks.tap_troop_promotion()
# adb_clicks.tap_academy()
# adb_clicks.tap_hospital()
# adb_clicks.tap_command_center()
# adb_clicks.tap_biochemical_lab()
# adb_clicks.tap_benefits_center()
# adb_clicks.tap_alliance_contribution()
# adb_clicks.tap_gather_processing_1()
# adb_clicks.tap_gather_processing_2()
# adb_clicks.tap_gather_processing_3()

# Пример использования класса
# adb_clicks = AdbClicks()
# adb_clicks.tap_tasks()
# adb_clicks.tap_bag()
# adb_clicks.tap_mail()
# adb_clicks.tap_alliance()
# adb_clicks.tap_profile()
# adb_clicks.tap_side_arrow()
# adb_clicks.tap_skills_menu()

# Подключение к устройству
client = AdbClient(host="127.0.0.1", port=5037)
os.system("adb connect 192.168.31.181:5555")
device = client.device('192.168.31.181:5555')

# Захват скриншота


# Сохранение скриншота


# adb_clicks = AdbClicks()
# adb_clicks.tap_side_arrow()

screenshot = device.screencap()
with open('screenshot.png', 'wb') as f:
    f.write(screenshot)
