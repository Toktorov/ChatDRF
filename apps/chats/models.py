from django.db import models
from apps.users.models import User

# Create your models here.
class Chat(models.Model):
    from_chat_user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = "from_user_chat",
        verbose_name = "Чат от пользователя"
    )
    to_chat_user = models.ForeignKey(
        User, 
        on_delete = models.CASCADE,
        related_name = "to_user_chat",
        verbose_name = "Чат к пользователю"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.id} -- {self.from_chat_user} -- {self.to_chat_user} -- {self.created_at}"

    class Meta:
        verbose_name = "Чат"
        verbose_name_plural = "Чаты"

class Message(models.Model):
    chat = models.ForeignKey(
        Chat, 
        on_delete = models.CASCADE,
        related_name = 'messages_chat',
        verbose_name = "ID чата"
    )
    from_user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = "chat_from_user",
        verbose_name = "Сообщение от пользователя"
    )
    to_user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = "chat_to_user",
        verbose_name = "Сообщение к пользователю"
    )
    message = models.CharField(
        max_length = 255,
        verbose_name = "Сообщение"
    )
    is_read = models.BooleanField(
        default=False,
        verbose_name="Прочитан"
    )
    created_at = models.TimeField(
        auto_now_add = True
    )

    def __str__(self):
        return f"{self.chat}"

    class Meta:
        verbose_name = "Сообщение в чате"
        verbose_name_plural = "Сообщение в чатах"