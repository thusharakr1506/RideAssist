from django.db import models

from django.db.models import Sum

# Create your models here.


class Customer(models.Model):

    name = models.CharField(max_length=200)

    phone = models.CharField(max_length=100)

    email = models.CharField(max_length=200)

    vehicle_no = models.CharField(max_length=100)

    running_km = models.CharField(max_length=100)

    created_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    @property
    def works(self):

        return self.work_set.all()

    @property
    def work_total(self):

        return self.works.values("amount").aggregate(total=Sum("amount"))["total"]


    def __str__(self):

        return self.name


class Work(models.Model):

    title=models.CharField(max_length=200)

    description=models.TextField()

    amount=models.PositiveIntegerField()

    customer_object=models.ForeignKey(Customer,on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):

        return self.title

    