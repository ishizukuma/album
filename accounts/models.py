from django.db import models
from django.contrib.auth.models import (BaseUserManager,
                                        AbstractBaseUser,
                                        PermissionsMixin)
from django.utils.translation import gettext_lazy as _

USER_TYPE_CHOICES = [
    (0, 'admin'),
    (1, 'student'),
    (2, 'teacher'),
]



class UserManager(BaseUserManager):
    def _create_user(self, email, username, password, user_type=1 or 2, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email,username=username, user_type=user_type, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, username, password=None, user_type=1 or 2, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            email=email,
            username=username,
            password=password,
            user_type=user_type,
            **extra_fields,
        )
    

    def create_superuser(self, email, username, password, user_type=0, **extra_fields):
        extra_fields['is_active'] = True
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        return self._create_user(
            email=email,
            username=username,
            password=password,
            user_type=user_type,
            **extra_fields,
        )


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        verbose_name=_("email"),
        unique=True
    )
    
    username = models.CharField(
        verbose_name=_("username"),
        max_length=150,
        null=True,
        blank=False
    )
    
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES, default=1)
    is_superuser = models.BooleanField(
        verbose_name=_("is_superuer"),
        default=False
    )

    
    is_superuser = models.BooleanField(
        verbose_name=_("is_superuer"),
        default=False
    )
    is_staff = models.BooleanField(
        verbose_name=_('staff status'),
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_("created_at"),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_("updateded_at"),
        auto_now=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email' # ログイン時、ユーザー名の代わりにemailを使用
    REQUIRED_FIELDS = ['username']  # スーパーユーザー作成時にusernameも設定する

    def __str__(self):
        return self.username

