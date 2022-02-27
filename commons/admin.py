from django.contrib import admin

# Register your models here.
from commons.models import Gender, DocumentType


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = [
        'short_name',
        'long_name',
        'is_active'
    ]


@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = [
        'long_name',
        'short_name',
        'character_length',
        'type_character',
        'is_active'
    ]
