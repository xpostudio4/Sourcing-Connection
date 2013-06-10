# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'Alliance.name' to match new field type.
        db.rename_column('company_profile_extended_alliance', 'name_id', 'name')
        # Changing field 'Alliance.name'
        db.alter_column('company_profile_extended_alliance', 'name', self.gf('django.db.models.fields.CharField')(max_length=200))
        # Removing index on 'Alliance', fields ['name']
        db.delete_index('company_profile_extended_alliance', ['name_id'])


        # Renaming column for 'Partnership.name' to match new field type.
        db.rename_column('company_profile_extended_partnership', 'name_id', 'name')
        # Changing field 'Partnership.name'
        db.alter_column('company_profile_extended_partnership', 'name', self.gf('django.db.models.fields.CharField')(max_length=200))
        # Removing index on 'Partnership', fields ['name']
        db.delete_index('company_profile_extended_partnership', ['name_id'])


        # Renaming column for 'TechnicalAssociation.name' to match new field type.
        db.rename_column('company_profile_extended_technicalassociation', 'name_id', 'name')
        # Changing field 'TechnicalAssociation.name'
        db.alter_column('company_profile_extended_technicalassociation', 'name', self.gf('django.db.models.fields.CharField')(max_length=200))
        # Removing index on 'TechnicalAssociation', fields ['name']
        db.delete_index('company_profile_extended_technicalassociation', ['name_id'])


        # Renaming column for 'Competitor.name' to match new field type.
        db.rename_column('company_profile_extended_competitor', 'name_id', 'name')
        # Changing field 'Competitor.name'
        db.alter_column('company_profile_extended_competitor', 'name', self.gf('django.db.models.fields.CharField')(max_length=200))
        # Removing index on 'Competitor', fields ['name']
        db.delete_index('company_profile_extended_competitor', ['name_id'])


    def backwards(self, orm):
        # Adding index on 'Competitor', fields ['name']
        db.create_index('company_profile_extended_competitor', ['name_id'])

        # Adding index on 'TechnicalAssociation', fields ['name']
        db.create_index('company_profile_extended_technicalassociation', ['name_id'])

        # Adding index on 'Partnership', fields ['name']
        db.create_index('company_profile_extended_partnership', ['name_id'])

        # Adding index on 'Alliance', fields ['name']
        db.create_index('company_profile_extended_alliance', ['name_id'])


        # Renaming column for 'Alliance.name' to match new field type.
        db.rename_column('company_profile_extended_alliance', 'name', 'name_id')
        # Changing field 'Alliance.name'
        db.alter_column('company_profile_extended_alliance', 'name_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['companies.Company']))

        # Renaming column for 'Partnership.name' to match new field type.
        db.rename_column('company_profile_extended_partnership', 'name', 'name_id')
        # Changing field 'Partnership.name'
        db.alter_column('company_profile_extended_partnership', 'name_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['companies.Company']))

        # Renaming column for 'TechnicalAssociation.name' to match new field type.
        db.rename_column('company_profile_extended_technicalassociation', 'name', 'name_id')
        # Changing field 'TechnicalAssociation.name'
        db.alter_column('company_profile_extended_technicalassociation', 'name_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['companies.Company']))

        # Renaming column for 'Competitor.name' to match new field type.
        db.rename_column('company_profile_extended_competitor', 'name', 'name_id')
        # Changing field 'Competitor.name'
        db.alter_column('company_profile_extended_competitor', 'name_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['companies.Company']))

    models = {
        'companies.company': {
            'Meta': {'ordering': "['id']", 'object_name': 'Company'},
            'applications': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Categories'", 'null': 'True', 'to': "orm['taxonomy.Category']"}),
            'company_status': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Company Country'", 'null': 'True', 'to': "orm['location.Country']"}),
            'description': ('wysihtml5.fields.Wysihtml5TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'employee_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'founding_date': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industries': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'main_phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'overview': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'product': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '80'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'technologies': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'value_proposition': ('wysihtml5.fields.Wysihtml5TextField', [], {'blank': 'True'})
        },
        'company_profile_extended.alliance': {
            'Meta': {'object_name': 'Alliance'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Company Alliances'", 'to': "orm['companies.Company']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'company_profile_extended.annualrevenue': {
            'Meta': {'object_name': 'AnnualRevenue'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Company Annual Revenue'", 'to': "orm['companies.Company']"}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'revenue': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'})
        },
        'company_profile_extended.competitor': {
            'Meta': {'object_name': 'Competitor'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Company Competitors'", 'blank': 'True', 'to': "orm['companies.Company']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'company_profile_extended.expertise': {
            'Meta': {'object_name': 'Expertise'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Company Expertise'", 'to': "orm['companies.Company']"}),
            'expertise': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        'company_profile_extended.milestone': {
            'Meta': {'object_name': 'Milestone'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Company Milestones'", 'to': "orm['companies.Company']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'from_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'to_date': ('django.db.models.fields.DateField', [], {})
        },
        'company_profile_extended.partnership': {
            'Meta': {'object_name': 'Partnership'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Company Partnerships'", 'to': "orm['companies.Company']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'company_profile_extended.product': {
            'Meta': {'object_name': 'Product'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Company Products'", 'blank': 'True', 'to': "orm['companies.Company']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        'company_profile_extended.project': {
            'Meta': {'object_name': 'Project'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Company Clients'", 'to': "orm['companies.Company']"}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Company Projects'", 'to': "orm['companies.Company']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'company_profile_extended.successstories': {
            'Meta': {'object_name': 'SuccessStories'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Company Stories'", 'to': "orm['companies.Company']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'company_profile_extended.technicalassociation': {
            'Meta': {'object_name': 'TechnicalAssociation'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Company Technical Association'", 'to': "orm['companies.Company']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'company_profile_extended.vertical': {
            'Meta': {'object_name': 'Vertical'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Company Verticals'", 'to': "orm['companies.Company']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200'}),
            'vertical': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'location.country': {
            'Meta': {'object_name': 'Country'},
            'government_type': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'policy_favorability_Rating': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'stability_rating': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'url_wiki': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'url_wolfram': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'taxonomy.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['company_profile_extended']