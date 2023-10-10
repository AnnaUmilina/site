from django.forms import ModelForm
from .models import Food


class DiaryForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name','weight', 'carbs', 'protein', 'fats', 'calories']
        labels = {'name': 'Продукт', 'weight':'Вес продукта(г)','carbs': 'Углеводы(на 100 г)',
                  'protein': 'Белки(на 100 г)', 'fats': 'Жиры(на 100 г)', 'calories': 'Калории(на 100 г)'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'diary_input','min': '1'})
        self.fields['name'].widget.attrs.update({'class': 'diary_input special'})
