from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model

NUMBER_OF_SYMBOLS = 20
User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)


class Title(models.Model):
    name = models.CharField(max_length=256)
    year = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    genre = models.ManyToManyField(Genre, related_name='titles')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name='titles', null=True)


class Review(models.Model):
    text = models.TextField(
        verbose_name='Текст отзыва'
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор отзыва',
        related_name='revies',
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации отзыва'
    )
    score = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг',
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    title = models.ForeignKey(
        Title,
        verbose_name='Наименование произведения',
        related_name='reviews',
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text[:NUMBER_OF_SYMBOLS]


class Comments(models.Model):
    title = models.ForeignKey(
        Title,
        related_name='comments',
        verbose_name='Наименование произведения'
        on_delete=models.CASCADE,
        null=True
    )
    review = models.ForeignKey(
        Review,
        related_name='comments',
        verbose_name='Отзыв',
        on_delete=models.CASCADE
    )
    text = models.TextField(
        verbose_name='Текст комментария'
    )
    author = models.ForeignKey(
        'User',
        related_name='comments',
        verbose_name='Автор комментария',
         on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации комментария'
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:NUMBER_OF_SYMBOLS]
        
