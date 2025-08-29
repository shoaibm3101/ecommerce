from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_page_url(self):
        return reverse("category", kwargs={'id':self.id})
    

class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.ImageField(upload_to="product.image/")
    description = models.CharField(max_length=50, default="")
    background_image = models.ImageField(upload_to="product.image/", default=False)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, related_name="product")

    def __str__(self):
        return self.name
    
    def get_add_to_cart_url(self):
        return reverse("add_to_cart", kwargs={'id':self.id})
    
    def get_info_url(self):
        return reverse("item_info", kwargs={'id':self.id})
    
class OrderItem(models.Model):
    product = models.ForeignKey(Products, null=True, on_delete=models.CASCADE, related_name="order_item")
    quantity = models.IntegerField(default=1)

    def get_delete_cart_item_url(self):
        return reverse("delete_cart_item", kwargs={'id':self.id})

    #def __str__(self):
        #return self.product + ": " + self.quantity






    
