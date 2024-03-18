from django.db import models
from django.contrib.auth.models import AbstractUser ,BaseUserManager

GENDER = (
    ('male','male'),
    ('female','female'),
    ('perfer not to say','perfer not to say')
)

VERIFY = (
    ('pending','pending'),
    ('verified','verified')
)


class MyManager(BaseUserManager):
    def create_user(self,email,password=None,**kwargs):
        if not email:
            raise ValueError('email cant`t be none')
        user = self.create(
            email=self.normalize_email(email),
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password,**kwargs):
        user = self.create_user(
            email = email,
            password=password,
            **kwargs
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser =True
        user.is_verified = True
        user.save(using=self._db)
        return user
class User(AbstractUser):
    email = models.EmailField(unique=True,max_length=225)
    username = models.CharField(max_length=225,unique=True)
    phone_number = models.IntegerField(null=True,blank=True)
    gender = models.CharField(choices=GENDER,max_length=100)
    profile_picture = models.ImageField(upload_to='profile',default='profile.jpg')
    objects = MyManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    def __str__(self)->str:
        return f'{self.email}'