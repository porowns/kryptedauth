# Generated by Django 2.0.1 on 2018-01-12 05:10

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
            name='EveCharacter',
            fields=[
                ('character_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('character_portrait', models.URLField(blank=True, max_length=255, null=True)),
                ('main', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eveonline.EveCharacter')),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_id', models.IntegerField(blank=True, null=True)),
                ('character_owner_hash', models.CharField(max_length=255)),
                ('character_name', models.CharField(max_length=255)),
                ('access_token', models.CharField(max_length=255)),
                ('refresh_token', models.TextField(blank=True, null=True)),
                ('expires_in', models.IntegerField(default=0)),
                ('expiry', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='evecharacter',
            name='token',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='eveonline.Token'),
        ),
        migrations.AddField(
            model_name='evecharacter',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
