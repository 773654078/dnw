# Generated by Django 2.0.6 on 2018-08-03 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_customer3_customer4_customer5'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='hospital',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='医院'),
        ),
        migrations.AddField(
            model_name='customer',
            name='order_num',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='预约号'),
        ),
        migrations.AddField(
            model_name='customer',
            name='qq_num',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='QQ号码'),
        ),
        migrations.AddField(
            model_name='customer',
            name='register_date',
            field=models.DateField(blank=True, null=True, verbose_name='登记时间'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.IntegerField(choices=[(0, '未到店'), (1, '已到店'), (2, '新单'), (3, '已完成')], default=0, verbose_name='赴约状态'),
        ),
    ]
