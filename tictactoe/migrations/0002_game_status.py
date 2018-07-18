# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.CharField(max_length=1, default=True, choices=[('A', 'Active'), ('F', 'First PLayer Wins'), ('S', 'Second Player Wins'), ('D', 'Draw')]),
        ),
    ]
