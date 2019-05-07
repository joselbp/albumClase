from django.shortcuts import render
from django.http import HttpResponse
from album.models import Category, Photo
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from rest_framework import viewsets
from .serializer import CategorySerializer, PhotoSerializer

# Create your views here.

def first_view(request):
    return render(request, 'base.html')

class CategoryListView(ListView):
	model=Category

class CategoryDetailView(DetailView):
	model=Category

class CategoryCreate(CreateView):
	model=Category
	fields='__all__'

class CategoryUpdateView(UpdateView):
	model=Category
	fields='__all__'
	
class CategoryDeteleView(DeleteView):
	model=Category
	success_url=reverse_lazy('category-list')

class PhotoListView(ListView):
	model = Photo

class PhotoDetailView(DetailView):
	model = Photo

class PhotoUpdate(UpdateView):
	model = Photo
	fields = '__all__'

class PhotoCreate(CreateView):
	model = Photo
	fields = '__all__'
	
class PhotoDelete(DeleteView):
    model = Photo
    success_url = reverse_lazy('photo-list')

class CategoryList(viewsets.ModelViewSet):
	queryset=Category.objects.all()
	serializer_class=CategorySerializer

class PhotoList(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer