# Generated by Django 3.1.7 on 2021-02-23 21:46

from django.db import migrations, models
import django.db.models.deletion
import person.models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_person_postcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150, verbose_name='Имя')),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150, verbose_name='Имя')),
            ],
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=150, verbose_name='Имя')),
                ('FamilyName', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('Patronymic', models.CharField(max_length=150, verbose_name='Отчество')),
                ('PhoneNumber', models.IntegerField(default=person.models.random_number, verbose_name='Номер телефона')),
                ('PostCode', models.IntegerField(default=person.models.random_postcode, verbose_name='Индекс почты')),
                ('Country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.countries', verbose_name='Страна')),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
