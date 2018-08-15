# Generated by Django 2.0.6 on 2018-08-14 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_auto_20180814_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='sex',
            field=models.IntegerField(blank=True, choices=[(0, '男'), (1, '女')], default='', verbose_name='性别'),
        ),
    ]
