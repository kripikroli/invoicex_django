# Generated by Django 3.1.7 on 2021-04-08 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='bank_account',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
