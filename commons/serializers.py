"""Commons serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from .models import (Gender, DocumentType)


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ('id', 'short_name', 'long_name')


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        # fields = '__all__'
        fields = ('id', 'long_name', 'short_name', 'character_length', 'type_character')
