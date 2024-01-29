from django.db import models
from django.contrib.auth.models import User 
from PIL import Image

# Create your models here.
    
class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    institute=models.CharField(max_length=200, null=True, blank=True, default="")
    img=models.ImageField(upload_to='images', default='default_pic.jpg')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image=Image.open(self.img.path)

        if image.height>300 or image.width>300:
            output_size= (300, 300)
            image.thumbnail(output_size)
            image.save(self.img.path)

    def __str__(self):
        return str(self.user) +" "+self.institute