# Generated by Django 2.0.6 on 2018-08-14 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_auto_20180814_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='birthday',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='生日'),
        ),
    ]