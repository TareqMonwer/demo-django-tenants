from django.db import models

from books_platform_shared.models import Category, Publisher


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True, null=True)
    # category = models.ForeignKey(Category, 
    #                              on_delete=models.CASCADE, 
    #                              related_name='books')
    # publisher = models.ForeignKey(Publisher, 
    #                               on_delete=models.CASCADE, 
    #                               related_name='books')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
