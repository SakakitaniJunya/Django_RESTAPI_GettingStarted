from rest_framework import serializers
from .models import Task, Post
from django.contrib.auth.models import User

# ユーザ作成用
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        # パスワードは読み込みのみに制限
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    # 暗号化している
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class PostSerializer(serializers.ModelSerializer):
    # 日付を単純化
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'created_at')

class TaskSerializer(serializers.ModelSerializer):
    # 日付を単純化
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'created_at')
