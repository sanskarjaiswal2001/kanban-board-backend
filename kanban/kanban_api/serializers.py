from rest_framework import serializers
from .models import *

class BoardSerializer (serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'
        
class TaskSerializer (serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        
class EmployeeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        
class CommentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'