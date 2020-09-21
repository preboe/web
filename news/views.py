from django.shortcuts import render, redirect
from .models import Artiles
from  .forms import ArtilesForm


def news_home(request):
    news = Artiles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была не верна'

    form = ArtilesForm

    date = {
        'form': form,
        'error': error

    }

    return render(request, 'news/create.html', date)