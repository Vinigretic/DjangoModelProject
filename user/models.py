from django.db import models

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

class FieldType(models.Model):
    field1 = models.BinaryField()
    field2 = models.BooleanField()
    # field3 = models.NullBooleanField(null=True)
    field4 = models.DateField()
    field5 = models.TimeField()
    field6 = models.DateTimeField()
    field7 = models.DurationField()
    # field8 = models.AutoField()
    field9 = models.BigIntegerField()
    field10 = models.FloatField()
    field11 = models.IntegerField()
    field12 = models.PositiveIntegerField()
    field13 = models.PositiveSmallIntegerField()
    field14 = models.SmallIntegerField()
    field15 = models.CharField(max_length=20)
    field16 = models.TextField()
    field17 = models.EmailField()
    field18 = models.FileField()
    field19 = models.FilePathField()
    # field20 = models.ImageField()
    field21 = models.GenericIPAddressField()
    field22 = models.SlugField()
    field23 = models.URLField()


