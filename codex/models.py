import os
from django.db import models


def image_file_name(instance, filename):
    extension = os.path.splitext(filename)[1]
    file_name = unicode(instance.id)
    return file_name + extension


class Rarity(models.Model):
    name        = models.CharField(max_length=64)
    color       = models.CharField(max_length=6) # hex colors for web

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Rarities'


class BaseItem(models.Model):
    name        = models.CharField(max_length=128)
    description = models.CharField(max_length=512, null=True, blank=True)
    image       = models.ImageField(upload_to=image_file_name, null=True, blank=True)
    created     = models.DateTimeField(auto_now_add=True, null=True)
    updated     = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


# Item types are their own classes

class Material(BaseItem):
    stack_count = models.PositiveIntegerField(default=50)
    rarity      = models.ForeignKey(Rarity, default=0)

    def __unicode__(self):
        return self.name


class Consumable(BaseItem):
    stack_count = models.PositiveIntegerField(default=10)
    rarity      = models.ForeignKey(Rarity, default=0)

    def __unicode__(self):
        return self.name


class Currency(BaseItem):
    pass

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Currencies'
