from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, email, password = None):
        if not email:
            raise ValueError("Account must have an email")

        user = self.model(
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using = self._db)
        return user


    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password= password
        )
        user.is_staff = True
        user.is_admin = True
        user.is_super = True

        user.save(using = self.db)
        return user






class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name = "Email", max_length=254,unique = True )
    username = models.CharField(verbose_name="Username", max_length = 255, unique= True )
    date_joined = models.DateTimeField(verbose_name = 'Date joined', auto_now_add=True)
    date_login = models.DateTimeField( verbose_name="date login", auto_now=True, )
    is_active = models.BooleanField(default=True)
    is_admin =models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_super = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = AccountManager()

    def __str__(self):
        return self.email


    def has_perms(self,perm, obj=None):
        return self.is_super

    def has_module_perms(self,app_label):
        return self.is_super