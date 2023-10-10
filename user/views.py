from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Body
from .forms import RegisterCreationForm, ProfileForm, BodyForm
from food.models import Articles


def login_user(request):
    if request.user.is_authenticated:
        return redirect('account')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            print('Username does not exists')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            print("Username or password is incorrect")
    return render(request, 'user/authorisation.html')


def registration(request):
    form = RegisterCreationForm()

    if request.method == 'POST':
        form = RegisterCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('account')
    context = {
        'form': form
    }
    return render(request, 'user/registration.html', context)


@login_required(login_url='login-user')
def account(request):
    profile = request.user.profile
    articles = Articles.objects.filter(owner=request.user.id)
    if articles.exists():
        return render(request, 'user/account.html', {'articles': articles, 'profile': profile})
    else:
        articles = None
        return render(request, 'user/account.html', {'articles': articles, 'profile': profile})


@login_required(login_url='login-user')
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')


@login_required(login_url='login-user')
def profile_user(request):
    prof = request.user.profile
    context = {'profile': prof}
    return render(request, 'user/profile.html', context)


@login_required(login_url='login-user')
def edit_profile(request):
    prof = request.user.profile
    form = ProfileForm(instance=prof)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=prof)
        if form.is_valid():
            form.save()
            return redirect('profile-user')
    context = {'form': form, 'profile': prof}
    return render(request, 'user/edit_profile.html', context)


@login_required(login_url='login-user')
def body(request):
    obj = Body.objects.filter(user=request.user.id)
    context = {
        'obj': obj,
    }
    return render(request, 'user/body.html', context)


@login_required(login_url='login-user')
def update_body(request):
    profile = request.user.profile
    form = BodyForm()
    if request.method == 'POST':
        form = BodyForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = profile
            obj.save()
            return redirect('body')
    else:
        return render(request, 'user/update_body.html', {'form': form})
