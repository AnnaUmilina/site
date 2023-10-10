from django.contrib import admin
from .models import Topic, Articles, Recipies, Diets, RewiewArticle, RewiewRecipe


admin.site.register(Topic)
admin.site.register(Articles)
admin.site.register(Recipies)
admin.site.register(Diets)
admin.site.register(RewiewArticle)
admin.site.register(RewiewRecipe)
