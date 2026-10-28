from django.db import models

# Create your models here.
class Member(models.Model):
    surname= models.CharField(max_length=200)
    first_name= models.CharField(max_length=200)
    email= models.EmailField()
    phone_number=models.IntegerField()
    
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f" {self.surname} {self.first_name}")