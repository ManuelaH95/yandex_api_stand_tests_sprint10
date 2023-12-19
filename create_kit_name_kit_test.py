import sender_stand_request
import data


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def get_new_user_token():
    current_body = data.headers.copy()
    # current_body["Authorization"] = Authorization
    return current_body


def positive_assert(name):
    kit_body = get_kit_body(name)
    user_response = sender_stand_request.post_new_client_kit(kit_body)

    assert user_response.status_code == 201
    assert user_response.json()["name"] == name


def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400


# Тест 1. Успешное создание набора. Параметр name состоит из 1 символа
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")


# Тест 2. Успешное создание набора. Параметр name состоит из 511 символов
def test_create_kit_511_letters_in_name_get_success_response():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Тест 3. Ошибка. Параметр name состоит из пустой строки
def test_create_kit_empty_name_get_error_response():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)


# Тест 4. Ошибка. Параметр name состоит из 512 символов
def test_create_kit_512_letters_in_name_get_error_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# Тест 5. Успешное создание набора. Параметр name состоит из английских букв
def test_create_kit_english_letters_in_name_get_success_response():
    positive_assert("QWErty")


# Тест 6. Успешное создание набора. Параметр name состоит из русских букв
def test_create_kit_russian_letters_in_name_get_success_response():
    positive_assert("Мария")


# Тест 7. Успешное создание набора. Параметр name состоит из спецсимволов
def test_create_kit_special_symbols_in_name_get_success_response():
    positive_assert("№%@,")


# Тест 8. Успешное создание набора. Параметр name состоит из слов с пробелами
def test_create_kit_has_spaces_in_name_get_success_response():
    positive_assert(" Человек и КО ")


# Тест 9. Успешное создание набора. Параметр name состоит из строки цифр
def test_create_kit_has_numbers_in_name_get_success_response():
    positive_assert("123")


# Тест 10. Ошибка. Параметр name не передан в запросе
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_code_400(kit_body)


# Тест 11. Ошибка. В параметр name передан другой тип параметра (число)
def test_create_kit_number_type_name_get_error_response():
   # kit_body = get_kit_body(123)
   # response = sender_stand_request.post_new_client_kit(kit_body)
   # assert response.status_code == 400
   negative_assert_code_400(123)




