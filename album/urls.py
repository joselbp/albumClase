"""myapps2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from album import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('category_rest', views.CategoryList)
router.register('photo_rest', views.PhotoList)

urlpatterns = [
    path('',views.first_view,name='base'),
    path('category',views.CategoryListView.as_view(),name='category-list'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('category/create', views.CategoryCreate.as_view(), name='category-create'),
    path('category/<int:pk>/update', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category/<int:pk>/delete', views.DeleteView.as_view(), name='category-delete'),
    path('photo/', views.PhotoListView.as_view(), name='photo-list'),
    path('photo/<int:pk>', views.PhotoDetailView.as_view(), name='photo-detail'),
    path('photo/create/', views.PhotoCreate.as_view(), name='photo-create'),
    path('photo/<int:pk>/update/', views.PhotoUpdate.as_view(), name='photo-update'),
    path('photo/<int:pk>/delete/', views.PhotoDelete.as_view(), name='photo-delete'),
    path('api/', include(router.urls)),
]