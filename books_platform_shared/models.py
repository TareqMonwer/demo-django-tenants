from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


