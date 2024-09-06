from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=25)
    bio = models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    def published_recently(self) -> bool:
        return self.published_date < 7