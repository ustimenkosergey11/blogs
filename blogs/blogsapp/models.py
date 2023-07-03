from django.contrib.auth.models import AbstractUser
from django.db import models


class Post(models.Model):
    title = models.CharField('Название', max_length=255, blank=False)
    description = models.TextField('Содержание', max_length=5000)
    author = models.CharField('Автор', max_length=100, blank=False)
    img = models.ImageField('Фото', upload_to='image/%Y/%m/%d')
    datetime = models.DateTimeField('Дата и время', auto_now=True)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return f'{self.title} от {self.author} {self.datetime}'


class User(AbstractUser):
    pass
