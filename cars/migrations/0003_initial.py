# Generated by Django 4.0.6 on 2022-07-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0002_delete_buyer_delete_cars_delete_dealer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('email_dealer', models.EmailField(max_length=254)),
                ('image_dealer', models.FilePathField()),
                ('description', models.TextField()),
            ],
        ),
    ]
