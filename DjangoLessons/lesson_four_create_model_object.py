# Создание обьектов моделей

# Все классы для моделей создаются в файле models.py. Все CRUDE операции описываем во views

# Создаем модель в файле models.py
#
# class Person(models.Model):
#     name = models.CharField(max_length=20)
#     age = models.IntegerField()


# Описываем CRUDE операции в файле views

# делаем импорты

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Person

# Описываем views

# 1. Создаем переменную в которую передаем все атрибуты класса Person
# Затем передаем ее в HTML файл
#
# def index(request):
#     people = Person.objects.all()
#     return render(request, 'index.html', {'people': people})

# 2. Создаем views для формы
# Создаем обьект класса Person
# Вытягиваем из формы данные в его атрибуты
# Сохраняем
# Делаем возврат на главную страницу
#
# def create(request):
#     if request.method == 'POST':
#         object1 = Person()
#         object1.name = request.POST.get('name')
#         object1.age = request.POST.get('age')
#         object1.save()
#     return HttpResponseRedirect('/')

# Описываем HTML файл
#
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
# </head>
# <body class="container">
#     <form method="POST" action="create/"> action="create/" - привязка действия к HTML файлу, ссылка указывает на
#         {% csrf_token %}                                     url, а дальше на view
#         <p>
#             <label>Input name</label> <br>  тег label подпись поля формы, тег <br> перевод на новую строку
#             <input type="text" name="name"/>
#         </p>
#         <p>
#             <label>Input age</label> <br>
#             <input type="number" name="age">
#         </p>
#         <input type="submit" value="save">
#     </form>
#     {% if people.count > 0 %}
#     <h2>the List of users</h2>
#     <table>
#         <tr>
#             <th>Id</th>
#             <th>Name</th>
#             <th>Age</th>
#         </tr>
#         {% for person in people %}
#         <tr>
#             <td>{{ person.id }}</td>
#             <td>{{ person.name }}</td>
#             <td>{{ person.age }}</td>
#         </tr>
#         {% endfor %}
#     </table>
#     {% endif %}
# </body>
# </html>