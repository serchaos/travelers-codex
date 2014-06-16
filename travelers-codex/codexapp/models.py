from django.db import models


# Field autosave reference:
# http://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add/1737078#1737078
class TrackCreatedUpdatedModel(models.Model):
    created                         = models.DateTimeField(auto_now_add=True)
    updated                         = models.DateTimeField(auto_now=True)


class AvailableAugments(TrackCreatedUpdatedModel):
    item_fk                         = models.ForeignKey('Item')
    augment_fk                      = models.ForeignKey('Augment')


class Item(TrackCreatedUpdatedModel):
    item_rarity                     = models.ForeignKey('Rarity')
    restricted_to                   = models.ForeignKey('Class')
    # not sure how to best structure this link - putting it here for v1 of schema
    available_augments              = models.ManyToManyField('Augment', through=AvailableAugments)
    # is ImageField the best way?
    # icon                            = models.ImageField(upload_to)


# enum-type for player class
class Class(TrackCreatedUpdatedModel):
    name                            = models.CharField(max_length=64)


# enum-type for factions (Vanguard, Dead Orbit, etc)
class Faction(TrackCreatedUpdatedModel):
    name                            = models.CharField(max_length=64)


# enum-type for item rarity
class Rarity(TrackCreatedUpdatedModel):
    name                            = models.CharField(max_length=64)
    color                           = models.CharField()


# enum-type for all weapon types (sniper, fusion, scout rifle, etc)
class WeaponType(TrackCreatedUpdatedModel):
    name                            = models.CharField(max_length=64)


class Element(TrackCreatedUpdatedModel):
    name                            = models.CharField(max_length=64)


# for optional 'enhancements' available to a weapon of a given rarity - enum-type
# ex: 'Slide farther while this weapon is equipped', 'Carry more ammo of x type'
class Augment(TrackCreatedUpdatedModel):
    description                     = models.CharField(max_length=2048)


class Weapon(TrackCreatedUpdatedModel):
    item_id                         = models.ForeignKey('Item')
    level_req                       = models.PositiveIntegerField()
    name                            = models.CharField(max_length=64)
    description                     = models.CharField(max_length=2048)
    element                         = models.ForeignKey('Element')
    # do we need ranges here?
    impact_min                      = models.PositiveIntegerField()
    impact_max                      = models.PositiveIntegerField()
    range_min                       = models.PositiveIntegerField()
    range_max                       = models.PositiveIntegerField()
    stability_min                   = models.PositiveIntegerField()
    stability_max                   = models.PositiveIntegerField()
    reload_min                      = models.PositiveIntegerField()
    reload_max                      = models.PositiveIntegerField()
    magazine_min                    = models.PositiveIntegerField()
    magazine_max                    = models.PositiveIntegerField()
    fire_rate_min                   = models.PositiveIntegerField()
    fire_rate_max                   = models.PositiveIntegerField()
    

class Headgear(TrackCreatedUpdatedModel):
    item_id                         = models.ForeignKey('Item')
    name                            = models.CharField(max_length=64)
    description                     = models.CharField(max_length=2048)
    str_min                         = models.PositiveIntegerField()
    str_max                         = models.PositiveIntegerField()
    int_min                         = models.PositiveIntegerField()
    int_max                         = models.PositiveIntegerField()
    disc_min                        = models.PositiveIntegerField()
    disc_max                        = models.PositiveIntegerField()


class Gauntlets(TrackCreatedUpdatedModel):
    item_id                         = models.ForeignKey('Item')
    name                            = models.CharField(max_length=64)
    description                     = models.CharField(max_length=2048)
    str_min                         = models.PositiveIntegerField()
    str_max                         = models.PositiveIntegerField()
    int_min                         = models.PositiveIntegerField()
    int_max                         = models.PositiveIntegerField()
    disc_min                        = models.PositiveIntegerField()
    disc_max                        = models.PositiveIntegerField()


class Chestpiece(TrackCreatedUpdatedModel):
    item_id                         = models.ForeignKey('Item')
    name                            = models.CharField(max_length=64)
    description                     = models.CharField(max_length=2048)
    str_min                         = models.PositiveIntegerField()
    str_max                         = models.PositiveIntegerField()
    int_min                         = models.PositiveIntegerField()
    int_max                         = models.PositiveIntegerField()
    disc_min                        = models.PositiveIntegerField()
    disc_max                        = models.PositiveIntegerField()


class Greaves(TrackCreatedUpdatedModel):
    item_id                         = models.ForeignKey('Item')
    name                            = models.CharField(max_length=64)
    description                     = models.CharField(max_length=2048)
    str_min                         = models.PositiveIntegerField()
    str_max                         = models.PositiveIntegerField()
    int_min                         = models.PositiveIntegerField()
    int_max                         = models.PositiveIntegerField()
    disc_min                        = models.PositiveIntegerField()
    disc_max                        = models.PositiveIntegerField()


class ClassItem(TrackCreatedUpdatedModel):
    item_id                         = models.ForeignKey('Item')
    name                            = models.CharField(max_length=64)
    description                     = models.CharField(max_length=2048)
    # Do we need these here too?
    # str_min, str_max                = models.PositiveIntegerField()
    # int_min, int_max                = models.PositiveIntegerField()
    # disc_min, disc_max              = models.PositiveIntegerField()


class Ghost(TrackCreatedUpdatedModel):
    item_id                         = models.ForeignKey('Item')
    name                            = models.CharField(max_length=64)
    description                     = models.CharField(max_length=2048)


class Vehicle(TrackCreatedUpdatedModel):
    item_id                         = models.ForeignKey('Item')
    name                            = models.CharField(max_length=64)
    description                     = models.CharField(max_length=2048)
    durability                      = models.PositiveIntegerField()


class Starship(TrackCreatedUpdatedModel):
    item_id                         = models.ForeignKey('Item')
    name                            = models.CharField(max_length=64)
    description                     = models.CharField(max_length=2048)


class ArmorShader(TrackCreatedUpdatedModel):
    item_id                         = models.ForeignKey('Item')
    name                            = models.CharField(max_length=64)
    description                     = models.CharField(max_length=2048)


class Emblem(TrackCreatedUpdatedModel):
    item_id                         = models.ForeignKey('Item')
    name                            = models.CharField(max_length=64)
    description                     = models.CharField(max_length=2048)


# TODO: Figure out how to represent craftability/recipes :/
class Material(TrackCreatedUpdatedModel):
    item_id                         = models.ForeignKey('Item')
    name                            = models.CharField(max_length=64)
    description                     = models.CharField(max_length=2048)
    stack_to                        = models.PositiveIntegerField()


class Consumable(TrackCreatedUpdatedModel):
    item_id                         = models.ForeignKey('Item')
    name                            = models.CharField(max_length=64)
    description                     = models.CharField(max_length=2048)
    stack_to                        = models.PostiveIntegerField()


class Mission(TrackCreatedUpdatedModel):
    item_id                         = models.ForeignKey('Item')
    name                            = models.CharField(max_length=64)
    description                     = models.CharField(max_length=2048)


class Bounty(TrackCreatedUpdatedModel):
    item_id                         = models.ForeignKey('Item')
    name                            = models.CharField(max_length=64)
    description                     = models.CharField(max_length=2048)
    rep_faction                     = models.FoeignKey('Faction')
    rep_amount                      = models.PositiveIntegerField()
    exp_amount                      = models.PositiveIntegerField()
    