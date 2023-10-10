from django.db import models
from user.models import Profile


class Topic(models.Model):
    name = models.CharField(max_length=200, verbose_name='Тема')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Articles(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)

    title = models.CharField(max_length=200, verbose_name='Название статьи')
    topics = models.ManyToManyField(Topic, blank=True, verbose_name='Тема')
    image = models.ImageField(upload_to='articles/', default='articles/default.jpg',
                              blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(verbose_name='Текст статьи')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']


class Recipies(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название рецепта')
    image = models.ImageField(upload_to='recipes/', verbose_name='Фото')
    ingredients = models.TextField(verbose_name='Ингредиенты')
    description = models.TextField(verbose_name='Текст рецепта')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']


class Diets(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название диеты')
    image = models.ImageField(upload_to='diets/', verbose_name='Картинка')
    description = models.TextField(verbose_name='Описание диеты')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class RewiewArticle(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    body = models.TextField(verbose_name='Комментарий')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ['-date']


class RewiewRecipe(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipies, on_delete=models.CASCADE)
    body = models.TextField(verbose_name='Комментарий')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ['-date']