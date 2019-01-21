# Generated by Django 2.1.4 on 2018-12-30 03:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_user_secret'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('date_created', models.DateField(auto_now=True)),
                ('date_finished', models.DateField()),
                ('url', models.CharField(max_length=256)),
                ('survey_key', models.UUIDField(default=uuid.uuid4)),
                ('guild', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Guild')),
                ('users_completed', models.ManyToManyField(blank=True, related_name='_survey_users_completed_+', to=settings.AUTH_USER_MODEL)),
                ('users_started', models.ManyToManyField(blank=True, related_name='_survey_users_started_+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]