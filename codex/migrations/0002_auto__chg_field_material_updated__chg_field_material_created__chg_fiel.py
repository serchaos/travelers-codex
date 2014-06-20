# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Material.updated'
        db.alter_column(u'codex_material', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True))

        # Changing field 'Material.created'
        db.alter_column(u'codex_material', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True))

        # Changing field 'Consumable.updated'
        db.alter_column(u'codex_consumable', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True))

        # Changing field 'Consumable.created'
        db.alter_column(u'codex_consumable', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True))

        # Changing field 'Currency.updated'
        db.alter_column(u'codex_currency', 'updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True))

        # Changing field 'Currency.created'
        db.alter_column(u'codex_currency', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Material.updated'
        raise RuntimeError("Cannot reverse this migration. 'Material.updated' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Material.updated'
        db.alter_column(u'codex_material', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # User chose to not deal with backwards NULL issues for 'Material.created'
        raise RuntimeError("Cannot reverse this migration. 'Material.created' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Material.created'
        db.alter_column(u'codex_material', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # User chose to not deal with backwards NULL issues for 'Consumable.updated'
        raise RuntimeError("Cannot reverse this migration. 'Consumable.updated' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Consumable.updated'
        db.alter_column(u'codex_consumable', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # User chose to not deal with backwards NULL issues for 'Consumable.created'
        raise RuntimeError("Cannot reverse this migration. 'Consumable.created' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Consumable.created'
        db.alter_column(u'codex_consumable', 'created', self.gf('django.db.models.fields.DateTimeField')())

        # User chose to not deal with backwards NULL issues for 'Currency.updated'
        raise RuntimeError("Cannot reverse this migration. 'Currency.updated' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Currency.updated'
        db.alter_column(u'codex_currency', 'updated', self.gf('django.db.models.fields.DateTimeField')())

        # User chose to not deal with backwards NULL issues for 'Currency.created'
        raise RuntimeError("Cannot reverse this migration. 'Currency.created' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Currency.created'
        db.alter_column(u'codex_currency', 'created', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        u'codex.consumable': {
            'Meta': {'object_name': 'Consumable'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'rarity': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['codex.Rarity']"}),
            'stack_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '10'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'codex.currency': {
            'Meta': {'object_name': 'Currency'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'codex.material': {
            'Meta': {'object_name': 'Material'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'rarity': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['codex.Rarity']"}),
            'stack_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '50'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'codex.rarity': {
            'Meta': {'object_name': 'Rarity'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['codex']