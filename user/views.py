from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Person


def index(request):
    people = Person.objects.all()
    return render(request, 'index.html', {'people': people})


def create(request):
    if request.method == 'POST':
        object1 = Person()
        object1.name = request.POST.get('name')
        object1.age = request.POST.get('age')
        object1.save()
    return HttpResponseRedirect('/')



