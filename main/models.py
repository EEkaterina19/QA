from django.db import models

class Task(models.Model):
    title = models.TextField('Заголовок', max_length=30)
    titleh1 = models.TextField('Главный заголовок', max_length=20)
    button1 = models.TextField('Кнопка1', max_length=50)
    button2 = models.TextField('Кнопка2', max_length=50)

    def __str__(self):
        return self.title 
    


class Task1(models.Model):
    title = models.TextField('Заголовок карточки 1', max_length=30)
    cart= models.TextField('Описание карточки 1', max_length=200)
    button1 = models.TextField('Кнопка карточки 1', max_length=30)
   
    def __str__(self):
        return self.title 
    


class Task2(models.Model):
    title = models.TextField('Заголовок карточки 2', max_length=30)
    cart= models.TextField('Описание карточки 2', max_length=200)
    button2 = models.TextField('Кнопка карточки 2', max_length=30)
   
    def __str__(self):
        return self.title 
    
    
class Task3(models.Model):
    title = models.TextField('Заголовок карточки 3', max_length=30)
    cart= models.TextField('Описание карточки 3', max_length=200)
    button3 = models.TextField('Кнопка карточки 3', max_length=30)
   
    def __str__(self):
        return self.title 

