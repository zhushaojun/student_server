from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    DEPARTMENT_CHOICES = (
        ('部门1', '部门1'),
        ('部门2', '部门2'),
        ('部门3', '部门3'),
        ('部门4', '部门4'),
        ('部门5', '部门5'),
        ('部门6', '部门6'),
        ('部门7', '部门7'),
    )
    department = models.CharField(_('所属部门'),
                                  max_length=16,
                                  choices=DEPARTMENT_CHOICES,
                                  default='部门1',
                                  )
    email = models.EmailField(_('电子邮箱'), unique=True)
    name = models.CharField(_('姓名'), max_length=30, blank=True)
    is_staff = models.BooleanField(_('是否管理员'), default=False)
    is_active = models.BooleanField(_('是否激活'), default=False)
    date_joined = models.DateTimeField(_('创建日期'), default=timezone.now)
    phone = models.CharField(_('手机号'), max_length=11, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["email"]
        verbose_name_plural = "用户"
        verbose_name = "用户"
