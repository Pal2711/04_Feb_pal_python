from django.db import models

# Create your models here.

class product(models.Model):
    pname = models.CharField(max_length=50)

    def __str__(self):
        return self.pname
    

class product_detail(models.Model):
    pname = models.ForeignKey(product, on_delete=models.CASCADE)
    price = models.IntegerField()
    qty = models.IntegerField()
    pimage=models.ImageField(upload_to="myproducts")
