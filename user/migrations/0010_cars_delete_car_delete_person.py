# Generated by Django 4.0.6 on 2022-07-18 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('car_age', models.SmallIntegerField()),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
