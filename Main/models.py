from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="books", default=1)
    image = models.ImageField(upload_to='books/%y/%m/%d/')
    is_new = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.title} by {self.author}"

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

