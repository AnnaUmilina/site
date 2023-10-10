# Generated by Django 4.2.4 on 2023-08-18 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('food', '0004_alter_rewiewrecipe_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Комментарий')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.articles')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
            ],
            options={
                'unique_together': {('owner', 'article')},
            },
        ),
        migrations.CreateModel(
            name='ReviewRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Комментарий')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.recipies')),
            ],
            options={
                'unique_together': {('owner', 'recipe')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='rewiewrecipe',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='rewiewrecipe',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='rewiewrecipe',
            name='recipe',
        ),
        migrations.DeleteModel(
            name='RewiewArticle',
        ),
        migrations.DeleteModel(
            name='RewiewRecipe',
        ),
    ]
