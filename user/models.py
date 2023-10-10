from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    username = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    start_weight = models.IntegerField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile/', default='profile/photo_profile.jpg')
    social_website = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.username


class Body(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)

    weight = models.FloatField(null=True, blank=True, default=0, verbose_name='Вес')
    chest_girth = models.FloatField(null=True, blank=True, default=0, verbose_name='Обхват груди')
    arm_chest = models.FloatField(null=True, blank=True, default=0, verbose_name='Обхват рук')
    waist = models.FloatField(null=True, blank=True, default=0, verbose_name='Талия')
    lower_abdomen = models.FloatField(null=True, blank=True, default=0, verbose_name='Низ живота')
    hip_girth = models.FloatField(null=True, blank=True, default=0, verbose_name='Обхват бедер')
    leg_girth = models.FloatField(null=True, blank=True, default=0, verbose_name='Обхват ног')
    calf_girth = models.FloatField(null=True, blank=True, default=0, verbose_name='Обхват икр')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ['-date']