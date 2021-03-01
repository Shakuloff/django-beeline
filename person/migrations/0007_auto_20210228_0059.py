# Generated by Django 3.1.7 on 2021-02-27 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0006_auto_20210225_0404'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Персона', 'verbose_name_plural': 'Персоны'},
        ),
        migrations.AddField(
            model_name='person',
            name='Job',
            field=models.CharField(default='Неизвестно', max_length=150, verbose_name='Работа'),
        ),
        migrations.AddField(
            model_name='person',
            name='Salary',
            field=models.IntegerField(default=40000, verbose_name='Зарплата'),
        ),
    ]
