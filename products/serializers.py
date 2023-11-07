from rest_framework import serializers
from . import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubCategory
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TagSerializer, self).__init__(*args, **kwargs)
        request = self.context.get("request", None)
        if request.method == "GET":
            self.fields['category'] = CategorySerializer()
    
class BodyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BodyCategory
        fields = "__all__"

class AnimationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Animation
        fields = "__all__"    