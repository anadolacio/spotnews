from django.urls import path
from news.views import home_page, details_of_news

urlpatterns = [
    path("", home_page, name="home-page"),
    path("news/", home_page, name="news-details-page"),
    path("news/<int:id>/", details_of_news, name="news-details-page"),
]
