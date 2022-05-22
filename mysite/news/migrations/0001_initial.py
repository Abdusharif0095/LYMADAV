# Generated by Django 3.2.13 on 2022-05-03 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50, verbose_name='ФИО')),
                ('email', models.CharField(max_length=50, verbose_name='Эл. Почта')),
                ('password', models.CharField(max_length=30, verbose_name='Пароль')),
                ('birthday', models.DateField(verbose_name='День Рождения')),
                ('photo', models.ImageField(blank=True, upload_to='photos/user/', verbose_name='Фото')),
                ('about', models.TextField(blank=True, verbose_name='О пользователе')),
                ('status', models.BooleanField(default=False, verbose_name='Регистрирован')),
                ('position_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.position', verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Наименование')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('photo', models.ImageField(blank=True, default='photos/logo.png', upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликовано')),
                ('is_reviewed', models.BooleanField(default=False, verbose_name='Рассмотрено')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category', verbose_name='Категория')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.user', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=40, verbose_name='Пользователь')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='Время')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('news_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.news', verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
                'ordering': ['id'],
            },
        ),
    ]