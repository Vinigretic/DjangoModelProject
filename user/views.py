from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Person


# Get data from db
def index(request):
    people = Person.objects.all()
    return render(request, 'index.html', {'people': people})


# Save data in db
def create(request):
    if request.method == 'POST':
        object1 = Person()
        object1.name = request.POST.get('name')
        object1.age = request.POST.get('age')
        object1.save()
    return HttpResponseRedirect('/')


# Update data in db
def edit(request, id):
    try:
        object1 = Person.objects.get(id=id)

        if request.method == 'POST':
            object1.name = request.POST.get('name')
            object1.age = request.POST.get('age')
            object1.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'edit.html', {'person': object1})
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Person NotFound</h2>')


# Delete data from db
def delete(request, id):
    try:
        object1 = Person.objects.get(id=id)
        object1.delete()
        return HttpResponseRedirect('/')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Person NotFound</h2>')





