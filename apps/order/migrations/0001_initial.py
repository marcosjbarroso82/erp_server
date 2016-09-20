# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 18:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('status', models.IntegerField(choices=[(0, 'canceled'), (1, 'pending'), (3, 'completed'), (4, 'delivered'), (5, 'paid')])),
                ('total', models.DecimalField(decimal_places=2, editable=False, max_digits=12)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='client.Client')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('quantity', models.PositiveIntegerField()),
                ('product_name', models.CharField(editable=False, max_length=20)),
                ('price', models.DecimalField(decimal_places=2, editable=False, max_digits=12)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='order.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
