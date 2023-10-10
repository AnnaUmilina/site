from django.db import models
from django.urls import reverse


class Fitness(models.Model):
    type_of_training = models.CharField(max_length=300, verbose_name='Вид тренировок')
    short_description = models.TextField(blank=True, null=True, verbose_name='Краткое описание')
    image = models.ImageField(upload_to='fitness/', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return self.type_of_training


class Training(models.Model):
    owner = models.ForeignKey(Fitness, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=250, verbose_name='Вид тренировок')
    image = models.ImageField(verbose_name='Изображение')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']
