# Generated by Django 4.1.5 on 2023-01-05 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='is_read',
            field=models.BooleanField(default=False, verbose_name='Прочитан'),
        ),
    ]
