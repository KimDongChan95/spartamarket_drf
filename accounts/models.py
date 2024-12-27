from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",  # 기본 User와 충돌 방지를 위해 변경
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_user_permissions",  # 기본 User와 충돌 방지를 위해 변경
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
