from django.forms import ModelForm
from .models import Articles, RewiewArticle, RewiewRecipe, Recipies
from django import forms


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'topics', 'image', 'description']
        widgets = {'topics': forms.CheckboxSelectMultiple()}
        labels = {'title': 'Название статьи', 'topics': 'Тема статьи', 'image': 'Выберите изображение',
                  'description': 'Текст статьи'}


class RecipiesForm(ModelForm):
    class Meta:
        model = Recipies
        fields = ['title', 'image', 'ingredients', 'description']
        labels = {'title': 'Название рецепта', 'image': 'Выберите изображение', 'ingredients': 'Ингредиенты',
                  'description': 'Описание'}


class ReviewForm(ModelForm):
    class Meta:
        model = RewiewArticle
        fields = ['body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'field_text'})


class ReviewFormRecipe(ModelForm):
    class Meta:
        model = RewiewRecipe
        fields = ['body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'field_text'})
