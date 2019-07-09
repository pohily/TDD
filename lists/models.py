from django.db import models
#from django.core.urlresolvers import reverse
from django.urls import reverse #django 2.2
from django.conf import settings


class List(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])


    @property
    def name(self):
        return self.item_set.first().text


    @staticmethod
    def create_new(first_item_text, owner=None):
        list_ = List.objects.create(owner=owner) 
        Item.objects.create(text=first_item_text, list=list_)
        return list_


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None, on_delete=models.SET_DEFAULT)

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')


    def __str__(self):
        return self.text


        
