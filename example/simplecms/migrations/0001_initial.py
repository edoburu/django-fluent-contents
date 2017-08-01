# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 18:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('_cached_url', models.CharField(blank=True, db_index=True, default='', editable=False, max_length=300)),
                ('template_name', models.CharField(choices=[('theme1/pages/standard.html', 'Standard'), ('theme1/pages/standard-twocols.html', 'Two columns')], default='theme1/pages/standard.html', max_length=255, verbose_name='Layout')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='simplecms.Page')),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
        ),
    ]
