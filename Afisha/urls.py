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
from django.urls import path# urls.py
from django.contrib import admin
from django.urls import path
from movie_app.views import (
    DirectorListCreateView,
    DirectorRetrieveUpdateDestroyView,
    MovieListCreateView,
    MovieRetrieveUpdateDestroyView,
    ReviewListCreateView,
    ReviewRetrieveUpdateDestroyView,
    RegisterUserView,
    ConfirmUserView,
    CustomAuthToken
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Directors
    path('api/v1/directors/', DirectorListCreateView.as_view()),
    path('api/v1/directors/<int:id>/', DirectorRetrieveUpdateDestroyView.as_view()),
    # Movies
    path('api/v1/movies/', MovieListCreateView.as_view()),
    path('api/v1/movies/<int:id>/', MovieRetrieveUpdateDestroyView.as_view()),
    # Reviews
    path('api/v1/reviews/', ReviewListCreateView.as_view()),
    path('api/v1/reviews/<int:id>/', ReviewRetrieveUpdateDestroyView.as_view()),
    # Users
    path('api/v1/users/register/', RegisterUserView.as_view()),
    path('api/v1/users/confirm/', ConfirmUserView.as_view()),
    path('api/v1/login/', CustomAuthToken.as_view())
]

