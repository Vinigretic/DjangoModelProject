# Generated by Django 4.0.6 on 2022-07-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_company_product_delete_listcars'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('courses', models.ManyToManyField(to='user.course')),
            ],
        ),
    ]