import cv2
import numpy as np


def where_i_am(screenshot_bytes):
    # Путь к файлам изображений
    template_path = "in_city.png"

    # Конвертация байтового массива в изображение OpenCV
    nparr = np.frombuffer(screenshot_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Загрузка изображения шаблона
    template = cv2.imread(template_path, 0)

    # Проверка успешности загрузки изображений
    if image is None:
        print(f"Ошибка загрузки изображения из байтового массива")
        return 0
    if template is None:
        print(f"Ошибка загрузки изображения шаблона: {template_path}")
        return 0

    # Преобразование изображения в оттенки серого
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Поиск шаблона на изображении
    result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Задание порога для определения совпадения
    threshold = 0.8

    # Проверка, найден ли шаблон
    if max_val >= threshold:
        return 1
    else:
        return 0

def full_or_not(screenshot_bytes):
    # Путь к файлам изображений
    template_path = "full_q_vip.png"

    # Конвертация байтового массива в изображение OpenCV
    nparr = np.frombuffer(screenshot_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Загрузка изображения шаблона
    template = cv2.imread(template_path, 0)

    # Проверка успешности загрузки изображений
    if image is None:
        print(f"Ошибка загрузки изображения из байтового массива")
        return 0
    if template is None:
        print(f"Ошибка загрузки изображения шаблона: {template_path}")
        return 0

    # Преобразование изображения в оттенки серого
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Поиск шаблона на изображении
    result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Задание порога для определения совпадения
    threshold = 0.8

    # Проверка, найден ли шаблон
    if max_val >= threshold:
        return 1
    else:
        return 0

def full_or_not_2(screenshot_bytes):
    # Путь к файлам изображений
    template_path = "full_q.png"

    # Конвертация байтового массива в изображение OpenCV
    nparr = np.frombuffer(screenshot_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Загрузка изображения шаблона
    template = cv2.imread(template_path, 0)

    # Проверка успешности загрузки изображений
    if image is None:
        print(f"Ошибка загрузки изображения из байтового массива")
        return 0
    if template is None:
        print(f"Ошибка загрузки изображения шаблона: {template_path}")
        return 0

    # Преобразование изображения в оттенки серого
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Поиск шаблона на изображении
    result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Задание порога для определения совпадения
    threshold = 0.8

    # Проверка, найден ли шаблон
    if max_val >= threshold:
        return 1
    else:
        return 0

def get_instance_dict(nation=None):
    import json
    import os

    base_path = "misc/ports_ex"
    if nation:
        file_path = os.path.join(base_path, f'{nation}_instance_data.json')
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        instance_dict = {}
        for file_name in ["1143_instance_data.json", "1220_instance_data.json"]:
            file_path = os.path.join(base_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                instance_dict.update(json.load(file))
        return instance_dict




def this_fucking_game_run_or_not(screenshot_bytes):
    # Путь к файлам изображений
    template_path = "main_ico.png"

    # Конвертация байтового массива в изображение OpenCV
    nparr = np.frombuffer(screenshot_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Загрузка изображения шаблона
    template = cv2.imread(template_path, 0)

    # Проверка успешности загрузки изображений
    if image is None:
        print(f"Ошибка загрузки изображения из байтового массива")
        return 0
    if template is None:
        print(f"Ошибка загрузки изображения шаблона: {template_path}")
        return 0

    # Преобразование изображения в оттенки серого
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Поиск шаблона на изображении
    result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Задание порога для определения совпадения
    threshold = 0.8

    # Проверка, найден ли шаблон
    if max_val >= threshold:
        return 1
    else:
        return 0

