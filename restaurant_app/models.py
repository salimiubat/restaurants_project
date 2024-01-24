# Restaurant Model
from django.db import models
from users.models import User

class Restaurant(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=1)
    
    def save(self, *args, **kwargs):
        self.total_price = self.quantity * sum(item.price for item in self.items.all())
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"Order by {self.user.username}"

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()

#     def __str__(self):
#         return f"{self.quantity} x {self.menu_item.name}"


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment for Order {self.order.id}"