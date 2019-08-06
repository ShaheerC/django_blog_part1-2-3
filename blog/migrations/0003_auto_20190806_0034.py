# Generated by Django 2.2.3 on 2019-08-06 00:34

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(null=True, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='article',
            name='draft',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]