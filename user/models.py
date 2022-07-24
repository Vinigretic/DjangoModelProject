from django.db import models
from django.db.models import F
# from cars.models import Dealer  # для связи моделей разных приложений можем импортировать класс другой модели


# class Person(models.Model):
#     name = models.CharField(max_length=20)
#     age = models.IntegerField()
#     city = models.CharField(max_length=20)
#
# class UserAdmin(models.Model):
#     name = models.CharField(max_length=20)
#     surname = models.CharField(max_length=30)
#     email = models.EmailField()
#     is_admin = models.BooleanField()

# class FieldType(models.Model):
#     field1 = models.BinaryField()
#     field2 = models.BooleanField()
#     # field3 = models.NullBooleanField(null=True)
#     field4 = models.DateField()
#     field5 = models.TimeField()
#     field6 = models.DateTimeField()
#     field7 = models.DurationField()
#     # field8 = models.AutoField()
#     field9 = models.BigIntegerField()
#     field10 = models.FloatField()
#     field11 = models.IntegerField()
#     field12 = models.PositiveIntegerField()
#     field13 = models.PositiveSmallIntegerField()
#     field14 = models.SmallIntegerField()
#     field15 = models.CharField(max_length=20)
#     field16 = models.TextField()
#     field17 = models.EmailField()
#     field18 = models.FileField()
#     field19 = models.FilePathField()
#     # field20 = models.ImageField()
#     field21 = models.GenericIPAddressField()
#     field22 = models.SlugField()
#     field23 = models.URLField()

# class Person(models.Model):
#     name = models.CharField(max_length=20)
#     age = models.PositiveSmallIntegerField()

# class Car(models.Model):
#     model = models.CharField(max_length=20)
#     color = models.CharField(max_length=50)



    # def __str__(self):
    #     return f'name:{self.name}, age:{self.age}'


# object1 = Person.objects.create(name='Lika', age=10)
# print('id:', object1.id)
# print('name:', object1.name)
# print('age:', object1.age)

# object2 = Person(name='Dima', age=4)
# object2.save()

# object3 = Person.objects.get(name='Dima', age=4)
# print(object3.name)
# print(object3.age)

# vika, created = Person.objects.get_or_create(name='Vika', age=15)
# print(vika.name)
# print(vika.age)

# people = Person.objects.all()
# print(people)

# people = Person.objects.filter(name='Lika')
# print(people)

# object1 = Person(name='Lika', age=8)
# object1.save()

# people = Person.objects.filter(name='Lika')
# print(people)

# people = Person.objects.filter(name='Lika', age=10)
# print(people)

# people = Person.objects.exclude(age=10)
# print(people)

# people = Person.objects.filter(name='Lika').exclude(age=10)
# print(people)

# people = Person.objects.in_bulk()
# print(people)
# for id in people:
#     print(people[id].name)
#     print(people[id].age)

# people2 = Person.objects.in_bulk([1, 3, 6])
# print(people2)

# new_user = Person.objects.create(name='Nata', age=20)
# new_user1 = Person(name='Slava', age=30)
# new_user1.save()
# print(Person.objects.all())
# users = Person.objects.all()
# for i in users:
#     print(i)
#     print(i.name, i.age)
# a = []
# for i in users:
#     a.append((i.name, i.age))
# print(a)



# ДЗ
# 1) Витягнути всіх юзерів з іменем Діма з таблиці.

# users = Person.objects.filter(name='Dima')
# print(users)

# 2) Витягнути юзерів в яких вік = 15 а ім'я = Віка

# users = Person.objects.filter(name='Vika', age=15)
# print(users)

# 3) Витягнути 2,3,6 id з таблиці, та вивести їх імена.

# users = Person.objects.in_bulk([2, 3, 6])
# for i in users:
#     print(users[i].name)

# object1 = Person.objects.get(id=1)
# print(object1.name)

# object1.name = 'Lola'
# object1.save()

# object1.name = 'Andrey'
# object1.save(update_fields=['name'])

# Person.objects.filter(id=2).update(age=18)

# Person.objects.filter(id=2).update(age = F('age') + 2)
# Person.objects.all().update(age = F('age') + 10)
# Person.objects.all().update(name = 'Cat')

# object1 = Person.objects.get(id=2)
# object1.name = 'Lika'
# object1.save()

# Person.objects.filter(id=3).update(name = 'Andrey')
# Person.objects.filter(id=4).update(name = 'Dima')

# values_for_update = {'name': 'Max', 'age': 45}
# value_for_update = {'id': '10'}
# object1, created = Person.objects.update_or_create(id=20, defaults=values_for_update)
# object1, created = Person.objects.update_or_create(id=20, defaults=value_for_update)

# object1 = Person.objects.get(id=20)
# object1.id = 21
# object1.save()


# 1) Витягнути з бд поля в яких вік = 30

# field = Person.objects.filter(age=30)
# print(field)
# 2) Замінити в id = 5 ім'я на Василь
# Person.objects.filter(id=5).update(name='Vasiliy')

# 3) Реалізувати для 22-id update or create данних.
# user = {'name': 'Ivan', 'age': 40}
# Person.objects.update_or_create(id=6, defaults=user)

# object = Person.objects.get(id=1)
# object.name = 'Lara'
# object.age = 35
# object.save()
#
# object = Person.objects.get(id=7)
# object.name = 'Pavel'
# object.save(update_fields=['name'])
#
# Person.objects.filter(id=10).update(name='Sveta')

# Person.objects.all().update(age = F('age') + 1)

# a = {'name': 'Yulia', 'age': 1}
# Person.objects.update_or_create(id=1, defaults=a)
# #
# object1 = Person.objects.filter(id=2)
# object1.delete()


# object1 = Car.objects.create(model='Kia', color='red')
# object2 = Car.objects.create(model='Mazda', color=

# Car.objects.filter(pk=2).delete()
# object = Car.objects.all()
# object.delete()

# car = Car.objects.filter(model='Kia')
# print(car.query)

# class Person(models.Model):
#     name = models.CharField(max_length=20)
#     age = models.IntegerField()


# class ListCars(models.Model):
#     brand = models.CharField(max_length=20)
#     age = models.SmallIntegerField()
#     color = models.CharField(max_length=20)

# Связи
# one to many

# class Company(models.Model):
#     name_company = models.CharField(max_length=50)
#     count_persons = models.SmallIntegerField()
#
#
# class Product(models.Model):
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     price = models.FloatField()

# object = Product.objects.get(id=2).company.id
# object = Product.objects.get(id=3).company.name_company

# print(object)
# Product.objects.get(id=1).company.name_company
#
# Product.objects.filter(company__name_company='Apple')

# apple = Company.objects.get(name_company='Apple', count_person=100)

# apple = Company.objects.get(name_company="Apple")
# print(apple)

# получение всех товаров

# apple = Company.objects.filter(name_company="Apple")
# apple.product_set.all()

# получение количества товаров
# apple.product_set.count()

# получение товаров, название которых начинается на "iPhone"
# apple.product_set.filter(name__startwith="iPhone")

# apple = Company.objects.create(name_company='Apple', count_persons=100)
# apple.product_set.create(name='Iphone', price=52.3)

# ipad = Product(name='Ipad', price=14.5)
# apple.product_set.add(ipad, bulk=False)

# ipod = Company.objects.create(name_company='Apple', count_persons=100)
# ipod.product_set.create(name='Ipod', price=35.6)

# mac = Product(name='Mac', price=120.4)
# apple.product_set.add(mac, bulk=False)

# sumsung = Company.objects.create(name_company='Sumsung', count_persons=80)
# galaxy = Product(name='Sumsung Galaxy', price=55.2)
# sumsung.product_set.add(galaxy, bulk=False)

# many to many

# class Course(models.Model):
#     courses_name = models.CharField(max_length=200)
#
# class Students(models.Model):
#     student_name = models.CharField(max_length=50)
#     courses = models.ManyToManyField(Course)

# object1 = Students.objects.create(student_name='Olga')
# object1.courses.create(courses_name='Maths')

# courses_1 = Students.objects.get(id=5).courses.all()
# print(courses_1)

# object2 = Course.objects.create(courses_name='Java Script')
# object2.students_set.create(student_name='Kiril')
#
# student_1 = object2.students_set.all()
# print('все студенты:', student_1)
#
# number = object2.students_set.count()
# print('всего студентов на курсе', number)

# создадим студента
# object1 = Students.objects.create(student_name='Lika')
#
# # создадим один курс и добавим его в список курсов object1
# object1.courses.create(courses_name="Algebra")
#
# # получим все курсы студента
# courses = Students.objects.get(student_name='Lika').courses.all()

# # получаем всех студентов, которые посещают курс Алгебра
# pupils = Students.objects.filter(courses__courses_name="Algebra")

# создадим курс
# ruby = Course.objects.create(courses_name="Ruby")

# # создаем студента и добавляем его на курс
# ruby.students_set.create(student_name="Bob")

# отдельно создаем студента и добавляем его на курс
# sam = Students(student_name="Sam")
# sam.save()
# ruby.students_set.add(sam)
#
# # получим всех студентов курса
# students = ruby.students_set.all()
#
# # получим количество студентов по курсу
# number = ruby.students_set.count()
#
# # удялим с курса одного студента
# ruby.students_set.remove(sam)

# One to one

# class User(models.Model):
#     name = models.CharField(max_length=20)


# class Account(models.Model):
#     login = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

# создадим пользователя
# sam = User.objects.create(name="Sam")
#
# # создадим аккаунт пользователя Sam
# acc = Account.objects.create(login="1234", password="6565", user=sam)
#
# # изменяем имя пользователя
# acc.user.name = "Bob"
# # сохраняем изменения в бд
# acc.user.save()

# создадим пользователя
# tom = User.objects.create(name="Tom")
#
# # создадим аккаунт пользователя
# acc = Account(login="1234", password="6565")
# tom.account = acc
# tom.account.save()

# обновляем данные
# tom.account.login = "qwerty"
# tom.account.password = "123456"
# tom.account.save()


class Users(models.Model):
    name = models.CharField(max_length=20)


class Account(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)
#
# # создадим пользователя
# sam = Users.objects.create(name="Sam")
#
# # создадим аккаунт пользователя Sam
# acc = Account.objects.create(login="1234", password="6565", user=sam)

# создадим пользователя
# bob = Users.objects.create(name="Bob")
# Изменим его имя
# bob = Users.objects.get(id=2)
# bob.name = 'Tom'
# bob.save()


