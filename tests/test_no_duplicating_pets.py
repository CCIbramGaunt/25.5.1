import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_no_duplicate_pets(go_to_my_pets):
    # Поверяем что на странице со списком моих питомцев нет повторяющихся питомцев

    # Устанавливаем явное ожидание
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "all_my_pets")))

    # Сохраняем в переменную pet_data элементы с данными о питомцах
    pet_data = pytest.driver.find_elements(By.XPATH, "//table[@class='table table-hover']/tbody/tr")

    # Перебираем данные из pet_data, оставляем имя, возраст и породу, остальное меняем на пустую строку
    # и разделяем по пробелу.
    list_data = []
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        list_data.append(split_data_pet)

    # Склеиваем имя, возраст и породу, получившиеся склееные слова добавляем в строку
    # и между ними вставляем пробел
    line = ''
    for i in list_data:
        line += ''.join(i)
        line += ' '

    # Получаем список из строки line
    list_line = line.split(' ')

    # Находим количество элементов списка и множества
    a = len(list_line)
    b = len(set(list_line))

    # Из количества элементов списка вычитаем количество элементов множества
    result = a - b

    # Если количество элементов == 0 значит карточки с одинаковыми данными отсутствуют
    assert result == 0
