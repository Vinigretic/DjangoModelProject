# CRUD. операции с моделями

# Четыре основных операции
#
# 1. Create
# 2. Read
# 3. Update
# 4. Delete

# Операция create

# Для того что бы создать информацию которая отправится в БД используется CRUD операция create
# Простой пример:

# class Person(models.Model):
#     name = models.CharField(max_length=20)
#     age = models.PositiveSmallIntegerField()


# Вариан 1
# object1 = Person.objects.create(name='Lika', age=10)

# objects - это обращение ко всем обьектам класса
# create - это создание данных в БД(метод save() уже встроен)

# Вариант 2
# Можно создавать данные по принципу ООП, но необходимо использовать метод save()

# object2 = Person(name='Dima', age=4)
# object2.save()


# Для того что бы вывести в консоль данные при написании логики проекта, используем функцию print и запускаем весь
# проект

# Операция read

# Для того что бы получить данные из БД используем метод get()

# object3 = Person.objects.get(name='Dima')

# Метод get применяем только в том случае когда знаем что в БД существует запрашиваемые данные и информация
# находится в одном экземпляре. Так как если таких данных нет метод выдаст ошибку(user.models.DoesNotExist:) и если
# данных больше одного экземпляра тоже выдаст ошибку(user.models.MultipleObjectsReturned)

# Если мы не уверены что данные в БД существуют используем метод get_or_create()

# vika, created = Person.objects.get_or_create(name='Vika', age=15)

# Метод get_or_create() - если запрашиваемых данных нет он их создаст, если есть в одном экземпляре отработает как
# метод get, если данных больше одного экземпляра выдаст ошибку(user.models.MultipleObjectsReturned)

# При использовании этого метода необходимо создавать две переменные
# vika, created - первая переменная будет обьектом класса, вторая переменая будет принемать булево значение
# True если данных нет и созданы новые, False если запрашиваемые данные уже есть

# Для того что бы получить доступ ко всем данным таблицы из БД используем метод all()
#
# people = Person.objects.all()
#
# Данные будут выводится в ввиде queryset, их нужно дополнительно обрабатывать для дальнейшего использования
#
# <QuerySet [<Person: Person object (1)>, <Person: Person object (2)>, <Person: Person object (3)>, <Person: Person object (4)>, <Person: Person object (5)>, <Person: P
# erson object (6)>]>

# Для того что бы получить определенные данные используем метод filter()
#
# people = Person.objects.filter(name='Lika', age=10)
#
# Метод filter - в качестве параметров передаем необходимые значения по которым хотим осуществить фильтр.
# Параметров может быть сколько угодно

# Если нам необходимо исключить какие то данные из выборки применяем метод еxclude

# people = Person.objects.exclude(age=10)

# В качестве параметров передаем значения которые нужно исключить из выборки

# Методы filter и exclude можно комбинировать

# people = Person.objects.filter(name='Lika').exclude(age=10)

# Если необходимо получить данные в виде словаря используем метод in_bulk

# people = Person.objects.in_bulk()

# Вывод данных

# {1: <Person: Person object (1)>, 2: <Person: Person object (2)>, 3: <Person: Person object (3)>, 4: <Person: Person object (4)>, 5: <Person: Person object (5)>, 6: <P
# erson: Person object (6)>}


# Извлекаем данные из словаря
# for id in people:
#     print(people[id].name)
#     print(people[id].age)

# Этот метод позваляет указывать индексы данных(id из БД) которые мы хотим получить
#
# people2 = Person.objects.in_bulk([1, 3, 6])