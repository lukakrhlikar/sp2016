# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 15:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Avtomobil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=200)),
                ('tip_goriva', models.CharField(choices=[('B', 'Bencin'), ('D', 'Diezel'), ('E', 'Elektrika')], default='B', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Model_avto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_avto', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Poraba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poraba', models.DecimalField(decimal_places=1, max_digits=4)),
                ('avto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poraba_app.Avtomobil')),
            ],
        ),
        migrations.CreateModel(
            name='User2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strosek', models.DecimalField(decimal_places=2, max_digits=7)),
                ('tip_voznika', models.CharField(choices=[('P', 'Povprečen'), ('N', 'Nedeljski'), ('E', 'Eko'), ('T', 'Voznik s težko nogo')], default='P', max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Znamka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('znamka', models.CharField(max_length=45)),
            ],
        ),
        migrations.AddField(
            model_name='model_avto',
            name='znamka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poraba_app.Znamka'),
        ),
        migrations.AddField(
            model_name='avtomobil',
            name='ime_modela',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poraba_app.Model_avto'),
        ),
        migrations.AddField(
            model_name='avtomobil',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='poraba_app.User2'),
        ),
    ]
