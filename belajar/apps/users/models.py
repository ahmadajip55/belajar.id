from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, 
                                        BaseUserManager)
from django.db import models
from django.utils import timezone
from model_utils import Choices

class UserManager(BaseUserManager):

    def create_user(self, username=None, email = None, creation_method = 1, registration_method = None, password = None, is_active = True,
                    address = '', phone = None, **extra_fields):

        now = timezone.now()
        if not username and not email and not phone:
            raise ValueError("Username or Email or mobile phone is required")

        if email:
            email = email.lower()

        if username:
            username = username.lower()

        user = self.model(username=username, email=email, phone=phone, is_active=is_active, is_superuser=False,
                          is_staff=False, last_login=now, date_joined=now, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password, **extra_fields):
        user = self.create_user(username=username, password=password, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE = Choices(
        (1, 'mentee', 'Mentee'),
        (2, 'mentor', 'Mentor'),
    )
    username = models.CharField(verbose_name='Username', max_length=255, unique=True)
    full_name = models.CharField(verbose_name='Full Name', max_length=255, blank=True, null=True)
    email = models.EmailField(verbose_name='Email Address', unique=True, max_length=254)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE, blank=True, null=True)
    is_active = models.BooleanField(
        'active',
        default=True,
        help_text='Designates whether this user should be treated as '
                  'active. Unselect this instead of deleting accounts.'
    )
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Whether the user can log into this admin site.'
    )
    date_joined = models.DateTimeField('date joined', default=timezone.now)
    phone = models.CharField(verbose_name='Mobile Number', max_length=30, blank=True, null=True, default=None, unique=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
