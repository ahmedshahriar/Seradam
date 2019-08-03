
from .serializers import *
from django.http import JsonResponse


from rest_framework import viewsets


class WishlistViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    print("1")
    serializer_class = WishlistSerializer
    print("2")
    queryset = Wishlist.objects.all()
    print("3")
    def get_queryset(self):
        print("4")
        queryset = Wishlist.objects.all()
        print("5")
        return queryset


# class RyansViewSet(viewsets.ModelViewSet):
#     """
#     A viewset for viewing and editing user instances.
#     """
#     serializer_class = RyansSerializer
#     queryset = Ryans.objects.filter(graphics_memory='Shared')

#
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)

class WishlistListView(ListAPIView):
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()


class WishlistDetailView(RetrieveAPIView):
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()

# class StartechDetailView(RetrieveAPIView):
#     queryset = Startech.objects.all()
#     serializer_class = StartechSerializer
#
#
# class WishlistCreateView(CreateAPIView):
#
#     serializer_class = WishlistSerializer
#     queryset = Wishlist.objects.all()

# class StartechUpdateView(UpdateAPIView):
#     queryset = Startech.objects.all()
#     serializer_class = StartechSerializer
#
#
# class StartechDeleteView(DestroyAPIView):
#     queryset = Startech.objects.all()
#     serializer_class = StartechSerializer
#
#




