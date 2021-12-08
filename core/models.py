from django.db import models
from django.contrib.auth.models import User


class Pharmacy(models.Model):
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    zip = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.city}, {self.address}, {self.zip}"


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    patronymic = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    pharmacy_id = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.patronymic}'


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    patronymic = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    manager_id = models.ForeignKey(Manager, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.patronymic}'


class Recipe(models.Model):
    doctor = models.CharField(max_length=50)
    pill_name = models.CharField(max_length=50)
    signature = models.CharField(max_length=256)
    expire_date = models.DateField()



class Pill(models.Model):
    name = models.CharField(max_length=50)
    cost = models.FloatField()
    reg_date = models.DateField()
    end_date = models.DateField(null=True)
    category = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    barcode = models.CharField(max_length=50)
    info = models.CharField(max_length=3000)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Storage(models.Model):
    pill_id = models.ForeignKey(Pill, on_delete=models.CASCADE)
    count = models.IntegerField()
    pharmacy_id = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)

    def __str__(self):
        return self.pharmacy_id.__str__()


class Order(models.Model):
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True, blank=True)
    manager_id = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True, blank=True)
    pharmacy_id = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    is_agreed = models.BooleanField()
    date = models.DateField()


class Basket(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    pill_id = models.ForeignKey(Pill, on_delete=models.CASCADE)
    count = models.IntegerField()
