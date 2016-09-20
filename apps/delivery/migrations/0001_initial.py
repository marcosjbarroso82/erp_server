# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 18:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0001_initial'),
        ('employee', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('status', models.IntegerField(choices=[(0, 'canceled'), (1, 'pending'), (3, 'completed')])),
                ('quantity', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeliveryGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('status', models.IntegerField(choices=[(0, 'canceled'), (1, 'pending'), (3, 'completed')])),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='address.Address')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_group', to='order.Order')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('date', models.DateTimeField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='delivery',
            name='distribution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.Distribution'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.DeliveryGroup'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.OrderItem'),
        ),
    ]