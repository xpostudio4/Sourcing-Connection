# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Company'
        db.create_table('companies_company', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=80)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=80)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('value_proposition', self.gf('django.db.models.fields.CharField')(max_length=144, blank=True)),
            ('overview', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('company_status', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('employee_quantity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('web_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('blog_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('twitter_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('facebook_link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('main_phone', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('industries', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('technologies', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('categories', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='Categories', null=True, to=orm['taxonomy.Category'])),
            ('applications', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='Company Country', null=True, to=orm['location.Country'])),
            ('offices', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('acquisition', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('product', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('certification', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('award', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('customer', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('contact', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
        ))
        db.send_create_signal('companies', ['Company'])

        # Adding model 'CompanyRating'
        db.create_table('companies_companyrating', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Ratings for Companies', to=orm['companies.Company'])),
            ('scalability_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('expansion_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('physical_plant_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('profilatibily_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ret_talent_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('financials_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rating_of_ownership', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('gtb_overall_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('companies', ['CompanyRating'])

        # Adding model 'Management'
        db.create_table('companies_management', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Management of the company', to=orm['companies.Company'])),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=56)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=56)),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('companies', ['Management'])

        # Adding model 'Funding'
        db.create_table('companies_funding', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Funds Delivered to', blank=True, to=orm['companies.Company'])),
            ('round', self.gf('django.db.models.fields.CharField')(default='Seed', max_length=16)),
            ('raised', self.gf('django.db.models.fields.CharField')(max_length=45)),
        ))
        db.send_create_signal('companies', ['Funding'])

        # Adding model 'Competitors'
        db.create_table('companies_competitors', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Source Company', blank=True, to=orm['companies.Company'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('companies', ['Competitors'])

        # Adding model 'Office'
        db.create_table('companies_office', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['companies.Company'], blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address_1', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('address_2', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='location', null=True, to=orm['location.City'])),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='Office Country', null=True, to=orm['location.Country'])),
        ))
        db.send_create_signal('companies', ['Office'])

        # Adding model 'AccessCompanyProfile'
        db.create_table('companies_accesscompanyprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Contact User', to=orm['auth.User'])),
        ))
        db.send_create_signal('companies', ['AccessCompanyProfile'])

        # Adding M2M table for field company on 'AccessCompanyProfile'
        db.create_table('companies_accesscompanyprofile_company', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('accesscompanyprofile', models.ForeignKey(orm['companies.accesscompanyprofile'], null=False)),
            ('company', models.ForeignKey(orm['companies.company'], null=False))
        ))
        db.create_unique('companies_accesscompanyprofile_company', ['accesscompanyprofile_id', 'company_id'])

        # Adding model 'ContactCompany'
        db.create_table('companies_contactcompany', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Contact Company', to=orm['companies.Company'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name="Contact's Profile", null=True, to=orm['contacts.Contact'])),
        ))
        db.send_create_signal('companies', ['ContactCompany'])

        # Adding model 'ProfileCompletion'
        db.create_table('companies_profilecompletion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Company Profile Completion ', to=orm['companies.Company'])),
            ('completion', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
        ))
        db.send_create_signal('companies', ['ProfileCompletion'])


    def backwards(self, orm):
        # Deleting model 'Company'
        db.delete_table('companies_company')

        # Deleting model 'CompanyRating'
        db.delete_table('companies_companyrating')

        # Deleting model 'Management'
        db.delete_table('companies_management')

        # Deleting model 'Funding'
        db.delete_table('companies_funding')

        # Deleting model 'Competitors'
        db.delete_table('companies_competitors')

        # Deleting model 'Office'
        db.delete_table('companies_office')

        # Deleting model 'AccessCompanyProfile'
        db.delete_table('companies_accesscompanyprofile')

        # Removing M2M table for field company on 'AccessCompanyProfile'
        db.delete_table('companies_accesscompanyprofile_company')

        # Deleting model 'ContactCompany'
        db.delete_table('companies_contactcompany')

        # Deleting model 'ProfileCompletion'
        db.delete_table('companies_profilecompletion')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'companies.accesscompanyprofile': {
            'Meta': {'object_name': 'AccessCompanyProfile'},
            'company': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Companies '", 'symmetrical': 'False', 'to': "orm['companies.Company']"}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Contact User'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'companies.company': {
            'Meta': {'ordering': "['id']", 'object_name': 'Company'},
            'acquisition': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'applications': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'award': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'blog_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Categories'", 'null': 'True', 'to': "orm['taxonomy.Category']"}),
            'certification': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'company_status': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Company Country'", 'null': 'True', 'to': "orm['location.Country']"}),
            'customer': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'employee_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'facebook_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industries': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'main_phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'offices': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'overview': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'product': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '80'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'technologies': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'twitter_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'value_proposition': ('django.db.models.fields.CharField', [], {'max_length': '144', 'blank': 'True'}),
            'web_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'companies.companyrating': {
            'Meta': {'object_name': 'CompanyRating'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Ratings for Companies'", 'to': "orm['companies.Company']"}),
            'expansion_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'financials_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gtb_overall_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'physical_plant_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'profilatibily_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rating_of_ownership': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ret_talent_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'scalability_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'companies.competitors': {
            'Meta': {'object_name': 'Competitors'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Source Company'", 'blank': 'True', 'to': "orm['companies.Company']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'companies.contactcompany': {
            'Meta': {'object_name': 'ContactCompany'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Contact Company'", 'to': "orm['companies.Company']"}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': '"Contact\'s Profile"', 'null': 'True', 'to': "orm['contacts.Contact']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'companies.funding': {
            'Meta': {'object_name': 'Funding'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Funds Delivered to'", 'blank': 'True', 'to': "orm['companies.Company']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'raised': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'round': ('django.db.models.fields.CharField', [], {'default': "'Seed'", 'max_length': '16'})
        },
        'companies.management': {
            'Meta': {'object_name': 'Management'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Management of the company'", 'to': "orm['companies.Company']"}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '56'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '56'})
        },
        'companies.office': {
            'Meta': {'object_name': 'Office'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'location'", 'null': 'True', 'to': "orm['location.City']"}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['companies.Company']", 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Office Country'", 'null': 'True', 'to': "orm['location.Country']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'})
        },
        'companies.profilecompletion': {
            'Meta': {'object_name': 'ProfileCompletion'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Company Profile Completion '", 'to': "orm['companies.Company']"}),
            'completion': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'contacts.contact': {
            'Meta': {'object_name': 'Contact'},
            'application': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'blog_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'City'", 'null': 'True', 'to': "orm['location.City']"}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'company'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['companies.Company']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Country'", 'null': 'True', 'to': "orm['location.Country']"}),
            'degrees': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'ext_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'financial_organization': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'fr_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'government_organization': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'latech_contact': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ld_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'ls_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'lt_contact': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'm_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'overview': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'photo_profile': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            't_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'technology': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'location.city': {
            'Meta': {'object_name': 'City'},
            'city_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'country'", 'max_length': '50', 'to': "orm['location.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local_talent_pool_rating': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'region_name': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'region'", 'max_length': '50', 'to': "orm['location.Region']"}),
            'telecom_facilities': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'universities': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'url_wiki': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'url_wolfram': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'location.country': {
            'Meta': {'object_name': 'Country'},
            'government_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'policy_favorability_Rating': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'stability_rating': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'url_wiki': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'url_wolfram': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'location.region': {
            'Meta': {'object_name': 'Region'},
            'accesiblity_rating': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'countries'", 'max_length': '30', 'to': "orm['location.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'transportations': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
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

    complete_apps = ['companies']