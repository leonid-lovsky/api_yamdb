import csv
import os

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

from api_yamdb.settings import BASE_DIR
from reviews.models import Category, Comments, Genre, Review, Title

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        # if User.objects.exists():
        #     raise Exception('Таблица `Users` не пуста!')
        # if Review.objects.exists():
        #     raise Exception('Таблица `Review` не пуста!')
        # if Comments.objects.exists():
        #     raise Exception('Таблица `Comments` не пуста!')
        # if Category.objects.exists():
        #     raise Exception('Таблица `Category` не пуста!')
        # if Genre.objects.exists():
        #     raise Exception('Таблица `Genre` не пуста!')
        # if Title.objects.exists():
        #     raise Exception('Таблица `Titles` не пуста!')

        Comments.objects.all().delete()
        Review.objects.all().delete()
        Title.objects.all().delete()
        Genre.objects.all().delete()
        Category.objects.all().delete()
        User.objects.all().delete()

        data_path = os.path.join(BASE_DIR, 'static/data')
        self.import_db(Genre, os.path.join(data_path, 'genre.csv'))
        self.import_db(Category, os.path.join(data_path, 'category.csv'))
        self.import_db(Title, os.path.join(data_path, 'titles.csv'))
        self.import_db(User, os.path.join(data_path, 'users.csv'))
        self.import_db(Review, os.path.join(data_path, 'review.csv'))
        self.import_db(Comments, os.path.join(data_path, 'comments.csv'))
        self.import_db(
            Title.genre.through, os.path.join(data_path, 'genre_title.csv')
        )

    def import_db(self, table, file_path):
        # counter = 0
        with open(file_path, encoding="utf8") as file:
            reader = csv.reader(file)
            columns = next(reader)
            for row in reader:
                table.objects.create(**dict(zip(columns, row)))
                # counter += 1
        # print(f'{table} added columns: {counter}')
