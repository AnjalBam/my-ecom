from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()


class Product(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(
        USER, related_name='products', on_delete=models.SET_NULL, null=True)
    # image = models.ImageField()
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2)
    numReviews = models.IntegerField(blank=True, null=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    countInStock = models.IntegerField(blank=True, null=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(
        Product, related_name='reviews',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=7, decimal_places=2)
    comment = models.TextField(blank=True, null=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.rating)


class Order(models.Model):
    user = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=255)
    taxPrice = models.DecimalField(max_digits=7, decimal_places=2)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.createdAt)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.CharField(max_length=255, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postalCode = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.address)
