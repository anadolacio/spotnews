from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from news.forms import CategoriesForm

# Create your views here.


def home_page(request):
    all_news = News.objects.all()
    new = {"news_list": all_news}
    return render(request, "home.html", new)


def details_of_news(request, id):
    news = {"news_details": get_object_or_404(News, id=id)}
    return render(request, "news_details.html", news)


def categories_register(request):
    if request.method == "POST":
        form = CategoriesForm(request.POST)
        if form.is_valid():
            return redirect("home-page")
    else:
        form = CategoriesForm()

    formulario = {"form": form}
    return render(request, "categories_form.html", formulario)
