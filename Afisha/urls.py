"""
URL configuration for Afisha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from movie_app.views import (directors_list_create_api_view,
directors_detail_api_view,
movies_list_create_api_view,
movies_detail_api_view,
reviews_detail_api_view ,
reviews_list_create_api_view,
register_user,
confirm_user,
CustomAuthToken)




urlpatterns = [
    path('admin/', admin.site.urls),
    # Directors
    path('api/v1/directors/', directors_list_create_api_view),
    path('api/v1/directors/<int:id>/', directors_detail_api_view),
    # Movies
    path('api/v1/movies/', movies_list_create_api_view),
    path('api/v1/movies/<int:id>/', movies_detail_api_view),
    # Reviews
    path('api/v1/reviews/', reviews_list_create_api_view),
    path('api/v1/reviews/<int:id>/', reviews_detail_api_view),
    path('api/v1/users/register/', register_user),
    path('api/v1/users/confirm/', confirm_user),
    path('api/v1/login/', CustomAuthToken.as_view())
]
