from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Kids(models.Model):
  product_name=models.CharField(max_length=100)
  product_price=models.DecimalField(max_digits=8,decimal_places=2)
  product_img=models.ImageField(upload_to='kid')

  def __str__(self):
    return self.product_name


