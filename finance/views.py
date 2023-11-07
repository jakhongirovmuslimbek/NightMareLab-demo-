from rest_framework import viewsets
from .serializers import *
from .models import *

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()    
    serializer_class = PaymentSerializer
