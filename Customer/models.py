from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class Customer(models.Model):
    firstName = models.CharField(max_length=30,default=None)
    middleName = models.CharField(max_length=30,blank=True,null=True)
    lastName = models.CharField(max_length=30,default=None)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message=(
                                     "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    mobileNo = models.CharField(validators=[phone_regex], max_length=15)
    userName=models.CharField(max_length=30,default=None)
    password = models.CharField(max_length=300,default=None)
    emailAdd = models.EmailField(max_length=40,default=None)
    age= models.IntegerField(default=None)
    temporaryAddress = models.TextField(max_length=300,default=None)
    tPincode= models.IntegerField(default=None)
    permanentAddress = models.TextField(max_length=300,default=None)
    pPincode= models.IntegerField(default=None)
    gender= models.CharField(max_length=10,default=None)
    # empId = models.IntegerField(default=None)

    def __str__(self):
        return self.userName

    class Meta:
        db_table = "Customers Information"

class CustomerFeedback(models.Model):
    feedback = models.CharField(max_length=1000, default=None)
    emailAdd = models.EmailField(max_length=40, default=None)
    date=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Customer Feedbacks"