from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.


class Author(models.Model):
    author_first_name = models.CharField(max_length=80)
    author_last_name = models.CharField(max_length=80)
    author_is_alive = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.author_first_name} {self.author_last_name}"


class Book(models.Model):
    book_title = models.CharField(max_length=250)
    book_author = models.ForeignKey(Author, on_delete=models.PROTECT)
    book_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.book_title} written by {self.book_author} with a rating of {self.book_rating}"
