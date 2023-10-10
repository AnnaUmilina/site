from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Body
from django.forms import ModelForm


class RegisterCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'register'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'last_name', 'email', 'date_of_birth', 'start_weight', 'profile_photo', 'social_website']
        labels = {'name': 'Имя', 'last_name': 'Фамилия', 'date_of_birth': 'Дата рождения',
                  'start_weight': 'Стартовый вес(кг)', 'profile_photo': 'Фото',
                  'social_website': 'Ссылка на социальную сеть'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'profile_input'})
        self.fields['profile_photo'].widget.attrs.update({'class': 'profile_photo'})
        self.fields['start_weight'].widget.attrs.update({'class': 'profile_input profile_start_weight'})
        self.fields['social_website'].widget.attrs.update({'class': 'profile_input profile_social_website'})


class BodyForm(ModelForm):
    class Meta:
        model = Body
        fields = ['weight', 'chest_girth', 'arm_chest', 'waist', 'lower_abdomen', 'hip_girth', 'leg_girth',
                  'calf_girth']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'body_input', 'min': '1'})
