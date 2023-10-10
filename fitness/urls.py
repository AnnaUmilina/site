
from django.urls import path
from . import views


urlpatterns = [
    path('training/', views.training, name='training'),
    path('type-of-training/<str:pk>/', views.type_of_training, name='type-of-training'),
]