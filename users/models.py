from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class UserRoles(models.TextChoices):
        USR = 'user'
        MOD = 'moderator'
        ADM = 'admin'

    bio = models.TextField(
        null=True,
        max_length=1000,
        verbose_name='Описание')
    role = models.CharField(
        max_length=15,
        choices=UserRoles.choices,
        default=UserRoles.USR,
        verbose_name='Уровень доступа'
    )
    confirmation_code = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Код подтверждения',
    )

    @property
    def is_user(self):
        return self.role == self.UserRoles.USR

    @property
    def is_moderator(self):
        return self.role == self.UserRoles.MOD

    @property
    def is_admin(self):
        return self.role == self.UserRoles.ADM or self.is_superuser

    class Meta:
        ordering = ['username']
