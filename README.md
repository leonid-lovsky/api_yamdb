# API YAMDB
### Авторы проекта: 
- ***Леонид Ловский***
- ***Константин Шперлинг***
- ***Сергей Тюрников***

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

## Запуск проекта в Dev режиме:
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

## Примеры запросов:
1. Запрос на регистрацию пользователя (POST-запрос):
http://127.0.0.1:8000/api/v1/auth/signup/
2. Запрос на получение JWT-токена (POST-запрос):
http://127.0.0.1:8000/api/v1/auth/token/
3. Запрос на получение списка всех категорий (GET-запрос):
http://127.0.0.1:8000/api/v1/categories/
4. Запрос на добавление новой категории (POST-запрос):
http://127.0.0.1:8000/api/v1/categories/
5. Запрос на удаление категории (DELETE-запрос):
http://127.0.0.1:8000/api/v1/categories/{slug}/
6. Запрос на получение списка всех жанров (GET-запрос):
http://127.0.0.1:8000/api/v1/genres/
7. Запрос на добавление жанра (POST-запрос):
http://127.0.0.1:8000/api/v1/genres/
8. Запрос на удаление жанра (DELETE-запрос):
http://127.0.0.1:8000/api/v1/genres/{slug}/
9. Запрос на получение списка всех произведений (GET-запрос):
http://127.0.0.1:8000/api/v1/titles/
10. Запрос на добавление произведения (POST-запрос):
http://127.0.0.1:8000/api/v1/titles/
11. Запрос на получение информации о произведении (GET-запрос):
http://127.0.0.1:8000/api/v1/titles/{titles_id}/
12. Запрос на частичное обновление информации о произведении (PATCH-запрос):
http://127.0.0.1:8000/api/v1/titles/{titles_id}/
12. Запрос на удаление произведения (DELETE-запрос):
http://127.0.0.1:8000/api/v1/titles/{titles_id}/
13. Запрос на получение списка всех отзывов (GET-запрос):
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
14. Запрос на добавление нового отзыва (POST-запрос):
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
15. Запрос на получение конкретного отзыва (GET-запрос):
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/
16. Запрос на частичное обновление конкретного отзыва (PATCH-запрос):
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/
17. Запрос на удаление конкретного отзыва (DELETE-запрос):
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/
18. Запрос на получение списка всех комментариев (GET-запрос):
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/
19. Запрос на добавление комментария к отзыву (POST-запрос):
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/
20. Запрос на получение конкретного комментария (GET-запрос):
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
21. Запрос на частичное обновление комментария (PATCH-запрос):
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
22. Запрос на удаление комментария (DELETE-запрос):
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/