from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.

class Ice(models.Model):
    img = models.ImageField(upload_to='index/img')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200)
    price = models.FloatField()
    bio = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("iceDetail", args=[self.slug])

class Hot(models.Model):
    img = models.ImageField(upload_to='index/img')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200)
    price = models.FloatField()
    bio = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("hotDetail", args=[self.slug])


class Fruit(models.Model):
    img = models.ImageField(upload_to='index/img')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)
    price = models.FloatField()
    bio = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("fruitDetail", args=[self.slug])


class About(models.Model):
    img = models.ImageField(upload_to='index/img')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("aboutDetail", args=[self.slug])


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name



class Item(models.Model):
    img = models.ImageField(upload_to='index/img')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("itemDetail", args=[self.slug])


class Comment(models.Model):
    ice = models.ForeignKey(Ice,
                               on_delete=models.CASCADE,
                               related_name='comments')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='comments')
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_time']
    def __str__(self):
        return f"Comment -->{self.body} by {self.user}"

















































