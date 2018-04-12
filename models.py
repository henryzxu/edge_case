from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='edge_case_pictures/')
    quote = models.TextField()
    
    def __str__(self):
        return self.name
