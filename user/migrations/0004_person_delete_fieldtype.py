# Generated by Django 4.0.6 on 2022-07-06 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_fieldtype_delete_person_delete_useradmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='FieldType',
        ),
    ]