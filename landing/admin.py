from django.contrib import admin
from .models import About, Feature
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('subheading',)

@admin.register(Feature)
class FeatureAdmin(SummernoteModelAdmin):
    summernote_fields = ('feature_description',)