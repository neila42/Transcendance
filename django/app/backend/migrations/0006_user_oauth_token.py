# Generated by Django 5.0.6 on 2024-06-13 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_user_session_token_expires'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='oauth_token',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
