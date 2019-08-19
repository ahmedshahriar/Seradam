
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
        print("get wishlist")
        queryset = Wishlist.objects.filter(user=self.request.user.id)
        return queryset

    def create(self, request, *args, **kwargs):

        print("in create wishlist")
        data = request.data
        mapping_id = data['id']
        del data['id']
        data['mapping_id'] = mapping_id
        data['user'] = self.request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     print(instance)
    #     self.perform_destroy(instance)
    #     return Response(status=status.HTTP_204_NO_CONTENT)


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

