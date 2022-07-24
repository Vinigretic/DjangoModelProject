from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
# from .models import Person
# from .models import Cars
# from .models import ListCars


# # Get data from db
# def index(request):
#     people = Person.objects.all()
#     return render(request, 'index.html', {'people': people})
#
#
# # Save data in db
# def create(request):
#     if request.method == 'POST':
#         object1 = Person()
#         object1.name = request.POST.get('name')
#         object1.age = request.POST.get('age')
#         object1.save()
#     return HttpResponseRedirect('/')
#
#
# # Update data in db
# def edit(request, id):
#     try:
#         object1 = Person.objects.get(id=id)
#
#         if request.method == 'POST':
#             object1.name = request.POST.get('name')
#             object1.age = request.POST.get('age')
#             object1.save()
#             return HttpResponseRedirect('/')
#         else:
#             return render(request, 'edit.html', {'person': object1})
#     except Person.DoesNotExist:
#         return HttpResponseNotFound('<h2>Person NotFound</h2>')
#
#
# # Delete data from db
# def delete(request, id):
#     try:
#         object1 = Person.objects.get(id=id)
#         object1.delete()
#         return HttpResponseRedirect('/')
#     except Person.DoesNotExist:
#         return HttpResponseNotFound('<h2>Person NotFound</h2>')


# # get information from db
# def cars_index(request):
#     cars = ListCars.objects.all()
#     return render(request, 'cars_index.html', {'cars': cars})
#
# # create and save new object
# def create_object(request):
#     if request.method == 'POST':
#         object1 = ListCars()
#         object1.brand = request.POST.get('brand')
#         object1.age = request.POST.get('age')
#         object1.color = request.POST.get('color')
#         object1.save()
#     return HttpResponseRedirect('/')
#
# # update object
# def cars_edit(request, id):
#     try:
#         object1 = ListCars.objects.get(id=id)
#
#         if request.method == 'POST':
#             object1.brand = request.POST.get('brand')
#             object1.age = request.POST.get('age')
#             object1.color = request.POST.get('color')
#             object1.save()
#             return HttpResponseRedirect('/')
#         else:
#             return render(request, 'cars_edit.html', {'object_update': object1})
#     except ListCars.DoesNotExist:
#         return HttpResponseNotFound('<h2>Car NotFound</h2>')
#
#
# # delete object
# def delete(request, id):
#     try:
#         object1 = ListCars.objects.get(id=id)
#         object1.delete()
#         return HttpResponseRedirect('/')
#     except ListCars.DoesNotExist:
#         return HttpResponseNotFound('<h2>Car NotFound</h2>')