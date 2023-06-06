import pytest


def test_show_my_pets(go_to_my_pets):

    # Проверяем что мы оказались на странице "Мои питомцы"
    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'
