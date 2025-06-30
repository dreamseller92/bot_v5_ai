
import time
from PIL import Image
from io import BytesIO
import numpy as np
import cv2


def reset_position_in_city(device):

    x, y = 60, 899
    time.sleep(3)
    device.shell(f"input tap {x} {y}")
    time.sleep(3)
    device.shell(f"input tap {x} {y}")




def click_resource(device, x, y):
    device.shell(f"input tap {x} {y}")
    time.sleep(0.5)


def find_and_click_image(device, template_path):
    # Получаем скриншот как байты
    result = device.screencap()

    # Преобразуем скриншот в изображение
    image = Image.open(BytesIO(result))

    # Преобразуем изображение в формат, используемый OpenCV
    image_np = np.array(image)

    # Преобразование в формат BGR, который используется OpenCV
    image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    # Загрузка изображения шаблона и преобразование в оттенки серого
    template = cv2.imread(template_path)
    gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Преобразование скриншота в оттенки серого
    gray_image = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)

    # Поиск шаблона на скриншоте
    res = cv2.matchTemplate(gray_image, gray_template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # Задание порога для определения совпадения
    threshold = 0.5
    if max_val >= threshold:
        # Координаты центра найденного шаблона
        x_center = max_loc[0] + gray_template.shape[1] // 2
        y_center = max_loc[1] + gray_template.shape[0] // 2
        click_resource(device, x_center, y_center)
        print(f"Изображение найдено и кликнуто в координатах ({x_center}, {y_center})")
    else:
        print("Изображение не найдено")
