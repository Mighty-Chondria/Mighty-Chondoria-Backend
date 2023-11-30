from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from django.contrib.auth.hashers import make_password

# Create your models here.

GENDER_CHOICES = (
    ('m', 'male'),
    ('f', 'female')
)


# Create your models here.

class UserAdmin(AbstractUser):
    fname = models.CharField(max_length=18, default='')
    lname = models.CharField(max_length=18, default='')
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthdate = models.DateField(null=True)
    is_subscriped = models.BooleanField(default=False)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username 
