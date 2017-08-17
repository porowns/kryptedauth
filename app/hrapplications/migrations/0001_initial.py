# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 14:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eveonline', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[(b'Approved', b'Approved'), (b'Pending', b'Pending'), (b'Processing', b'Processing'), (b'Rejected', b'Rejected'), (b'On Hold', b'On Hold')], default=b'Processing', max_length=24)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('processed_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('help_text', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EveApplication',
            fields=[
                ('application_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hrapplications.Application')),
                ('main_character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_character', to='eveonline.EveCharacter')),
            ],
            bases=('hrapplications.application',),
        ),
        migrations.AddField(
            model_name='application',
            name='guild',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guild', to='core.Guild'),
        ),
        migrations.AddField(
            model_name='application',
            name='questions',
            field=models.ManyToManyField(related_name='application_questions', to='hrapplications.Question'),
        ),
        migrations.AddField(
            model_name='application',
            name='reviewer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='application',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
