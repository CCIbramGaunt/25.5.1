import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_there_is_a_name_age_and_gender(go_to_my_pets):
    # Поверяем что на странице со списком моих питомцев, у всех питомцев есть имя, возраст и порода

    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "all_my_pets")))

    # количество ячеек в таблице (без изображений)
    tdno = pytest.driver.find_elements(By.XPATH, "//table[@class='table table-hover']/tbody/tr/td")

    # Делаем список, каждый элемент которого - это содержимое ячейки таблицы (кроме изображений)
    td_into_list = []
    for j in range(0, len(tdno)):
        td_into_list.append(tdno[j].text)

    # Тест успешно пройден, если количество ячеек в таблице строго равно количеству значений, переданных в список
    assert len(td_into_list) == len(tdno)
