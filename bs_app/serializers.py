from rest_framework import serializers
from .models import Post, CustomUser


class PostSerializer(serializers.ModelSerializer):
    publisher = serializers.ReadOnlyField(source='publisher.email')

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'publisher')

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password', 'posts')

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        password = validated_data.get('password', None)
        instance.set_password(password)
        instance.save()
        return instance
