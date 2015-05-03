# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=160)),
                ('deadline', models.DateTimeField(verbose_name='Deadline')),
                ('progress', models.DecimalField(decimal_places=0, max_digits=3)),
            ],
        ),
    ]
