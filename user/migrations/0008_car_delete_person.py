# Generated by Django 4.0.6 on 2022-07-15 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_person_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
