from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Artist(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)

    def __str__(self):
        return self.name + " " + self.surname

class CustomUser(AbstractUser):
    ROLE_CHOICES= (
        ('a', 'Admin'),
        ('r', 'Retailer'),
        ('c', 'Customer')
    )
    role=models.CharField(max_length=10, choices=ROLE_CHOICES, ) 

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name    

class ArtPiece(models.Model):
    title=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.TextField()
    width=models.IntegerField()
    height=models.IntegerField()
    available_pieces=models.IntegerField()
    artist=models.ForeignKey(Artist, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="paintings")

    def __str__(self):
        return self.title 


class Cart(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    art=models.ForeignKey(ArtPiece, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "User: " + self.user.username + " Art: " + self.art.title

class DeliveryInfo(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    postal_code=models.IntegerField()
    country=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)

    def __str__(self):
        return "Delivery info for " + self.user.username

class Order(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_price=models.IntegerField()
    delivery_info=models.ForeignKey(DeliveryInfo, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

 
