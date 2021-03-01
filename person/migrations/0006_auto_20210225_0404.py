# Generated by Django 3.1.7 on 2021-02-24 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0005_auto_20210224_0349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150, verbose_name='Название страны')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.AlterField(
            model_name='person',
            name='Patronymic',
            field=models.CharField(default='Не указано', max_length=150, verbose_name='Отчество'),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150, verbose_name='Название города')),
                ('Countries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.country')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='Cities',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='person.city', verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='person',
            name='Countries',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='person.country', verbose_name='Страна'),
        ),
    ]