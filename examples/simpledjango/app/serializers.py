from .blog_signals import save_blog_log  # noqa
from .models import Blog
from rest_framework import serializers


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
