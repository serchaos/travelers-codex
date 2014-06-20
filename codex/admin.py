from django.contrib import admin
from codex.models import Currency, Rarity, Material, BaseItem


admin.site.register(Rarity)
admin.site.register(Currency)
admin.site.register(Material)