from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=25, default='TheUpstartcoder')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    # an str is added to a self.author because i
    # ts an object and it needed to be converted to a string

    def get_absolute_url(self):
        #return reverse ('articles', args=(str(self.id)))
        return reverse('home')
