from django.db import models

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    quantity = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to='product_images/', default = 'default.png')

    def __str__(self):
        return self.name