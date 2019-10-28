from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
from passlib.hash import pbkdf2_sha256

class Employee(models.Model):
    firstName = models.CharField(max_length=30,default=None)
    middleName = models.CharField(max_length=30,null=True,blank=True)
    lastName = models.CharField(max_length=30,default=None)
    phone_regex= RegexValidator(regex=r'^\+?1?\d{9,15}$',
                   message=("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    mobileNo =models.CharField(validators=[phone_regex], max_length=15)
    empName=models.CharField(max_length=30,default=None)
    password = models.CharField(max_length=500,default=None)
    emailAdd = models.EmailField(max_length=40,default=None)
    salary = models.IntegerField(default=None)
    experience= models.IntegerField(default=None)
    age= models.IntegerField(default=None)
    temporaryAddress = models.TextField(max_length=300,default=None)
    tPincode= models.IntegerField(default=None)
    permanentAddress = models.TextField(max_length=300,default=None)
    pPincode= models.IntegerField(default=None)
    gender= models.CharField(max_length=15,default=None)
    # empId = models.IntegerField(default=None)

    def __str__(self):
        return self.empName


    class Meta:
        db_table = "Employee_Information"

        permissions=[("is_employee","can do employee task")]
