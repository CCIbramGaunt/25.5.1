import pytest
from settings import valid_email, valid_password
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_show_pet_friends():
    # Вводим email
    WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.ID, 'email')))
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)

    # Вводим пароль
    WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.ID, 'pass')))
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)

    # Нажимаем на кнопку входа в аккаунт
    WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/all_pets'

    # Устанавливаем неявные ожидания
    pytest.driver.implicitly_wait(5)
    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    pytest.driver.implicitly_wait(5)
    names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    pytest.driver.implicitly_wait(5)
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    assert names[0].text != ''

    for i in range(len(names)):
        assert images[i].get_attribute('src') is not None
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ',' in descriptions[i].text
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0
