from django.db import models

# Create your models here.
class Book(models.Model):
    bookId = models.IntegerField()
    title = models.CharField(max_length=30)
    isbn = models.CharField(max_length=15)
    language = models.CharField(max_length=20)
    publisher = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    mrp = models.IntegerField()
    publishYear = models.CharField(max_length=4)
    quantity = models.IntegerField()
    availableQuantity = models.IntegerField()
    description = models.CharField(max_length=3000)
    rating = models.IntegerField()
    forSale=models.CharField(max_length=10)
    category=models.CharField(max_length=30)
    image = models.ImageField(upload_to='Book/media')

    def __str__(self):
        return self.title
    class Meta:
        db_table='Book Details'