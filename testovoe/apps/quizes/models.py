from django.db import models
from django.db.models.base import Model


class Quiz(models.Model):
    quiz_name = models.CharField('Название опроса', max_length=100)
    quiz_start_time = models.DateTimeField('Дата старта')
    quiz_end_time = models.DateTimeField('Дата окончания')
    quiz_description = models.TextField('Описание опроса')

    def __str__(self):
        return self.quiz_name

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField('Текст вопроса', max_length=500)
    QUESTION_TYPE = (
        (1, "ответ текстом"),
        (2, "Ответ с выбором одного варианта"),
        (3, "Ответ с выбором нескольких вариантов"),
    )
    question_type = models.IntegerField('Тип вопроса', choices=QUESTION_TYPE)


    def __str__(self):
        return self.question_text


class User(models.Model):
    user_name = models.CharField('имя пользователя', max_length=50)

    def __str__(self):
        return self.user_name

class Complited(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz_number = models.IntegerField('Номер опроса')
    question_number = models.IntegerField('Номер вопроса')
    answer = models.TextField('Ответ пользователя')

    def __str__(self):
        return self.quiz_number