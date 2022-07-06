# Типы полей
# Все поля наследуются от models импортируются из from django.db import models

# field1 = models.BinaryField() - хранит бинарные файлы
# field2 = models.BooleanField() - хранит 0,1, или True, False
# field3 = models.NullBooleanField(null=True) - хранит хранит 0,1, или True, False, Null
# field4 = models.DateField() - хранит дату
# field5 = models.TimeField() - хранит время
# field6 = models.DateTimeField() - хранит дату и время
# field7 = models.DurationField() - хранит интервал времени(указывается дата и время)
# field8 = models.AutoField() - хранит числа которые генерируются автоматически, используются для ключей
# field9 = models.BigIntegerField() - хранит числа в интервале -9223372036854775808 до 9223372036854775807
# field10 = models.FloatField() - хранит числа с плавающей точкой
# field11 = models.IntegerField() - хранит числа в интервале - -2147483648 до 2147483647
# field12 = models.PositiveIntegerField() - хранит числа в интервале - от 0 до 2147483647+-
# field13 = models.PositiveSmallIntegerField() - хранит числа в интервале - от 0 до 32767+-
# field14 = models.SmallIntegerField() - хранит числа в интервале - от -32768 до 32767 +-
# field15 = models.CharField(max_length=20) - хранит текст, обязательно указывать кол-во символов
# field16 = models.TextField() - хранит текс, кол-во символов можно не указывать
# field17 = models.EmailField() - хранит емаил, имеет встроенную проверку на валидность
# field18 = models.FileField() - хранит название файла
# field19 = models.FilePathField() - хранит путь к файлу
# field20 = models.ImageField() - хранит название изображения
# field21 = models.GenericIPAddressField() - хранит IP адрес в формате IPV4 и IPV6
# field22 = models.SlugField() - хранит текс в нижнем регистре цифры от 1 до 9 и знак '_'
# field23 = models.URLField() - хранит url


# Створити app cars
# Розробити таблиці:
# 1) cars (brand, model, age, color, email_company)
# 2) dealer(brand, email_dealer, image_dealer, description)
# 3) buyer(name, lastname, email, phone, rating)