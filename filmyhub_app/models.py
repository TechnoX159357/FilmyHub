from django.db import models

# Create your models here.
class contact(models.Model):
    email=models.CharField(max_length=122)
    password=models.CharField(max_length=122)
    
    def __str__(self):
        return self.email
    
    

class movies(models.Model):
    name=models.CharField(max_length=122)
    movie_type=models.CharField(max_length=122)
    imdb=models.FloatField(max_length=122)
    release=models.IntegerField()
    language=models.CharField(max_length=122)
    genres=models.CharField(max_length=122)
    length=models.CharField(max_length=122)
    date=models.DateField()
    link=models.CharField(max_length=122)
    image=models.CharField(max_length=122)
    
    
    def __str__(self):
        return self.name
        