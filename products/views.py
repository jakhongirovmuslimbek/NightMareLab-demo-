from rest_framework import viewsets
from .serializers import * 
from .models import *

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
class BodyCategoryViewSet(viewsets.ModelViewSet):
    queryset = BodyCategory.objects.all()
    serializer_class = BodyCategorySerializer

class AnimationViewSet(viewsets.ModelViewSet):
    queryset = Animation.objects.all()    
    serializer_class = AnimationSerializer
