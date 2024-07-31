from django.db import models

# Create your models here.


class ImageModel(models.Model):
    title = models.CharField(max_length=155, null=True)
    image = models.ImageField(upload_to='uploads/')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
