import data
import sender_stand_request

# Длинные переменные
symbol511 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
symbol512 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"

# Получение обновленного kit_body для тестов
def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body

# Позитивное утверждение
def positive_assertion(name):
    kit_body_positive = get_kit_body(name)
    kit_response_positive = sender_stand_request.post_new_client_kit(kit_body_positive)
    assert kit_response_positive.json()["name"] == name
    assert kit_response_positive.status_code == 201

# Отрицательное утверждение с name-field в kit_body
def negative_assertion(name):
    kit_body_negative = get_kit_body(name)
    kit_response_negative = sender_stand_request.post_new_client_kit(kit_body_negative)
    assert kit_response_negative.status_code == 400

# Отрицательное утверждение без name-field в kit_body
def negative_assertion_no_name(kit_body):
    kit_response_negative_no_name = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response_negative_no_name.status_code == 400

# Положительные тесты
# Name-field в kit_body состоит из одного символа
def test_create_kit_1_symbols_in_name_get_success_response():
    positive_assertion("a")

# Name-field в kit_body состоит из 511 symbols
def test_create_kit_511_symbols_in_name_get_success_response():
    positive_assertion(symbol511)

# Name-field в kit_body содержит английские буквы
def test_create_kit_english_letters_in_name_get_success_response():
    positive_assertion("QWErty")

# Name-field в kit_body содержит русские буквы
def test_create_kit_russian_letters_in_name_get_success_response():
    positive_assertion("Мария")

# Name-field в kit_body содержит специальный символ
def test_create_kit_has_special_symbols_in_name_get_success_response():
    positive_assertion("\"№%@\",")

# Name-field в kit_body содержит пробел
def test_create_kit_has_space_in_name_get_success_response():
    positive_assertion("Человек и КО")

# Name-field в kit_body содержит числа
def test_create_kit_has_number_in_name_get_success_response():
    positive_assertion("123")

# Отрицательные тесты
# Name-field в kit_body содержит пустую строку
def test_create_kit_empty_name_get_error_response():
    negative_assertion("")

# Name-field в kit_body состоит из 512 symbols
def test_create_kit_512_symbols_in_name_get_error_response():
    negative_assertion(symbol512)

#   Kit_body не содержит никакого поля с name-field
def test_create_kit_no_name_get_error_response():
    current_kit_body_negative_no_name = data.kit_body.copy()
        # Удаление name-field из запроса
    current_kit_body_negative_no_name.pop("name")
    negative_assertion_no_name(current_kit_body_negative_no_name)

# Name-field в kit_body это число
def test_create_kit_numeric_type_name_get_error_response():
    negative_assertion(123)




