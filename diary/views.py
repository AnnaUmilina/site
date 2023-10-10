from django.shortcuts import render, redirect
from .forms import DiaryForm
from .models import Food
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta, time
from django.db.models import Q
from django.db.models import Sum


@login_required(login_url='login-user')
def diary_food(request):
    form = DiaryForm()
    profile = request.user.profile
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())
    today_end = datetime.combine(tomorrow, time())
    models = Food.objects.filter(Q(date__lte=today_end) & Q(date__gte=today_start))
    total_carbs = models.aggregate(Sum('carbs')).get('carbs__sum')
    total_protein = models.aggregate(Sum('protein')).get('protein__sum')
    total_fats = models.aggregate(Sum('fats')).get('fats__sum')
    total_calories = models.aggregate(Sum('calories')).get('calories__sum')

    if request.method == "POST":
        form = DiaryForm(request.POST)
        if form.is_valid():
            object = form.save(commit=False)
            object.owner = profile
            object.name = request.POST['name']
            object.weight = request.POST['weight']
            object.carbs = float(request.POST['carbs']) / 100 * float(object.weight)
            object.protein = float(request.POST['protein']) / 100 * float(object.weight)
            object.fats = float(request.POST['fats']) / 100 * float(object.weight)
            object.calories = float(request.POST['calories']) / 100 * float(object.weight)
            object.save()
            return redirect('diary-food')
    context = {
        'form': form,
        'models': models,
        'today': today,
        'total_carbs': total_carbs,
        'total_protein': total_protein,
        'total_fats': total_fats,
        'total_calories': total_calories,
    }
    return render(request, 'diary/diary-index.html', context)


@login_required(login_url='login-user')
def food_delete(request, pk):
    food = Food.objects.get(id=pk)
    if request.method == 'POST':
        food.delete()
        return redirect('diary-food')
    context = {'object': food}
    return render(request, 'diary/diary-index.html', context)
