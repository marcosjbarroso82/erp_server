# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 18:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_auto_20160922_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='distribution',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='status',
        ),
        migrations.AddField(
            model_name='deliverygroup',
            name='distribution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.Distribution'),
        ),
        migrations.AlterField(
            model_name='deliverygroup',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='address.Address'),
        ),
        migrations.AlterField(
            model_name='deliverygroup',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_groups', to='order.Order'),
        ),
        migrations.AlterField(
            model_name='deliverygroup',
            name='status',
            field=models.IntegerField(choices=[(0, 'canceled'), (1, 'pending'), (2, 'completed')], default=1),
        ),
    ]