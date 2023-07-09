"""
URL configuration for sports_news project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import NewsViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    # endpoint for creating news

    path('news/', NewsViewSet.as_view({"post":"create"}), name="create_news_api_view"),
    path('news/sport/<int:sport_id>/', NewsViewSet.as_view({"get": "get_sport_news"}), name="sport_news_api_view"),
    path('news/tour/<int:tour_id>/',NewsViewSet.as_view({"get": "get_tour_news"}), name="tour_new_api_view" ),
    path('news/match/<int:match_id>/', NewsViewSet.as_view({"get": "get_match_news"}), name="match_news_api_view")
]
