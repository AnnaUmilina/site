from django.db import models
from user.models import Profile


class Purpose(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Lifestyle(models.Model):
    name = models.CharField(max_length=200, verbose_name='Образ жизни')
    values = models.FloatField(blank=True, null=True, verbose_name='Коэффициент')

    def __str__(self):
        return self.name


class Calculator(models.Model):
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, verbose_name='Пол')
    age = models.IntegerField(verbose_name='Возраст')
    height = models.IntegerField(verbose_name='Рост')
    weight = models.IntegerField(verbose_name='Вес')
    lifestyle = models.ManyToManyField(Lifestyle, verbose_name='Образ жизни')
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE, verbose_name='Ваша цель')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True)

    def __str__(self):
        return self.user.username


class Food(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)

    name = models.CharField(max_length=100)
    weight = models.FloatField(null=True, blank=True, default='100')
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']


class Consume(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)
