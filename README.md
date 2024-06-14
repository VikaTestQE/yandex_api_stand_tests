## Автоматизация чек-листа для поля `name` в запросе на создание набора в Яндекс Прилавке с помощью API Яндекс Прилавка.

### Требования

- Выполнить запрос на создание нового пользователя и запомнить токен авторизации `authToken`.
- Выполнить запрос на создание личного набора для этого пользователя. Обязательно передать заголовок `Authorization`.


### Чек-лист проверок

| №  | Описание                                                                     | ОР                                                                            |
|----|------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| 1  | Допустимое количество символов (1): `kit_body = { "name": "a" }`             | <br/>Код ответа — 201<br/>В ответе поле name совпадает с полем name в запросе |
| 2  | Допустимое количество символов (511): тестовое значение под таблицей         | <br/>Код ответа — 201<br/>В ответе поле name совпадает с полем name в запросе |
| 3  | Количество символов меньше допустимого (0): `kit_body = { "name": "" }`      | <br/>Код ответа — 400                                                         |
| 4  | Количество символов больше допустимого (512): тестовое значение под таблицей | <br/>Код ответа — 400                                                         |
| 5  | Разрешены английские буквы: `kit_body = { "name": "QWErty" }`                | <br/>Код ответа — 201<br/>В ответе поле name совпадает с полем name в запросе |
| 6  | Разрешены русские буквы: `kit_body = { "name": "Мария" }`                    | <br/>Код ответа — 201<br/>В ответе поле name совпадает с полем name в запросе |
| 7  | Разрешены спецсимволы: `kit_body = { "name": ""№%@"," }`                     | <br/>Код ответа — 201<br/>В ответе поле name совпадает с полем name в запросе |
| 8  | Разрешены пробелы: `kit_body = { "name": " Человек и КО " }`                 | <br/>Код ответа — 201<br/>В ответе поле name совпадает с полем name в запросе |
| 9  | Разрешены цифры: `kit_body = { "name": "123" }`                              | <br/>Код ответа — 201<br/>В ответе поле name совпадает с полем name в запросе |
| 10 | Параметр не передан в запросе: `kit_body = {}`                               | <br/>Код ответа — 400                                                         |
| 11 | Передан другой тип параметра (число): `kit_body = { "name": 123 }`           | <br/>Код ответа — 400                                                         |

#### Тестовые значения для проверок №2 и №4
Допустимое количество символов (511)
```py
kit_body = { "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC" }
```
Количество символов больше допустимого (512)
```py
kit_body = { "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD" }
```

### Что важно учесть

Некоторые тесты вернутся с результатом FAILED. Не переживай: это соответствует чек-листу.
При отправке решения не забудь добавить файлы .gitignore и README.md. В файле README.md кратко опиши содержимое проекта и правила запуска тестов. 
Всего понадобится шесть файлов: `configuration.py`, `data.py`, `sender_stand_request.p`y, `create_kit_name_kit_test.py`, `README.md`, `.gitignore.`
### Подсказки
> #### URL и пути запросов: файл configuration.py
> Все пути удобно хранить в отдельном файле. Его можно назвать `configuration.py`.

> #### Отправка запросов: файл sender_stand_request.py
> - Все запросы, которые пригодятся для решения задачи, можно собрать в одном файле и назвать его, например, так:`sender_stand_request.py`.
> - Запрос на создание нового пользователя можно взять из урока про POST-запрос.
> - Функцию создания нового набора можно назвать так:`post_new_client_kit` .
> - В функции создания нового набора используй два параметра: `kit_body` — тело запроса, `auth_token` — токен авторизации.
> - Если переиспользуешь словарь для данных из файла `data.py`, воспользуйся функцией `copy()`. Исходный словарь менять не стоит: это может привести к ошибкам.
> - Если запрос отправляется с ошибкой, обрати внимание на слэши `(//)`, особенно завершающие.

> #### Данные: файл data.py
> Тела POST-запросов вынеси в отдельный файл `data.py`.

> #### Тесты: файл create_kit_name_kit_test.py
> - Весь чек-лист нужно писать в отдельном файле. Его можно назвать `create_kit_name_kit_test.py` .
> - Для запуска Pytest можно указать файлы и каталоги. Если этого не сделать, Pytest будет искать тесты в текущем рабочем каталоге и подкаталогах. Ему нужны файлы, начинающиеся с `test_` или заканчивающиеся на `_test`. Поиск не регистрозависимый: в выборку попадёт и `Test_1.py`, и `test_1.py`.
> - Можно создать функцию, которая будет менять содержимое тела запроса. Назови ее `get_kit_body` и добавь параметр `name` .
> - В чек-листе два вида проверок: позитивные и негативные (с кодом 400.) Их логику можно вынести в отдельные функции:`positive_assert(kit_body)` и `negative_assert_code_400(kit_body)`:.
> - Получение токена тоже может быть отдельной функцией. Назови ее `get_new_user_token()`.
> - Каждый тест должен быть в отдельной функции с префиксом `test`. 

> #### Файл README.md
> - Для проверки написанного текста используй сервис https://dillinger.io/.
> -Переиспользуй файл README.md из урока «Вспомогательные файлы проекта: gitignore и README».

> #### Файл .gitignore
> Переиспользуй файл из урока «Вспомогательные файлы проекта: gitignore и README».

## Автор

Иванцовская Виктория, 19 когорта 