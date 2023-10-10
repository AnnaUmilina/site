# Generated by Django 4.2.4 on 2023-09-18 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fitness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_training', models.CharField(max_length=300, verbose_name='Вид тренировок')),
                ('short_description', models.TextField(blank=True, null=True, verbose_name='Краткое описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='fitness/', verbose_name='Изображение')),
            ],
        ),
    ]