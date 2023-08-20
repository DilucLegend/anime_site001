from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
def main_page(request):
    all_categories = models.Category.objects.all()
    all_anime = models.Anime.objects.all()


    context = {'all_categories': all_categories, 'all_anime':all_anime}
    return render(request, 'index.html', context)

def get_category(request, pk):
    exact_category = models.Anime.objects.filter(category_name__id=pk)

    context = {'category_anime': exact_category}
    return render(request, 'category.html', context)

def get_anime(request, name, pk):
    exact_anime = models.Anime.objects.get(name=name, id=pk)

    context = {'exact_anime': exact_anime}
    return render(request, 'anime.html', context)