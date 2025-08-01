from django.db import models
import datetime as DT
from django.utils.text import slugify

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, null=True, blank=True, editable=False)
    author = models.CharField(max_length=50)
    description = models.TextField(null = True, blank = True)
    category = models.ManyToManyField('Category', related_name='books')
    image = models.ImageField(upload_to='books/%y/%m/%d/', null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    added_date = models.DateField(default=DT.date.today())
    price = models.DecimalField(max_digits=5, decimal_places=2, default=20.0)
    is_new = models.BooleanField(default= False)
    is_popular = models.BooleanField(default=False)

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return f"{self.title} by {self.author}"

    def set_new(self):
        return self.added_date >= DT.date.today() - DT.timedelta(days=7)

    @property
    def display_image(self):
        if self.image:
            return self.image.url
        elif self.image_url:
            return self.image_url
        return "https://i.pinimg.com/736x/d1/d9/ba/d1d9ba37625f9a1210a432731e1754f3.jpg"

    def save(self, *args, **kwargs):

        self.is_new = self.set_new()
        if self.added_date > DT.date.today():
            self.added_date = DT.date.today()

        self.slug = slugify(self.title)
        super().save(*args, **kwargs)



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"

