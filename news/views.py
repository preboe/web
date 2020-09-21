from django.shortcuts import render
from .models import Artiles
from  .forms import ArtilesForm


def news_home(request):
    news = Artiles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


def create(request):
    form = ArtilesForm

    date = {
        'form': form
    }

    return render(request, 'news/create.html', date)