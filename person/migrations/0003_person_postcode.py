# Generated by Django 3.1.7 on 2021-02-22 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_person_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='PostCode',
            field=models.IntegerField(default=720001, verbose_name='Индекс почты'),
        ),
    ]
