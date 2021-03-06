from rest_framework import viewsets
from .models import *
from .serializers import CategoryProcedureSerializer, ProcedureSerializer, ContactSerializer, RequestSerializer

class CategoryProcedureListAPIView(viewsets.ModelViewSet):

    serializer_class = CategoryProcedureSerializer
    queryset = CategoryProcedure.objects.all()

class ProcedureListAPIView(viewsets.ModelViewSet):

    serializer_class = ProcedureSerializer
    queryset = Procedure.objects.all()

class ContactListAPIView(viewsets.ModelViewSet):

    serializer_class = ContactSerializer
    queryset = Contacts.objects.all()

class RequestListAPIView(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    queryset = Requests.objects.all()

