from rest_framework import viewsets
from .serializers import *
from .models import *

class UserTypeViewSet(viewsets.ModelViewSet):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer

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

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()    
    serializer_class = PaymentSerializer

class RequestTypeViewSet(viewsets.ModelViewSet):
    queryset = RequestType.objects.all()
    serializer_class = RequestTypeSerializer

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

