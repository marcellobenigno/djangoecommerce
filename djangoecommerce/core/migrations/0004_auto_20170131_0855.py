# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 11:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['name'], 'verbose_name': 'contato', 'verbose_name_plural': 'contatos'},
        ),
    ]
