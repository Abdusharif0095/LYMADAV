from django.db import models
from django.urls import reverse
# from .forms import CommentForm


class Position(models.Model):
    name = models.CharField(max_length=30, verbose_name='Должность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id_id": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class User(models.Model):
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Должность')
    fullname = models.CharField(max_length=50, verbose_name='ФИО')
    email = models.CharField(max_length=50, verbose_name='Эл. Почта')
    password = models.CharField(max_length=30, verbose_name='Пароль')
    birthday = models.DateField(verbose_name='День Рождения')
    photo = models.ImageField(upload_to='photos/user/', blank=True, verbose_name='Фото')
    about = models.TextField(blank=True, verbose_name='О пользователе')
    status = models.BooleanField(default=False, verbose_name='Регистрирован')

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']


class News(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=100, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, default='photos/logo.png', verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    is_reviewed = models.BooleanField(default=False, verbose_name='Рассмотрено')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"news_id": self.pk})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Comment(models.Model):
    news_id = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Наименование')
    writer = models.CharField(max_length=40, verbose_name='Пользователь')
    content = models.TextField(blank=True, verbose_name='Контент')
    time = models.DateTimeField(auto_now_add=True, verbose_name='Время')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.writer

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['id']
