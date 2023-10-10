from django.core.exceptions import ObjectDoesNotExist
from .models import Fitness, Training
from django.shortcuts import render


def training(request):
    fitness = Fitness.objects.all()

    context = {
        'fitness': fitness,
    }
    return render(request, 'fitness/training.html', context)


def type_of_training(request,pk):
    fitness = Fitness.objects.get(id=pk)
    type = fitness.training_set.all()
    context = {
        'type': type,
        'fitness':fitness,
    }
    return render(request, 'fitness/type_of_training.html', context)
