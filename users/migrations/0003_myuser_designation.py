# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_userdesignation'),
        ('users', '0002_auto_20161215_0526'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='designation',
            field=models.ForeignKey(db_column=b'designation', blank=True, to='settings.UserDesignation', null=True),
        ),
    ]
