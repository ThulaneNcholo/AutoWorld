from django.db import models

# Create your models here.
class LatestNewsModel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    image1 = models.ImageField(
        null=True, blank=True, upload_to='static/images')
    image2 = models.ImageField(
        null=True, blank=True, upload_to='static/images')
    image3 = models.ImageField(
        null=True, blank=True, upload_to='static/images')
    article = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title