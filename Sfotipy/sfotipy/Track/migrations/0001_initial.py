# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Track'
        db.create_table(u'Track_track', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('track_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('artist_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Artist.Artist'])),
        ))
        db.send_create_signal(u'Track', ['Track'])


    def backwards(self, orm):
        # Deleting model 'Track'
        db.delete_table(u'Track_track')


    models = {
        u'Artist.artist': {
            'Meta': {'object_name': 'Artist'},
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'Track.track': {
            'Meta': {'object_name': 'Track'},
            'artist_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Artist.Artist']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'track_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['Track']