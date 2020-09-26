from django.shortcuts import render

def app(request):
    return request(request, 'weather/app.html')
