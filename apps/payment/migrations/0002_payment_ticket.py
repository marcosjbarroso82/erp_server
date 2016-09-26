# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 18:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_balance', '0003_auto_20160926_1809'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='ticket',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='account_balance.Ticket'),
        ),
    ]
