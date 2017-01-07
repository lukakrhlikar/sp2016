# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 21:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poraba_app', '0005_auto_20170104_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model_avto',
            name='znamka',
        ),
        migrations.RemoveField(
            model_name='avtomobil',
            name='ime_modela',
        ),
        migrations.AddField(
            model_name='poraba',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='avtomobil',
            name='tip_goriva',
            field=models.CharField(default='Bencin 95', max_length=45),
        ),
        migrations.AlterField(
            model_name='avtomobil',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Model_avto',
        ),
        migrations.DeleteModel(
            name='Znamka',
        ),
    ]
