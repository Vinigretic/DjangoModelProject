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