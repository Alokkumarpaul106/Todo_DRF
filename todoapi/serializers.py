from django.db.models import fields
from rest_framework import serializers
from .models import Category,Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','category', 'title','description', 'created_at','updated_at','status','priority')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('id','name','user')