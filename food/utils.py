from .models import Articles, Topic, Recipies
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def search_articles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    topics = Topic.objects.filter(name__icontains=search_query)

    art = Articles.objects.filter(
        Q(title__iregex=search_query) |
        Q(topics__in=topics) |
        Q(description__iregex=search_query))

    return art, search_query


def search_recipes(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    rec = Recipies.objects.filter(
        Q(title__iregex=search_query) |
        Q(ingredients__iregex=search_query))

    return rec, search_query


def paginate_articles(request, art, results):
    page = request.GET.get('page')

    paginator = Paginator(art, results)
    try:
        art = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        art = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        art = paginator.page(page)

    left_index = int(page) - 3
    if left_index < 1:
        left_index = 1

    right_index = int(page) + 4
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, art


def paginate_recipies(request, rec, results):
    page = request.GET.get('page')

    paginator = Paginator(rec, results)
    try:
        rec = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        rec = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        rec = paginator.page(page)

    left_index = int(page) - 3
    if left_index < 1:
        left_index = 1

    right_index = int(page) + 4
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, rec
