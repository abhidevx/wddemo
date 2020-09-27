# imports
from django.db import models
import uuid 
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinLengthValidator,EmailValidator
# Create your models here.

# Customer Profile Model.
class Profile(models.Model):
    bio = models.CharField(max_length=255, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    git_profile_link = models.URLField(null=True, blank=True)

# Customer Model.
class Customer(models.Model):
    id = models.UUIDField( primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length=255, validators=[MinLengthValidator(1)], null=False, blank=False)   
    slug = models.SlugField(allow_unicode=True, null=True ,blank=True)
    email = models.EmailField(null=False,default=None, blank=False, validators=[EmailValidator])
    phone = PhoneNumberField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField( blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, db_constraint=False, null=True, blank=True)

    def __str__(self):
        return self.name



         
    
   


