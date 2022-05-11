from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    summary = models.TextField(max_length=1000)
    author_name = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    image= models.ImageField(upload_to='images/',blank=True)
    


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("index", args=[str(self.id)])
        
        
