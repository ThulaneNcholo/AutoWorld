from django.shortcuts import render

# Create your views here.


def NewsView(request):
    return render(request, 'news/news.html')
