# Generated by Django 2.0.6 on 2018-06-28 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(default=2, editable=False)),
                ('name', models.CharField(default='', max_length=100, verbose_name='名称')),
            ],
            options={
                'verbose_name': '市代',
                'verbose_name_plural': '市代',
            },
        ),
        migrations.CreateModel(
            name='HeadStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(default=0, editable=False)),
                ('name', models.CharField(default='', max_length=100, verbose_name='名称')),
            ],
            options={
                'verbose_name': '总店',
                'verbose_name_plural': '总店',
            },
        ),
        migrations.CreateModel(
            name='LastStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(default=3, editable=False)),
                ('name', models.CharField(default='', max_length=100, verbose_name='名称')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='son', to='organization.CityAgent', verbose_name='所属机构')),
            ],
            options={
                'verbose_name': '门店',
                'verbose_name_plural': '门店',
            },
        ),
        migrations.CreateModel(
            name='ProvinceAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(default=1, editable=False)),
                ('name', models.CharField(default='', max_length=100, verbose_name='名称')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='son', to='organization.HeadStore', verbose_name='所属机构')),
            ],
            options={
                'verbose_name': '省代',
                'verbose_name_plural': '省代',
            },
        ),
        migrations.AddField(
            model_name='cityagent',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='son', to='organization.ProvinceAgent', verbose_name='所属机构'),
        ),
    ]
