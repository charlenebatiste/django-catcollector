from django.shortcuts import render
from .models import Cat
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.
def profile(request, username):
    user = User.objects.get(username=username)
    cats = Cat.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'cats': cats})
    
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

# forms - generic from django
class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    success_url = '/cats'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/cats')

class CatUpdate(UpdateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/cats/' + str(self.object.pk))

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats'