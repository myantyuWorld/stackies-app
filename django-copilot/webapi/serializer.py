from rest_framework import serializers
from webapi.models import *

class MemberSerializer(serializers.ModelSerializer):
     class Meta:
        model = Member
        fields = ('name', 'email', 'age')

class CategorySerializer(serializers.ModelSerializer):
     class Meta:
        model = Category
        fields = '__all__'

class TechnologySerializer(serializers.ModelSerializer):
     class Meta:
        model = Technology
        fields = '__all__'