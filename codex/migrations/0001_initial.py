# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Rarity'
        db.create_table(u'codex_rarity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal(u'codex', ['Rarity'])

        # Adding model 'Material'
        db.create_table(u'codex_material', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('stack_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=50)),
            ('rarity', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['codex.Rarity'])),
        ))
        db.send_create_signal(u'codex', ['Material'])

        # Adding model 'Consumable'
        db.create_table(u'codex_consumable', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('stack_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=10)),
            ('rarity', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['codex.Rarity'])),
        ))
        db.send_create_signal(u'codex', ['Consumable'])

        # Adding model 'Currency'
        db.create_table(u'codex_currency', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'codex', ['Currency'])


    def backwards(self, orm):
        # Deleting model 'Rarity'
        db.delete_table(u'codex_rarity')

        # Deleting model 'Material'
        db.delete_table(u'codex_material')

        # Deleting model 'Consumable'
        db.delete_table(u'codex_consumable')

        # Deleting model 'Currency'
        db.delete_table(u'codex_currency')


    models = {
        u'codex.consumable': {
            'Meta': {'object_name': 'Consumable'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'rarity': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['codex.Rarity']"}),
            'stack_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '10'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'codex.currency': {
            'Meta': {'object_name': 'Currency'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'codex.material': {
            'Meta': {'object_name': 'Material'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'rarity': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['codex.Rarity']"}),
            'stack_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '50'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'codex.rarity': {
            'Meta': {'object_name': 'Rarity'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['codex']