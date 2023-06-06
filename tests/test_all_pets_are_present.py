import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_all_pets_are_present(go_to_my_pets):
    # Проверяем что на странице со списком моих питомцев присутствуют все питомцы

    WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class=".col-sm-4 left"]')))

    # Сохраняем в переменную statistic элементы статистики
    statistic = pytest.driver.find_elements(By.CSS_SELECTOR, 'div[class=".col-sm-4 left"]')

    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "all_my_pets")))

    # Сохраняем в переменную pets элементы карточек питомцев
    pets = pytest.driver.find_elements(By.XPATH, "//table[@class='table table-hover']/tbody/tr")

    # Получаем количество питомцев из данных статистики
    pet_qty = statistic[0].text.split('\n')
    pet_qty = pet_qty[1].split(' ')
    pet_qty = int(pet_qty[1])

    # Получаем количество карточек питомцев
    number_of_pets = len(pets)

    # Проверяем что количество питомцев из статистики совпадает с количеством карточек питомцев
    assert pet_qty == number_of_pets
