# Generated by Django 5.0.6 on 2024-06-12 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_user_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='session_token_expires',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
