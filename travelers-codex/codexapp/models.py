from django.db import models
from polymorphic import PolymorphicModel


def image_file_name(instance, filename):
    extension = os.path.splitext(filename)[1]
    file_name = unicode(instance.id)
    return file_name + extension


class Rarity(models.Model):
    name        = models.CharField(max_length=64)
    color       = models.CharField(max_length=6) # hex colors for web


class BaseItem(PolymorphicModel):
    name        = models.CharField(max_length=128)
    description = models.CharField(max_length=512, null=True, blank=True)
    image       = models.ImageField(upload_to=image_file_name, null=True, blank=True)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


# Item types are their own classes

class Material(BaseItem):
    stack_count = models.PositiveIntegerField(default=50)
    rarity      = models.ForeignKey(Rarity, default=0)


class Consumable(BaseItem):
    stack_count = models.PositiveIntegerField(default=10)
    rarity      = models.ForeignKey(Rarity, default=0)


class Currency(BaseItem):
    pass



# All models below are incomplete and disabled until game release is closer
###########################################################################

# enum-type for player class
# class Class(models.Model):
#     name                            = models.CharField(max_length=64)

# enum-type for factions (Vanguard, Dead Orbit, etc)
# class Faction(models.Model):
#     name                            = models.CharField(max_length=64)


# class PrimaryWeaponType(models.Model):
#     name                            = models.CharField(max_length=64)


# class SpecialWeaponType(models.Model):
#     name                            = models.CharField(max_length=64)


# class HeavyWeaponType(models.Model):
#     name                            = models.CharField(max_length=64)


# # enum-type for damage type (kinetic, void, arc, etc)
# class DamageType(models.Model):
#     name                            = models.CharField(max_length=64)


# A basic gear model, to be completed when the game is closer to release.
# class Gear(BaseItem):
#     level     = models.PositiveIntegerField(default=1)
#     rarity    = models.ForeignKey(Rarity, default=0)
