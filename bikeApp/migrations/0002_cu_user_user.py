# Generated by Django 3.2 on 2022-11-07 04:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bikeApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cu_user',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
