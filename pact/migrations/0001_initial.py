# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 20:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('circle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buddy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=200)),
                ('status', models.IntegerField(choices=[(1, 'Pending'), (2, 'Yes'), (3, 'No'), (4, 'Ignore Request')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Checkin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=140)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200)),
                ('goal', models.IntegerField(blank=True, default=5)),
                ('motivation', models.TextField(default=None)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Completed'), (3, 'Archived')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='circle.Content')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='checkin',
            name='pact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pact.Pact'),
        ),
        migrations.AddField(
            model_name='checkin',
            name='submitted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='buddy',
            name='pact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pact.Pact'),
        ),
        migrations.AddField(
            model_name='buddy',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
