from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.



# (RBAC)
    
# ------ Permission ------
class Permission(models.Model):
    name = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.name

# -------- Role ------
class Role(models.Model):
    name = models.CharField(max_length=20,unique=True)
    permissions = models.ManyToManyField(Permission,blank=True,related_name="roles")
    def __str__(self):
        return self.name
# ---------

class User(AbstractUser):
    
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)

    #  links
    roles = models.ManyToManyField(Role, blank=True, related_name="users")
    user_permissions = models.ManyToManyField(
        Permission, blank=True, related_name="users_custom"
    )

    def __str__(self):
        return self.username
