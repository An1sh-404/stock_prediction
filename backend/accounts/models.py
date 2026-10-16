from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db.models.functions import Lower


from .managers import MyAccountManager





class Account(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True)              
	username = models.CharField(max_length=15,
							 unique=True, 
							 validators=[
								 RegexValidator(
									 regex=r'^[a-z0-9_]{4,15}$',
									 message=('Username must contain 4-15 characters and can only include lowercase letters, numbers, and underscores.')
									 )
								])
	
	date_joined = models.DateTimeField(auto_now_add=True)
	is_active = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	email_verified = models.BooleanField(default=False)

	

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username'] # for super users

	objects = MyAccountManager()


	def __str__(self):
		return self.email

	class Meta:
		constraints = [
			models.CheckConstraint(condition= models.Q(username__regex=r'^[a-z0-9_]{4,15}$'), name='username_regex'),
			models.CheckConstraint(condition=models.Q(email=Lower('email')), name='email_lowercase'),
		]