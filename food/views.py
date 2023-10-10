from django.shortcuts import render, get_object_or_404, redirect
from .models import Articles, Diets, Recipies
from .forms import ArticlesForm, ReviewForm, ReviewFormRecipe, RecipiesForm
from .utils import search_articles, search_recipes, paginate_articles, paginate_recipies
from django.contrib.auth.decorators import login_required


def index(request):
    art, search_query = search_articles(request)
    custom_range, art = paginate_articles(request, art, 6)
    context = {
        'articles': art,
        'search_query': search_query,
        'custom_range': custom_range
    }
    return render(request, 'food/index.html', context)


def diets(request):
    diets = Diets.objects.order_by('-date')
    context = {
        'diets': diets
    }
    return render(request, 'food/diets.html', context)


def recipes(request):
    rec, search_query = search_recipes(request)
    custom_range, rec = paginate_recipies(request, rec, 9)

    context = {
        'recipes': rec,
        'search_query': search_query,
        'custom_range': custom_range
    }
    return render(request, 'food/recipes.html', context)


def recipe(request, id):
    cook = get_object_or_404(Recipies, id=id)
    form = ReviewFormRecipe()
    if request.method == 'POST':
        form = ReviewFormRecipe(request.POST)
        review = form.save(commit=False)
        review.recipe = cook
        review.owner = request.user.profile
        review.save()
        return redirect('recipe', id=cook.id)
    return render(request, 'food/recipe.html', {'recipe': cook, 'form': form})


def detail(request, id):
    post = get_object_or_404(Articles, id=id)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.article = post
        review.owner = request.user.profile
        review.save()
        return redirect('detail', id=post.id)
    return render(request, 'food/detail.html', {'post': post, 'form': form})


@login_required(login_url='login-user')
def create_article(request):
    page = 'create'
    profile = request.user.profile
    form = ArticlesForm()
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = profile
            obj.save()
            return redirect('index')
    return render(request, 'food/user_article.html', {'form': form, 'page': page})


@login_required(login_url='login-user')
def create_recipe(request):
    form = RecipiesForm()
    if request.method == 'POST':
        form = RecipiesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipes')
    return render(request, 'food/user_recipe.html', {'form': form})


@login_required(login_url='login-user')
def update_article(request, pk):
    profile = request.user.profile
    article = profile.articles_set.get(id=pk)
    form = ArticlesForm(instance=article)

    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('account')

    context = {
               'form':form,
               'article': article}

    return render(request, 'food/user_article.html', context)


@login_required(login_url='login-user')
def delete_article(request, pk):
    profile = request.user.profile
    article = profile.articles_set.get(id=pk)

    if request.method == 'POST':
        article.delete()
        return redirect('account')

    context = {'object': article}

    return render(request, 'food/delete.html', context)


@login_required(login_url='login-user')
def delete_comment(request, pk):
    profile = request.user.profile
    comment = profile.rewiewarticle_set.get(id=pk)

    comment.delete()
    return redirect('detail', id=comment.article_id)


@login_required(login_url='login-user')
def delete_comment_recipe(request, pk):
    profile = request.user.profile
    comment = profile.rewiewrecipe_set.get(id=pk)

    comment.delete()
    return redirect('recipe', id=comment.recipe_id)
