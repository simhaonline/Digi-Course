# Generated by Django 3.1 on 2020-08-27 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20200822_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
