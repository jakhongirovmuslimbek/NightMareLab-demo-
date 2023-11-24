from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model
from products.serializers import AnimationSerializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={"input_type": "password"})
    owner_animations = serializers.SerializerMethodField("get_owner_animations")
    user_animations = serializers.SerializerMethodField("get_user_animations")
    thumbnail_image = serializers.ImageField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "image",
            'thumbnail_image',
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
        extra_kwargs = {'password': {'write_only': True}}

    def get_owner_animations(self, obj):
        data = []
        if obj.owner_animations:
            serializer = AnimationSerializer(obj.owner_animations, many=True, context=self.context)
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

#learn
    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        instance.set_password(password)
        instance.save()
        return super().update(instance, validated_data)
    
#learn
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = get_user_model().objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return super().create(validated_data)






# def create(self, validated_data):
#         user = get_user_model().objects.create_user(
#             email=validated_data['email'],
#             password=validated_data['password']
#         )
#         return user













##########

from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model
from product.serializers import AnimationSerializer

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True, style={"input_type": "password"})
    owner_animations=serializers.SerializerMethodField("get_owner_animations")
    user_animations=serializers.SerializerMethodField("get_user_animations")
    thumbnail_image = serializers.ImageField(read_only=True)
    email = serializers.EmailField()
    username=serializers.ReadOnlyField()

    class Meta:
        model=get_user_model()
        fields=[
            "id",
            "image",
            "thumbnail_image",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "middle_name",
            "type_user",
            "owner_animations",
            "user_animations"
        ]
        extra_kwargs = {'password': {'write_only': True}}
    def get_owner_animations(self,obj):
        data=[]
        if obj.owner_animations:
            serializer=AnimationSerializer(obj.owner_animations,many=True,context=self.context)
            data=serializer.data
        return data
    
    def get_user_animations(self,obj):
        # request=self.context.get("request",None)
        # print(request.GET.get("with",None)) #TODO Yaxshi narsa ekan
        data=[]
        if obj.user_animations:
            serializer=AnimationSerializer(obj.user_animations,many=True,context=self.context)
            data=serializer.data
        return data

    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        instance.set_password(password)
        instance.save()
        return super().update(instance, validated_data)

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['username']=validated_data['email']
        user = get_user_model().objects.create_user(**validated_data,)
        user.set_password(password)
        user.save()
        return user


















