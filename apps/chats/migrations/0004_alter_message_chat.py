# Generated by Django 4.1.5 on 2023-01-05 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_remove_chat_is_read_message_is_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_chat_id', to='chats.chat', verbose_name='ID сообщения'),
        ),
    ]