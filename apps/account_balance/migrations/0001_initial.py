# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 17:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('status', models.IntegerField(choices=[(0, 'canceled'), (1, 'pending'), (2, 'closed')], default=1)),
                ('type', models.IntegerField(choices=[(0, 'output'), (1, 'input')])),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('actor_id', models.PositiveIntegerField()),
                ('actor_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='contenttypes.ContentType')),
                ('balance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account_balance.Balance')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
