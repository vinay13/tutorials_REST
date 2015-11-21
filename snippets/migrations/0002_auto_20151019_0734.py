# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='language',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='snippet',
            old_name='code',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='linenos',
        ),
    ]
