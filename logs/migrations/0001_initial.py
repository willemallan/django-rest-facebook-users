# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('function', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('level', models.CharField(max_length=255, choices=[(b'DEBUG', b'DEBUG'), (b'INFO', b'INFO'), (b'WARNING', b'WARNING'), (b'ERROR', b'ERROR'), (b'CRITICAL', b'CRITICAL')])),
                ('create', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Log',
                'verbose_name_plural': 'Logs',
            },
            bases=(models.Model,),
        ),
    ]
