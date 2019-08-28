# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-20 09:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import picklefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeferredAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=40)),
                ('valid_until', models.DateTimeField(null=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('declined', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('form_class', models.CharField(max_length=255)),
                ('form_input', picklefield.fields.PickledObjectField(editable=False)),
                ('form_prefix', models.CharField(blank=True, max_length=255, null=True)),
                ('object_pk', models.TextField(null=True)),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('requested_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requested_by', to=settings.AUTH_USER_MODEL)),
                ('reviewed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewed_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
