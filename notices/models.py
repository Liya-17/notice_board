from django.db import models
 
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='notices/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(blank=True, null=True)  # Add this line
    categories = models.ManyToManyField(Category, related_name='notices', blank=True)
    tags = models.ManyToManyField(Tag, related_name='notices', blank=True)
    file = models.FileField(upload_to='notices/', null=True, blank=True)

    def __str__(self):
        return self.title
    
    def is_expired(self):
        if self.expiry_date:
            return self.expiry_date <= timezone.now()
        return False


