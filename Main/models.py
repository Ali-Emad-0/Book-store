from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField(null = True, blank = True)
    category = models.ManyToManyField('Category', related_name='books')
    image = models.ImageField(upload_to='books/%y/%m/%d/', default="books/default_ico/default.png")
    is_new = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=20.0)

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        ordering = ['title']

    @property
    def display_image(self):
        if self.image:
            return self.image.url
        return "https://i.pinimg.com/736x/d1/d9/ba/d1d9ba37625f9a1210a432731e1754f3.jpg"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"

