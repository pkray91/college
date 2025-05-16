from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


class Basemodel(models.Model):
    auto_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50,null=True,blank=True,editable=False)
    updated_by = models.CharField(max_length=50,null=True,blank=True,editable=False)
    
    class Meta:
        abstract = True

class Aboutus(Basemodel):
    title = models.CharField(max_length=50,null=True,blank=True)
    about_images = models.ImageField(upload_to='media/')
    description = models.CharField(max_length=50,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        db_table="aboutus"


    def __str__(self):
        return self.title
    
class Ourteam(Basemodel):
    title = models.CharField(max_length=50,null=True,blank=True)
    ourteam_images = models.FileField(upload_to='media/')
    description = models.CharField(max_length=50,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        db_table="our_teams"

    def __str__(self):
        return self.title
class Coureses(Basemodel):
    title = models.CharField(max_length=50,null=True,blank=True)
    semester = models.CharField(max_length=50,null=True,blank=True)
    coureses_images = models.FileField(upload_to='media/')
    description = models.CharField(max_length=50,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        db_table="courses"

    def __str__(self):
        return self.title
    
    

USER_TYPES = (
    ("1", "Principal"),
    ("2", "Hod"),
    ("3", "Staff"),
    ("4", "Teacher"),
    ("5", "Student"),
    ("6", "Account"),   
)
class UserCustomManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self,password,phone_number=None, **extra_fields):
        # if not phone_number:
        #     raise ValueError('provide phonenumber')
        
        email = extra_fields['email']
        user = self.model(phone_number=phone_number, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(password, **extra_fields)
    
    
class User(AbstractUser):
    # You have to remove 'username' and 'password'!
    # username = None
    # password = None
    email = models.EmailField(null=True, blank=True,unique=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    phone_number = models.BigIntegerField(null=True, blank=True,unique=True)
    user_type = models.CharField(max_length=40, choices=USER_TYPES)
    data_join = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    # You must remove the 'phone_number' from REQUIRED_FIELDS!
    # Here you can't repeat in the REQUIRED_FIELDS the same field that you put in USERNAME_FIELD, you can add other: 'email', etc ...
    REQUIRED_FIELDS = []
    

    objects = UserCustomManager()
    
    def __str__(self):
        return self.first_name+' '+self.last_name+' '+self.email
 
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    
