from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField('Is admin',default=False)
    is_student = models.BooleanField('Is student',default=False)

class Books(models.Model):
    title = models.CharField(max_length= 100, db_column= "title_of_book")
    author = models.CharField(max_length= 100, db_column= "name_of_author")
    image = models.CharField(max_length= 100)
    status= models.CharField(max_length=100)
    def __str__(self):
        return self.title
