from django.db import models

# Create your models here.
class students(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    location = models.CharField(max_length=20,default='Nairobi')
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name0