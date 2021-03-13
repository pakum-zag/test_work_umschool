# Generated by Django 3.1.7 on 2021-03-12 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Чат',
                'verbose_name_plural': 'Чаты',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, verbose_name='Полное имя')),
                ('status', models.CharField(choices=[('student', 'Студент'), ('manager', 'Менеджер')], max_length=50, null=True, verbose_name='Статус пользователя')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who_wrote', models.CharField(choices=[('student', 'Студент'), ('manager', 'Менеджер')], max_length=50, verbose_name='Кто написал?')),
                ('message', models.TextField(max_length=500, verbose_name='Сообщение')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.chat', verbose_name='Чат')),
            ],
            options={
                'verbose_name': 'Сообшение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название предмета')),
                ('managers', models.ManyToManyField(related_name='managers', to='main_app.UserProfile', verbose_name='Менеджеры, что имеют доступ к предмету')),
                ('students', models.ManyToManyField(related_name='students', to='main_app.UserProfile', verbose_name='Студенты, что имеют доступ к предмету')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
            },
        ),
        migrations.AddField(
            model_name='chat',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.lesson', verbose_name='Предмет'),
        ),
        migrations.AddField(
            model_name='chat',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
