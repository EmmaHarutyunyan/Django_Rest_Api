from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=100)

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)


    def __str__(self):
        return self.name