# Generated by Django 4.0.6 on 2022-07-24 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
    ]