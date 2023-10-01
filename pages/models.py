from django.db import models
from utils import cid_to_path

# Create your models here.
class Sneaker(models.Model):
    cid = models.CharField(max_length=50, primary_key=True)
    path = models.CharField(max_length=100, blank=True)  # Adjust the max_length as needed

    def save(self, *args, **kwargs):
        # Calculate the path based on cid using the cid_to_path function
        self.path = cid_to_path(str(self.cid))
        super(Sneaker, self).save(*args, **kwargs)
    

    def __str__(self):
        return f"CID: {self.cid}"

