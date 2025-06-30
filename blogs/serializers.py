from rest_framework import serializers
from .models import *


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'
        
class BlogSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(many=True,read_only=True) #"comments" must be match with model "related_name"
    class Meta:
        model=Blog
        fields='__all__'
        
