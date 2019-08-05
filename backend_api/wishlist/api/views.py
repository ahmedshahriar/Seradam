
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import viewsets, status


class WishlistViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    print("authentication pass")
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = WishlistSerializer

    def get_queryset(self):
        queryset = Wishlist.objects.filter(user=self.request.user.id)
        return queryset

    def create(self, request, *args, **kwargs):

        data = request.data
        data['user'] = self.request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        print("before")
        print(headers)
        print(type(headers))
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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

