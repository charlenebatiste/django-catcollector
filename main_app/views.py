from django.shortcuts import render
from .models import Cat

# Create your views here.

def about(request):
  return render(request, 'about.html')

def index(request):
  return render(request, 'index.html')

def cats_index(request):
    cats = Cat.objects.all()
    data = { 'cats': cats }
    return render(request, 'cats/index.html', data)

def cats_show(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    data = { 'cat': cat }
    return render(request, 'cats/show.html', data)