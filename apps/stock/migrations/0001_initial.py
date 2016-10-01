# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 17:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('item_resource', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IOItemResourceStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('quantity', models.IntegerField(default=0)),
                ('note', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IOProductStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('quantity', models.IntegerField(default=0)),
                ('note', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ItemResourceStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=0)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='item_resource.ItemResource')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=0)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='product.ProductVariant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='ioproductstock',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='stock.ProductStock'),
        ),
        migrations.AddField(
            model_name='ioitemresourcestock',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='stock.ItemResourceStock'),
        ),
    ]
