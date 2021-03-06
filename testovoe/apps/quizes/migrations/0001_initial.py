# Generated by Django 3.2.4 on 2021-06-17 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_name', models.CharField(max_length=100, verbose_name='Название опроса')),
                ('quiz_start_time', models.DateTimeField(verbose_name='Дата старта')),
                ('quiz_end_time', models.DateTimeField(verbose_name='Дата окончания')),
                ('quiz_description', models.TextField(verbose_name='Описание опроса')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=500, verbose_name='Текст вопроса')),
                ('question_type', models.IntegerField(verbose_name='Тип вопроса')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizes.quiz')),
            ],
        ),
    ]
