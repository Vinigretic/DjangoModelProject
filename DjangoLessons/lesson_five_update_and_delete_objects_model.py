# Редактирование данных

# Описываем views для редактирования
# def edit(request, id):
#     try:
#         object1 = Person.objects.get(id=id)
#         # создаем обьект класса в который получаем данные из бд
#         # id передается в функцию из HTML
#         # <td><a href = "edit/{{ person.id }}" > Изменить < / a > | < a
#         # href = "delete/{{ person.id }}" > Удалить < / a > < / td >
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
# # Описываем views удаления
# def delete(request, id):
#     try:
#         object1 = Person.objects.get(id=id)
#         object1.delete()
#         return HttpResponseRedirect('/')
#     except Person.DoesNotExist:
#         return HttpResponseNotFound('<h2>Person NotFound</h2>')
#
# Описываем страницу для edit
#
# <body class="container">
#     <form method="POST">
#         {% csrf_token %}
#         <p>
#             <label>Введите имя</label> <br>
#             <input type="text" name="name" value="{{person.name}}"/>
#         </p>
#         <p>
#             <label>Введите возраст</label> <br>
#             <input type="number" name="age" value="{{person.age}}"/>
#         </p>
#         <input type="submit" value="save">
#     </form>

# Корректируем  index
# Добавляем код который будет отправлять id во views,
#       {% for person1 in people %}-->
#         <tr>
#             <td>{{ person1.id }}</td>
#             <td>{{ person1.name }}</td>
#             <td>{{ person1.age }}</td>
#             <td><a href="edit/{{ person1.id }}">Изменить</a> | <a href="delete/{{ person1.id }}">Удалить</a></td>
#         </tr>


# Описываем url
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index),
#     path('create/', views.create),
#     path('edit/<int:id>/', views.edit),
#     path('delete/<int:id>/', views.delete)
#
# ]

# Побудувати таблицю в базі даних cars, з полями brand, car_age, color. Добавити можливість редагування,
# створення та видалення полів на  UI.