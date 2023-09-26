from django.shortcuts import render, get_object_or_404
from .models import News

# Create your views here.


def home_page(request):
    all_news = News.objects.all()
    new = {"news_list": all_news}
    return render(request, "home.html", new)


def details_of_news(request, id):
    news = {"news_details": get_object_or_404(News, id=id)}
    return render(request, "news_details.html", news)
