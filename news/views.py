from django.shortcuts import render
from .models import News

# Create your views here.


def home_page(request):
    all_news = News.objects.all()
    new = {"news_list": all_news}
    return render(request, "home.html", new)
