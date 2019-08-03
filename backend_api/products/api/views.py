
from .serializers import *
from django.http import JsonResponse


from rest_framework import viewsets


# class StartechViewSet(viewsets.ModelViewSet):
#     """
#     A viewset for viewing and editing user instances.
#     """
#     serializer_class = StartechSerializer
#     queryset = Startech.objects.all()


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

class StartechListView(ListAPIView):

    queryset = Startech.objects.all()
    serializer_class = StartechSerializer

    def get_queryset(self):
        queryset = Startech.objects.all()

        graphics_memory = self.request.query_params.get('graphics_memory', None)
        brand = self.request.query_params.get('brand', None)
        ram_type = self.request.query_params.get('ram_type', None)
        ram = self.request.query_params.get('ram', None)
        display_size = self.request.query_params.get('display_size', None)

        # graphics_memory = self.request.

        if graphics_memory is not None:
            print("graphics memory : " + graphics_memory)
            queryset = queryset.filter(graphics_memory=graphics_memory)
        if brand is not None:
            print("brand : " + brand)
            queryset = queryset.filter(brand=brand)
        if ram_type is not None:
            print("ram tpye : " + ram_type)
            queryset = queryset.filter(ram_type=ram_type)
        if ram is not None:
            print("ram : " + ram)
            queryset = queryset.filter(ram=ram)
        if display_size is not None:
            print("display_size : " + display_size)
            queryset = queryset.filter(display_size=display_size)

        return queryset


class MappingListView(ListAPIView):
    queryset = Mapping.objects.all()
    serializer_class = MappingSerializer

    def get_queryset(self):

        queryset = Mapping.objects.all()

        graphics_memory = self.request.query_params.get('graphics_memory', None)
        brand = self.request.query_params.get('brand', None)
        ram_type = self.request.query_params.get('ram_type', None)
        ram = self.request.query_params.get('ram', None)
        display_size = self.request.query_params.get('display_size', None)

        key = self.request.query_params.get('key', None)

        print(key)
        if key is not None:
            # queryset = Mapping.objects.raw_query({ "product_title": { "$regex": key } })
            queryset = Mapping.objects.filter(product_title__icontains=key)
        # graphics_memory = self.request.

        if graphics_memory is not None:
            print("graphics memory : " + graphics_memory)
            queryset = queryset.filter(graphics_memory=graphics_memory)
        if brand is not None:
            print("brand : " + brand)
            queryset = queryset.filter(brand=brand)
        if ram_type is not None:
            print("ram tpye : " + ram_type)
            queryset = queryset.filter(ram_type=ram_type)
        if ram is not None:
            print("ram : " + ram)
            queryset = queryset.filter(ram=ram)
        if display_size is not None:
            print("display_size : " + display_size)
            queryset = queryset.filter(display_size=display_size)

        return queryset

# class WishlistListView(viewsets.ModelViewSet):
#     serializer_class = WishlistSerializer
#     queryset = Wishlist.objects.all()


# class StartechDetailView(RetrieveAPIView):
#     queryset = Startech.objects.all()
#     serializer_class = StartechSerializer
#
#
# class StartechCreateView(CreateAPIView):
#     queryset = Startech.objects.all()
#     serializer_class = StartechSerializer
#
#
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



class RyansListView(ListAPIView):

    serializer_class = RyansSerializer
    queryset = Ryans.objects.all()

    def get_queryset(self):

        queryset = Ryans.objects.all()



        graphics_memory = self.request.query_params.get('graphics_memory', None)
        brand = self.request.query_params.get('brand', None)
        ram_type = self.request.query_params.get('ram_type', None)
        ram = self.request.query_params.get('ram', None)
        display_size = self.request.query_params.get('display_size', None)

        # graphics_memory = self.request.

        if graphics_memory is not None:
            print("graphics memory : " + graphics_memory)
            queryset = queryset.filter(graphics_memory=graphics_memory)
        if brand is not None:
            print("brand : " + brand)
            queryset = queryset.filter(brand=brand)
        if ram_type is not None:
            print("ram tpye : " + ram_type)
            queryset = queryset.filter(ram_type=ram_type)
        if ram is not None:
            print("ram : " + ram)
            queryset = queryset.filter(ram=ram)
        if display_size is not None:
            print("display_size : " + display_size)
            queryset = queryset.filter(display_size=display_size)

        return queryset

# class RyansDetailView(RetrieveAPIView):
#     queryset = Startech.objects.all()
#     serializer_class = RyansSerializer
#
#
# class RyansCreateView(CreateAPIView):
#     queryset = Ryans.objects.all()
#     serializer_class = RyansSerializer
#
#
# class RyansUpdateView(UpdateAPIView):
#     queryset = Ryans.objects.all()
#     serializer_class = RyansSerializer
#
#
# class RyansDeleteView(DestroyAPIView):
#     queryset = Ryans.objects.all()
#     serializer_class = RyansSerializer






def get_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    snippets = Mapping.objects.all()
    serializer = MappingSerializer(snippets, many=True)
    return JsonResponse(serializer.data, safe=False)
