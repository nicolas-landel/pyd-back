# Generated by Django 5.1.8 on 2025-05-18 10:18

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, null=True)),
                ('updated_at', models.DateTimeField(db_index=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
            ],
            options={
                'ordering': ('-created_at',),
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, null=True)),
                ('updated_at', models.DateTimeField(db_index=True, null=True)),
                ('start_date', models.DateTimeField(verbose_name='Start date')),
                ('end_date', models.DateTimeField(verbose_name='End date')),
                ('name', models.CharField(default='Event', max_length=255, verbose_name='Event name')),
                ('description', models.TextField(blank=True, default='', verbose_name='Comment')),
                ('is_validated', models.BooleanField(default=False, verbose_name='Is validated')),
                ('calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='place.calendar', verbose_name='Calendar')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
            ],
            options={
                'ordering': ('-created_at',),
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, null=True)),
                ('updated_at', models.DateTimeField(db_index=True, null=True)),
                ('name', models.CharField(default='Place', max_length=255, verbose_name='Place')),
                ('address', models.TextField(default='', max_length=255, verbose_name='Address')),
                ('address_comment', models.TextField(blank=True, default='', verbose_name='Address comment')),
                ('zipcode', models.CharField(default='', max_length=5, verbose_name='Zipcode')),
                ('city_name', models.CharField(default='', max_length=50, verbose_name='City name')),
                ('country_name', models.CharField(choices=[('FRANCE', 'FRANCE')], default='FRANCE', max_length=50, verbose_name='Country')),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('description', models.TextField(blank=True, default='', verbose_name='Description')),
                ('max_capacity', models.IntegerField(blank=True, null=True)),
                ('double_beds', models.IntegerField(blank=True, null=True)),
                ('simple_beds', models.IntegerField(blank=True, null=True)),
                ('rooms', models.IntegerField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
            ],
            options={
                'ordering': ('-created_at',),
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='calendar',
            name='place',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='calendar', to='place.place', verbose_name='Place'),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, null=True)),
                ('updated_at', models.DateTimeField(db_index=True, null=True)),
                ('name', models.CharField(default='Tag', max_length=255, verbose_name='Tag name')),
                ('description', models.TextField(blank=True, default='', verbose_name='Tag description')),
                ('calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='place.calendar', verbose_name='Calendar')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
            ],
            options={
                'ordering': ('-created_at',),
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventTags',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, null=True)),
                ('updated_at', models.DateTimeField(db_index=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_tags', to='place.event', verbose_name='Event')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_tags', to='place.tag', verbose_name='Tag')),
            ],
            options={
                'ordering': ('-created_at',),
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='events', through='place.EventTags', to='place.tag', verbose_name='Event tags'),
        ),
    ]
