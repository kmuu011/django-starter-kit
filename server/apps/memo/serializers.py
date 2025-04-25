from rest_framework import serializers
from .models import Memo

class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Memo
        fields = ['id','author','content','created_at','updated_at']
        read_only_fields = ['id','author','created_at','updated_at']
