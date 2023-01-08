# Generated by Django 4.1.5 on 2023-01-08 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0005_rename_created_chat_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_chat', to='chats.chat', verbose_name='ID сообщения'),
        ),
    ]
