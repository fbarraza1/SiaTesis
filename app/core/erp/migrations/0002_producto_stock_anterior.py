# Generated by Django 4.2.6 on 2023-10-24 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='stock_anterior',
            field=models.IntegerField(default=0),
        ),
    ]
