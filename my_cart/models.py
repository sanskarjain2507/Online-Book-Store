from  django.db import models

# Create your models here.
class Cart(models.Model):
    orderId = models.CharField(max_length=250)
    orderName=models.CharField(max_length=300)
    email = models.EmailField(max_length=40)
    quantity = models.IntegerField()
    price = models.IntegerField()
    img = models.CharField(max_length=200)
    address=models.CharField(max_length=500)
    orderDate=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=300)

    def __str__(self):
        return self.orderName
    class Meta:
        db_table='orders'
