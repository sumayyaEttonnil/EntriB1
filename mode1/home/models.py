from django.db import models

# Create your models here.


class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    items_img=models.ImageField(upload_to='products',null=True)

    def __str__(self):
      return self.name


class Cart(models.Model):
    name=models.ForeignKey(Product,on_delete=models.CASCADE)

