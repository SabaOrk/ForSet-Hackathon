"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from project.apps.home import views as home_views
from project.apps.subcategory import views as subcategory_views

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),

    #main
    path('', home_views.home, name='home'),
    path('<slug:title>/subcategories/', subcategory_views.sub_categories, name='sub_categories'),
    path('topic/<slug:slug>', home_views.topic, name='topic'),
    path('<slug:category>/<slug:subcategory>/<slug:title>/relate/', home_views.relate_to_topic, name='relate'),
    path('<slug:category>/<slug:subcategory>/<slug:title>/check_relate/', home_views.check_related, name='check_relate')

    #about
    path('about/', home_views.about, name='about'),


]
