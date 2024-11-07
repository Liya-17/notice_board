from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='notices/', blank=True, null=True)  # Add this line
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title