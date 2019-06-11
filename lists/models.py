from django.db import models
from django.urls import reverse

class List(models.Model):
    
    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])


class Item(models.Model):
    text = models.TextField(default='', unique=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE, default=None)

    class Meta:
        unique_together = ['text', 'list']
        ordering = ['id']

    def __str__(self):
        return self.text


        
