# Generated by Django 2.0.1 on 2018-01-23 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscourseGroup',
            fields=[
                ('role_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
        ),
    ]