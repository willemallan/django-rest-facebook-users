# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('facebook_id', models.SlugField(unique=True, max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=100)),
                ('inserted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('inserted',),
            },
            bases=(models.Model,),
        ),
    ]
