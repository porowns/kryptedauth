# Generated by Django 2.1.4 on 2018-12-29 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_auto_20181229_2057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventlog',
            old_name='date',
            new_name='datetime',
        ),
        migrations.RenameField(
            model_name='guildlog',
            old_name='date',
            new_name='datetime',
        ),
    ]