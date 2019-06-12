from django.db import models
#from django.core.urlresolvers import reverse
from django.urls import reverse #django 2.2


class List(models.Model):

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])



class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None, on_delete=models.SET_DEFAULT)

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')


    def __str__(self):
        return self.text


        
