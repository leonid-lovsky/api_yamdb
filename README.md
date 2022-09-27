# API YAMDB
### Авторы проекта: 
> ***Леонид Ловский***
> ***Константин Шперлинг***
> ***Сергей Тюрников***

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
