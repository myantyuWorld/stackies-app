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
     category = CategorySerializer(read_only=True)
     category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True)

     def create(self, validated_date):
        validated_date['category'] = validated_date.get('category_id', None)

        if validated_date['category'] is None:
            raise serializers.ValidationError("category not found.") 

        del validated_date['category_id']

        return Technology.objects.create(**validated_date)
     
     class Meta:
        model = Technology
        fields = '__all__'