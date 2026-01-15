from django.db import models


class BannerImage(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return "Banner Image"
    
    class Meta:
        verbose_name = "Banner Image"
        verbose_name_plural = "Banner Images"

class AboutUs(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return "About Us"
    
    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"



class Service(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"