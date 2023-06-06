import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_photo_availability(go_to_my_pets):
    # Поверяем что на странице со списком моих питомцев хотя бы у половины питомцев есть фото

    WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class=".col-sm-4 left"]')))

    WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.ID, "all_my_pets")))

    # Сохраняем в переменную ststistic элементы статистики
    statistic = pytest.driver.find_elements(By.CSS_SELECTOR, 'div[class=".col-sm-4 left"]')

    # Сохраняем в переменную images элементы с атрибутом img
    images = pytest.driver.find_elements(By.XPATH, "//table[@class='table table-hover']/tbody/tr/th")

    # Получаем количество питомцев из данных статистики
    pet_qty = statistic[0].text.split('\n')
    pet_qty = pet_qty[1].split(' ')
    pet_qty = int(pet_qty[1])

    # Находим количество питомцев с фотографией
    with_photos = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') is not None:
            with_photos += 1

    # Проверяем что количество питомцев с фотографией больше или равно половине количества питомцев
    assert with_photos >= pet_qty // 2
    print(f'количество фото: {with_photos}')
    print(f'Половина от числа питомцев: {pet_qty // 2}')
