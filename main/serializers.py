from rest_framework import serializers
from .models import UserModel


class UserModelSerializer(serializers.ModelSerializers):
    class Meta:
        model = Snippet
        fields = ['id', 'real_name', 'time_zone']
