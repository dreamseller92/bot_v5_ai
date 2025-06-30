import cv2
import numpy as np

# Загрузка исходного изображения и изображения шаблона
image = cv2.imread('../screenshots/new/screenshot_0.png')
template = cv2.imread('../actions_manager/in_city.png', 0)

# Преобразование изображения в оттенки серого
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Поиск шаблона на изображении
result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)
print(result)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Координаты верхнего левого угла области совпадения
top_left = max_loc
h, w = template.shape

# Координаты нижнего правого угла области совпадения
bottom_right = (top_left[0] + w, top_left[1] + h)

# Отображение области совпадения на изображении
cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

# Показать результат
cv2.imshow('Detected Template', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
