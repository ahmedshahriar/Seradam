
from django.db.models import Count
from pprint import pprint
from django.contrib.auth.models import User
from .serializers import *
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework import views,viewsets
from products.models import Search
from wishlist.models import Wishlist


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


class BrandListView(ListAPIView):

    serializer_class = BrandSerializer

    def get_queryset(self):
        queryset = Mapping.objects.values("brand").distinct()
        return queryset


class NotificationListView(ListAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):


        queryset = Notification.objects.filter(user_id=self.request.user.id).order_by('seen')[:7]
        print("nicher print ta comment korle, queryset a q.seen false thakleo false jay na. true jay. bujhina kahini. vuture problem")
        for q in queryset:
            print(q.seen)

        Notification.objects.filter(user_id=self.request.user.id).update(seen=True)

        return queryset




class BrandListView1(views.APIView):
    serializer_class = BrandSerializer

    def get(self, request):
        queryset = Mapping.objects.values("brand").distinct()
        results = BrandSerializer(queryset, many=True).data
        return Response(results)



class AdminListView(views.APIView):

    permission_classes = [IsAdminUser]
    serializer_class = AdminSerializer

    def get(self, request):

        total_brands = len(Mapping.objects.values("brand").distinct())

        results = [{"total_brands": total_brands }]

        results[0]["total_products"]= Mapping.objects.count()
        results[0]["total_websites"]= 2
        results[0]["total_users"]= User.objects.count()

        results = AdminSerializer(results, many=True).data
        return Response(results)


class SearchWishlistView(views.APIView):

    permission_classes = [IsAdminUser]
    serializer_class = SearchWishlistSerializer

    def get(self, request):

        results = []

        users = Search.objects.all()
        for user in users:

            name = User.objects.filter(id=user.user_id).values("username")[0]['username']

            # len(Mapping.objects.values("brand").distinct())
            result = {"name": name}

            if Search.objects.filter(user_id=request.user.id):
                search_count = Search.objects.filter(user_id=request.user.id)[0].search_count
            else:
                search_count = 0

            wishlist_count = Wishlist.objects.filter(user_id=request.user.id).count()

            result["search_count"] = search_count
            result["wishlist_count"] = wishlist_count

            results.append(result)
        results = SearchWishlistSerializer(results, many=True).data
        return Response(results)


class NotificationWishlistCountView(views.APIView):

    permission_classes = [IsAuthenticated]
    serializer_class = NotificationWishlistCountSerializer

    def get(self, request):
        print("in noti wish count get")
        notification_count = Notification.objects.filter(user_id=request.user.id,seen=False).count()
        wishlist_count = Wishlist.objects.filter(user_id=request.user.id).count()
        results = [{
            "notification_count": notification_count,
            "wishlist_count": wishlist_count
        }]


        results = NotificationWishlistCountSerializer(results, many=True).data
        return Response(results)


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

        if key is not None:
            queryset = Mapping.objects.filter(product_title__icontains=key)

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

        id = self.request.user.id
        if queryset.count() > 0 and id is not None:

            if Search.objects.filter(user_id=id):
                data = Search.objects.filter(user_id=id)
                data = data[0].search_count
                Search.objects.filter(user_id=id).update(search_count = data+1)
            else:
                instance = Search(user_id=id, search_count=1)
                instance.save()

        return queryset



class TestListView(ListAPIView):
    queryset = Mapping.objects.all()
    serializer_class = MappingSerializer

    def get_queryset(self):

        queryset = Mapping.objects.all()

        return queryset

    def post(self, request):

        print(request.data)
        return Response(request.data)



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
