"""mealPlan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from .views import home, forgetPassword, recipe, about, register, uploadHome, upload, editRecipe, editRecipeHome
from .views import viewRecipe

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", home),
    path("forgetPassword/", forgetPassword),
    path("recipe/", recipe),
    path("about/", about),
    path("register/", register),
    #path("login/", login),
    path("uploadHome/", uploadHome),
    path("upload/", upload),
    path("editRecipeHome/", editRecipeHome),
    path("editRecipe/", editRecipe),
    path("viewRecipe/", viewRecipe),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", RedirectView.as_view(url="accounts/login"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

