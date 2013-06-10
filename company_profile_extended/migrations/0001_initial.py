# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AnnualRevenue'
        db.create_table('company_profile_extended_annualrevenue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Company Annual Revenue', to=orm['companies.Company'])),
            ('revenue', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('company_profile_extended', ['AnnualRevenue'])

        # Adding model 'Milestone'
        db.create_table('company_profile_extended_milestone', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Company Milestones', to=orm['companies.Company'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('to_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('company_profile_extended', ['Milestone'])

        # Adding model 'Project'
        db.create_table('company_profile_extended_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Company Projects', to=orm['companies.Company'])),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Company Clients', to=orm['companies.Company'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('company_profile_extended', ['Project'])

        # Adding model 'SuccessStories'
        db.create_table('company_profile_extended_successstories', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Company Stories', to=orm['companies.Company'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('link', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('company_profile_extended', ['SuccessStories'])

        # Adding model 'Expertise'
        db.create_table('company_profile_extended_expertise', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Company Expertise', to=orm['companies.Company'])),
            ('expertise', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
        ))
        db.send_create_signal('company_profile_extended', ['Expertise'])

        # Adding model 'Vertical'
        db.create_table('company_profile_extended_vertical', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Company Verticals', to=orm['companies.Company'])),
            ('vertical', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200)),
        ))
        db.send_create_signal('company_profile_extended', ['Vertical'])

        # Adding model 'Partnership'
        db.create_table('company_profile_extended_partnership', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Company Partnerships', to=orm['companies.Company'])),
            ('name', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Company Partner', to=orm['companies.Company'])),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('company_profile_extended', ['Partnership'])

        # Adding model 'Alliance'
        db.create_table('company_profile_extended_alliance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Company Alliances', to=orm['companies.Company'])),
            ('name', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Company Ally', to=orm['companies.Company'])),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('company_profile_extended', ['Alliance'])

        # Adding model 'TechnicalAssociation'
        db.create_table('company_profile_extended_technicalassociation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Company Technical Association', to=orm['companies.Company'])),
            ('name', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Company Associate', to=orm['companies.Company'])),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('company_profile_extended', ['TechnicalAssociation'])

        # Adding model 'Competitor'
        db.create_table('company_profile_extended_competitor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Company Competitors', blank=True, to=orm['companies.Company'])),
            ('name', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Company Competitor', to=orm['companies.Company'])),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('company_profile_extended', ['Competitor'])

        # Adding model 'Product'
        db.create_table('company_profile_extended_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Company Products', blank=True, to=orm['companies.Company'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('company_profile_extended', ['Product'])


    def backwards(self, orm):
        # Deleting model 'AnnualRevenue'
        db.delete_table('company_profile_extended_annualrevenue')

        # Deleting model 'Milestone'
        db.delete_table('company_profile_extended_milestone')

        # Deleting model 'Project'
        db.delete_table('company_profile_extended_project')

        # Deleting model 'SuccessStories'
        db.delete_table('company_profile_extended_successstories')

        # Deleting model 'Expertise'
        db.delete_table('company_profile_extended_expertise')

        # Deleting model 'Vertical'
        db.delete_table('company_profile_extended_vertical')

        # Deleting model 'Partnership'
        db.delete_table('company_profile_extended_partnership')

        # Deleting model 'Alliance'
        db.delete_table('company_profile_extended_alliance')

        # Deleting model 'TechnicalAssociation'
        db.delete_table('company_profile_extended_technicalassociation')

        # Deleting model 'Competitor'
        db.delete_table('company_profile_extended_competitor')

        # Deleting model 'Product'
        db.delete_table('company_profile_extended_product')


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
            'name': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Company Ally'", 'to': "orm['companies.Company']"})
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
            'name': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Company Competitor'", 'to': "orm['companies.Company']"})
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
            'name': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Company Partner'", 'to': "orm['companies.Company']"})
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
            'name': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Company Associate'", 'to': "orm['companies.Company']"})
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