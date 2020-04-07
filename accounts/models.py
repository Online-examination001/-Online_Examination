from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class AccountManager(BaseUserManager):

    #Function to verify that user actualy gave in a data and not submit empty 
    def valueErrorFunction(self, value):
        if not value:
            raise ValueError(" A unuversity account must have " + value)
    
    def create_user(self,university_name,university_abb,email, password = None):
        # Call Above defined functions
        self.valueErrorFunction(university_name)
        self.valueErrorFunction(university_abb)
        self.valueErrorFunction(email)


        #create a new user

        user = self.model(
            university_name = university_name.upper(),
            university_abb = university_abb.lower(),
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.save(user = self._db)
        return user
        

    def create_superuser(self,username,email, password ):
        # Call Above defined functions
        self.valueErrorFunction(email)

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            password = password,
            is_staff = True,
            is_active = True,
            is_superuser = True,
            is_admin = True
        )
        
        user.save(user = self._db)
        return user
        

class Account(AbstractBaseUser):
    university_name = models.CharField( verbose_name= " University name", max_length=225 , blank=False, null=False )
    university_abb = models.CharField( verbose_name= " University Abbreviation", max_length=20 , blank=False, null=False, unique = True )
    username = models.CharField( verbose_name= " username", max_length=20 ,  unique = True )
    email = models.EmailField(verbose_name = 'Email',  max_length=254, blank = False, null = False , unique = True )
    date_joined = models.DateTimeField(verbose_name = 'Date joined', auto_now_add=True)
    date_login = models.DateTimeField( verbose_name="date login", auto_now=True, )
    is_active = models.BooleanField(default=True)    
    is_admin =models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_super = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['university_name ','university_abb']
    objects = AccountManager()
    def __str__(self):
        return self.university_name

    def has_perm(self,perm, obj=None):
        return self.is_super

    def has_model_perms(self,app_label):
        return True
    

