from django.db import models

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    kart = models.TextField('Карточка')


    def __str__(self):
        return self.title 
