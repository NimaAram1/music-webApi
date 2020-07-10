from django.db import models

class Music(models.Model):
    name = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='images')
    song = models.FileField(upload_to='songs')
    artist = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
