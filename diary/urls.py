from django.urls import path
from . import views


urlpatterns = [
    # path('diary-index/<str:pk>/', views.diary_index, name='diary-index'),
    path('diary-food/', views.diary_food, name='diary-food'),
    path('food-delete/<str:pk>/', views.food_delete, name='food-delete'),
]