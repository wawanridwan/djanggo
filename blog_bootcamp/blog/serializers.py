from rest_framework import serializers

class CategorySerializer(serializers.Serializer):
    title = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
