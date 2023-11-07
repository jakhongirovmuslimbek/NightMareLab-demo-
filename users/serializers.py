from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model
from products.serializers import AnimationSerializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.Field(write_only=True)
    owner_animations = serializers.SerializerMethodField("get_owner_animations")
    user_animations = serializers.SerializerMethodField("get_user_animations")

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "image",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "middle_name",
            "type_user",
            "owner_animations",
            "user_animations",
        ]

    def get_owner_animations(self, obj):
        data = []
        if obj.owner_animations:
            serializer = AnimationSerializer(obj.owner_animations, many=True)
            data = serializer.data
        return data 

    def get_user_animations(self, obj):
        # request = self.context.get("request", None)
        # print(request.GET.get("with", None))  #TODO yaxwi narsa ekan

        data = []
        if obj.user_animations:
            serializer = AnimationSerializer(obj.user_animations, many=True)
            data = serializer.data 
        return data 

