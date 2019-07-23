
from webs.models import *
from .serializers import *


from rest_framework import viewsets


class StartechViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = StartechSerializer
    queryset = Startech.objects.all()







from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)

class StartechListView(ListAPIView):
    queryset = Startech.objects.all()
    serializer_class = StartechSerializer


class StartechDetailView(RetrieveAPIView):
    queryset = Startech.objects.all()
    serializer_class = StartechSerializer


class StartechCreateView(CreateAPIView):
    queryset = Startech.objects.all()
    serializer_class = StartechSerializer


class StartechUpdateView(UpdateAPIView):
    queryset = Startech.objects.all()
    serializer_class = StartechSerializer


class StartechDeleteView(DestroyAPIView):
    queryset = Startech.objects.all()
    serializer_class = StartechSerializer





class RyansListView(ListAPIView):
    queryset = Ryans.objects.all()
    serializer_class = RyansSerializer


class RyansDetailView(RetrieveAPIView):
    queryset = Startech.objects.all()
    serializer_class = RyansSerializer


class RyansCreateView(CreateAPIView):
    queryset = Ryans.objects.all()
    serializer_class = RyansSerializer


class RyansUpdateView(UpdateAPIView):
    queryset = Ryans.objects.all()
    serializer_class = RyansSerializer


class RyansDeleteView(DestroyAPIView):
    queryset = Ryans.objects.all()
    serializer_class = RyansSerializer

