# Generated by Django 2.0.6 on 2018-08-15 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_auto_20180816_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='channel',
            field=models.IntegerField(blank=True, choices=[(0, '抖音'), (1, '微博'), (2, '团购')], default=0, null=True, verbose_name='渠道'),
        ),
    ]
