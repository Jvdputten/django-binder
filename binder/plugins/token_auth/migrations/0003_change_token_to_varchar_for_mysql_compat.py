# Generated by Django 2.2 on 2019-04-25 09:18

import binder.plugins.token_auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('token_auth', '0002_add_related_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(default=binder.plugins.token_auth.models.generate_token, max_length=32, unique=True),
        ),
    ]
