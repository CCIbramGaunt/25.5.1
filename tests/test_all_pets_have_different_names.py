import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_all_pets_have_different_names(go_to_my_pets):
    # Поверяем что на странице со списком моих питомцев, у всех питомцев разные имена

    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "all_my_pets")))
    # Сохраняем в переменную pet_data элементы с данными о питомцах
    pet_data = pytest.driver.find_elements(By.XPATH, "//table[@class='table table-hover']/tbody/tr")

    # Перебираем данные из pet_data, оставляем имя, возраст, и породу остальное меняем на пустую строку
    # и разделяем по пробелу. Имена добавляем в список.
    pets_names = []
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        pets_names.append(split_data_pet[0])

    # Перебираем имена и если имя повторяется то прибавляем к счетчику 1.
    r = 0
    for i in range(len(pets_names)):
        if pets_names.count(pets_names[i]) > 1:
            r += 1
    assert r == 0
