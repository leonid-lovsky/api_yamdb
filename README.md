# API YAMDB
## Авторы проекта 
- Сергей Тюрников
- Леонид Ловский
- Константин Шперлинг

## Описание
**YAMDB** - проект сервиса, позволяющего пользователям оставлять отзывы на произведения в трех категориях (_список категорий может быть расширен_), а также ставить им оценку (_1-10_):
1. Книги
2. Фильмы
3. Музыка

На одно произведение пользователь может оставить только один отзыв. 
Пользователи могут оставлять комментарии под отзывами.
Произведениям может быть присвоен жанр (_из списка предустановленных_).

## Технологии в проекте
- requests 2.26.0
- django 2.2.16
- djangorestframework 3.12.4
- PyJWT 2.1.0
- pytest 6.2.4
- pytest-django 4.4.0
- pytest-pythonpath 0.7.3
- djangorestframework-simplejwt 5.2.0
- django-filter 21.1

## Запуск проекта в Dev режиме
1. Клонировать репозиторий и перейти в него в командной строке:
```
# Клонирование репозитория
git clone git@github.com:Sergey2107/api_yamdb.git
# Переход в корневую директорию репозитория
cd api_final_yatube
```
2. Cоздать и активировать виртуальное окружение:
```
# Для OS Windows
python -m venv venv
source venv/Scripts/activate
# Для Mac OS/Linux
python3 -m venv venv
# Активация
source venv/bin/activate
```
3. Установить зависимости из файла requirements.txt:
```
# Обновление pip
# Для OS Windows
python -m pip install --upgrade pip
# Для Mac OS/Linux
python3 -m pip install --upgrade pip
# Установка зависимостей
pip install -r requirements.txt
```
4. Выполнить миграции (для этого необходимо перейти в директорию с файлом manage.py):
```
#  Переход в директорию с файлом 
cd api_yamdb
# Для OS Windows
python manage.py migrate
# Для Mac OS/Linux
python3 manage.py migrate
```
5. Запустить проект:
```
# Для OS Windows
python manage.py runserver
# Для Mac OS/Linux
python3 manage.py runserver
```
После запуска по адресу http://127.0.0.1:8000/redoc/ доступна документация проекта.

## Примеры запросов
1. Регистрация нового пользователя:
```
POST /auth/signup/
```
Пример запроса:
```
{
  "email": "string",
  "username": "string"
}
```
Пример ответа:
```
{
  "email": "string",
  "username": "string"
}
```
2. Получение JWT-токена:
```
POST /auth/token/
```
Пример запроса:
```
{
  "username": "string",
  "confirmation_code": "string"
}
```
Пример ответа:
```
{
  "token": "string"
}
```
3. Получение списка всех категорий:
```
GET /categories/
```
Пример ответа:
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "name": "string",
        "slug": "string"
      }
    ]
  }
]
```
4. Добавление новой категории:
```
POST /categories/
```
Пример запроса:
```
{
  "name": "string",
  "slug": "string"
}
```
Пример ответа:
```
{
  "name": "string",
  "slug": "string"
}
```
5. Удаление категории:
```
DELETE /categories/{slug}/
```
6. Получение списка всех жанров:
```
GET /genres/
```
Пример ответа:
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "name": "string",
        "slug": "string"
      }
    ]
  }
]
```
7. Добавление жанра:
```
POST /genres/
```
Пример запроса:
```
{
  "name": "string",
  "slug": "string"
}
```
Пример ответа:
```
{
  "name": "string",
  "slug": "string"
}
```
8. Удаление жанра:
```
DELETE /genres/{slug}/
```
9. Получение списка всех произведений:
```
GET /titles/
```
Пример ответа:
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "name": "string",
        "year": 0,
        "rating": 0,
        "description": "string",
        "genre": [
          {
            "name": "string",
            "slug": "string"
          }
        ],
        "category": {
          "name": "string",
          "slug": "string"
        }
      }
    ]
  }
]
```
10. Добавление произведения:
```
POST /titles/
```
Пример запроса:
```
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```
Пример ответа:
```
{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
```
11. Получение информации о произведении:
```
GET /titles/{titles_id}/
```
Пример ответа:
```
{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
```
12. Частичное обновление информации о произведении:
```
PATCH /titles/{titles_id}/
```
Пример запроса:
```
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```
Пример ответа:
```
{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
```
13. Удаление произведения:
```
DELETE /titles/{titles_id}/
```
14. Получение списка всех отзывов:
```
GET /titles/{title_id}/reviews/
```
Пример ответа:
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "text": "string",
        "author": "string",
        "score": 1,
        "pub_date": "2019-08-24T14:15:22Z"
      }
    ]
  }
]
```
15. Добавление нового отзыва:
```
POST /titles/{title_id}/reviews/
```
Пример запроса:
```
{
  "text": "string",
  "score": 1
}
```
Пример ответа:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```
16. Полуение отзыва по id:
```
GET /titles/{title_id}/reviews/{review_id}/
```
Пример ответа:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```
17. Частичное обновление отзыва по id:
```
PATCH /titles/{title_id}/reviews/{review_id}/
```
Пример запроса:
```
{
  "text": "string",
  "score": 1
}
```
Пример ответа:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```
18. Удаление отзыва по id:
```
DELETE /titles/{title_id}/reviews/{review_id}/
```
19. Получение списка всех комментариев к отзыву:
```
GET /titles/{title_id}/reviews/{review_id}/comments/
```
Пример ответа:
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "text": "string",
        "author": "string",
        "pub_date": "2019-08-24T14:15:22Z"
      }
    ]
  }
]
```
20. Добавление комментария к отзыву:
```
POST /titles/{title_id}/reviews/{review_id}/comments/
```
Пример запроса:
```
{
  "text": "string"
}
```
Пример ответа:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```
21. Получение комментария к отзыву:
```
GET /titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```
Пример ответа:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```
22. Частичное обновление комментария к отзыву:
```
PATCH /titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```
Пример запроса:
```
{
  "text": "string"
}
```
Пример ответа:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```
23. Удаление комментария к отзыву:
```
DELETE /titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```
24. Получение списка всех пользователей:
```
GET /users/
```
Пример ответа:
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "username": "string",
        "email": "user@example.com",
        "first_name": "string",
        "last_name": "string",
        "bio": "string",
        "role": "user"
      }
    ]
  }
]
```
25. Добавление пользователя:
```
POST /users/
```
Пример запроса:
```
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```
Пример ответа:
```
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```
25. Получение пользователя по username:
```
GET /users/{username}/
```
Пример ответа:
```
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```
26. Изменение данных пользователя по username:
```
PATCH /users/{username}/
```
Пример запроса:
```
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```
Пример ответа:
```
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```
27. Удаление пользователя по username:
```
DELETE /users/{username}/
```
28. Получение данных своей учетной записи:
```
GET /users/me/
```
Пример ответа:
```
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```
29. Изменение данных своей учетной записи:
```
PATCH /users/me/
```
Пример запроса:
```
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string"
}
```
Пример ответа:
```
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```
