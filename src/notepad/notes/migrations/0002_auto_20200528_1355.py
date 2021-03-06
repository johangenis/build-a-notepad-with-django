# Generated by Django 3.0.5 on 2020-05-28 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 28, 13, 54, 33, 984605)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='label',
            field=models.CharField(choices=[('R', 'primary'), ('SE', 'secondary'), ('S', 'success'), ('D', 'danger'), ('W', 'warning'), ('I', 'info'), ('L', 'light'), ('D', 'dark')], default='P', max_length=2),
            preserve_default=False,
        ),
    ]
