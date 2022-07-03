# Reminder_API

### Установка: 
#### Windows
`python -m venv venv `

`venv/Scripts/activate `

`python -m pip install --upgrade pip `

`pip install -r requirements.txt `

#### Linux
`python3 -m venv venv `

`source venv/bin/activate `

`python -m pip install --upgrade pip `

`pip install --upgrade setuptools ` опционально...

`python -m pip install --upgrade pip setuptools` либо так)

`pip install -r requirements.txt `

### Запуск
Перейдити в дирректорию reminder и выполните миграции:

`python manage.py migrate `

Запустите сервер:

`python manage.py runserver`

### Примеры запросов:
##### Создать пользователя

`http://127.0.0.1:8000/api/v1/users/`

в body запроса необходимо передать: 

`{
    "username": "имя",
    "password": "пароль"
}`

##### Получить токен

`http://127.0.0.1:8000/api/v1/jwt/create/`

в body запроса необходимо передать: 

`{
    "username": "имя",
    "password": "пароль"
}`

##### Только авторизованные запросы:

в хедер запроса необходимо передать полученный токен

##### Получить список пользователей
`http://127.0.0.1:8000/api/v1/users/`

##### Информация о конкретном пользователе
`http://127.0.0.1:8000/api/v1/users/1/`

##### Список дней рождения рождения
`http://127.0.0.1:8000/api/v1/birthdays/`
