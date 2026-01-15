from django.db import models

class AboutUs(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return "About Us"


class Service(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
