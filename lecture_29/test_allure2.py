import allure


def add_numbers(a, b):
    """Функція, що додає два числа."""
    return a + b


@allure.epic("Web interface")
@allure.feature("Essential features")
@allure.story("Authentication")
def test_add_numbers():
    @allure.step("Викликаємо функцію add_numbers з аргументами 2 і 3")
    def add_numbers_step():
        return add_numbers(2, 3)

    result = add_numbers_step()
    assert result == 5, f"Очікувано: 5, Фактично: {result}"


test_add_numbers()
