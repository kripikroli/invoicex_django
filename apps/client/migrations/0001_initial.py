# Generated by Django 3.1.7 on 2021-04-03 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('company_number', models.CharField(blank=True, max_length=255, null=True)),
                ('address_line_1', models.CharField(blank=True, max_length=255, null=True)),
                ('address_line_2', models.CharField(blank=True, max_length=255, null=True)),
                ('city_name', models.CharField(blank=True, max_length=50, null=True)),
                ('state_name', models.CharField(blank=True, max_length=50, null=True)),
                ('country_name', models.CharField(blank=True, max_length=50, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=20, null=True)),
                ('contact_person', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_reference', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
