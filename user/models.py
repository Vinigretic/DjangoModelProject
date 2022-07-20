from django.db import models
from django.db.models import F


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


class ListCars(models.Model):
    brand = models.CharField(max_length=20)
    age = models.SmallIntegerField()
    color = models.CharField(max_length=20)