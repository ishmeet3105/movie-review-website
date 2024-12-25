from rest_framework import serializers
from .models import Blog

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['sno','title','genre','content','short_desc','slug', 'time', 'poster']



