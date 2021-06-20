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
    path('admin/', admin.site.urls),
    path('', home_views.home, name='home'),
    path('<int:pk>/', home_views.sub_categories, name='sub_category'),
    path('topic/<int:topic>/', home_views.topic, name='topic'),
    path('<int:topic>/relate/', home_views.relate_to_topic, name='relate'),
    path('<int:topic>/check_relate/', home_views.check_related, name='check_relate'),

    #ajax
    path('experience/<str:topic>', home_views.add_experience, name='add_experience'),


    #about
    path('about/', home_views.about, name='about'),

]
