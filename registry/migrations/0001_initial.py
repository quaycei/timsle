# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 00:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=None, max_length=140)),
                ('last_name', models.CharField(default=None, max_length=140)),
                ('office', models.CharField(blank=True, default=None, max_length=140, null=True)),
                ('address_line_1', models.CharField(blank=True, default=None, max_length=140, null=True)),
                ('address_line_2', models.CharField(blank=True, default=None, max_length=140, null=True)),
                ('city', models.CharField(blank=True, default=None, max_length=140, null=True)),
                ('state_province_region', models.CharField(blank=True, default=None, max_length=140, null=True)),
                ('zip_postal_code', models.CharField(blank=True, default=None, max_length=140, null=True)),
                ('country', models.CharField(blank=True, default=None, max_length=140, null=True)),
                ('website', models.CharField(blank=True, default=None, max_length=140, null=True)),
                ('phone_number', models.CharField(blank=True, default=None, max_length=140, null=True)),
                ('email_address', models.CharField(default=None, max_length=140)),
                ('contact_note', models.TextField(blank=True, default=None, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('verification', models.IntegerField(choices=[(0, 'Pending'), (1, 'Verified'), (2, 'Flagged'), (3, 'Declined')], default=0)),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Online'), (2, 'Offline'), (3, 'Removed')], default=0)),
                ('name', models.CharField(max_length=50)),
                ('mission', models.TextField(default=None, max_length=250)),
                ('creator', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='registry',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='registry.Registry'),
        ),
    ]