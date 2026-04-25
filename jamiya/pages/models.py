from django.db import models

# Create your models here.

class Page(models.Model):
    slug = models.SlugField(unique=True)

    title_en = models.CharField(max_length=200)
    title_ur = models.CharField(max_length=200)

    content_en = models.TextField()
    content_ur = models.TextField()

    def __str__(self):
        return self.title_en


class MenuItem(models.Model):
    title_en = models.CharField(max_length=100)
    title_ur = models.CharField(max_length=100)
    slug = models.SlugField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title_en
