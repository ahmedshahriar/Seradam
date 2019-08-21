from djongo.models import Sum,Max
from django.db.models.functions import Coalesce
from pprint import pprint
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import views
from products.models import Search
from wishlist.models import Wishlist
from datetime import datetime,timedelta
import calendar
from dateutil.relativedelta import *
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)


class AdminBrandProductsWebsitesUserCountListView(views.APIView):

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


class AdminUserRegistrationListView(views.APIView):

    permission_classes = [IsAdminUser]

    def get(self, request):
        current_date = datetime.now()
        month = current_date.month
        year = current_date.year
        result = dict()
        start_date = datetime(year, month, 1)

        for i in range(1, 13):
            end_date = start_date + relativedelta(months=+1)

            users = User.objects.filter(date_joined__range=(start_date, end_date)).count()
            result[start_date.strftime("%B")] = users

            start_date = start_date + relativedelta(months=-1)

        return Response(result)


class AdminSearchCountPerDayListView(views.APIView):

    permission_classes = [IsAdminUser]

    def get(self, request):

        result = dict()
        start_date = datetime.now()

        for i in range(0, 8):
            end_date = start_date + relativedelta(hours=-3)
            hour = start_date.hour
            if hour < 12:
                if hour == 0:
                    hour = 12
                hour = str(hour) + "am"
            else:
                hour = 12 - (24 - hour)
                if hour == 0:
                    hour = 12
                hour = str(hour) + "pm"

            hit = 0
            # Coalesce(Sum('field'), 0)
            try:
                hit = SearchHit.objects.filter(date__range=(end_date, start_date)).aggregate(Sum('count'))
                # hit = SearchHit.objects.filter(date__range=(end_date, start_date)).aggregate(Coalesce(Sum('count'), 0))
                # hit = SearchHit.objects.filter(date__range=(end_date, start_date)).aggregate(Coalesce(models.Sum('count'), 0))
                hit = hit["count__sum"]
            except Exception as e:
                hit = 0

            result[hour] = hit

            start_date = end_date

        return Response(result)


class AdminUserActivityListView(views.APIView):

    permission_classes = [IsAdminUser]

    def get(self, request):

        result = dict()
        start_date = datetime.now()
        start_date = datetime(start_date.year, start_date.month, start_date.day)
        for i in range(0, 7):
            # print(start_date)
            end_date = start_date + timedelta(hours=+24)
            print(start_date)
            print(end_date)
            print(start_date.strftime("%A"))
            hit = 0
            # Coalesce(Sum('field'), 0)
            try:
                hit = UserActivity.objects.filter(date__range=(start_date, end_date)).count()

            except Exception as e:
                hit = 0
            print(hit)
            result[start_date.strftime("%A")] = hit
            start_date = start_date + timedelta(hours=-24)

        # pprint(result)
        return Response(result)


class AdminSearchCountPerDayListView1(views.APIView):

    permission_classes = [IsAdminUser]

    def get(self, request):

        result = dict()
        start_date = datetime.now()

        for i in range(0, 8):
            end_date = start_date + relativedelta(hours=-3)
            hour = start_date.hour
            if hour < 12:
                if hour == 0:
                    hour = 12
                hour = str(hour) + "am"
            else:
                hour = 12-(24-hour)
                if hour == 0:
                    hour = 12
                hour = str( hour) + "pm"

            hit = 0
            # Coalesce(Sum('field'), 0)
            try:
                hit = SearchHit.objects.filter(date__range=(end_date, start_date)).aggregate(Sum('count'))
                # hit = SearchHit.objects.filter(date__range=(end_date, start_date)).aggregate(Coalesce(Sum('count'), 0))
                # hit = SearchHit.objects.filter(date__range=(end_date, start_date)).aggregate(Coalesce(models.Sum('count'), 0))
                hit = hit["count__sum"]
            except Exception as e:
                hit = 0

            result[hour] = hit

            start_date = end_date

        return Response(result)


class AdminSearchWishCountOfUserListView(views.APIView):

    permission_classes = [IsAdminUser]
    serializer_class = SearchWishlistSerializer

    def get(self, request):

        results = []

        users = Search.objects.all()
        for user in users:

            name = User.objects.filter(id=user.user_id).values("username")[0]['username']
            print(name)
            name = name
            print(user)
            # len(Mapping.objects.values("brand").distinct())
            result = {"name": name}

            wishlist_count = Wishlist.objects.filter(user_id=user.user.id).count()

            result["search_count"] = user.search_count
            result["wishlist_count"] = wishlist_count

            results.append(result)
        results = SearchWishlistSerializer(results, many=True).data
        return Response(results)


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

    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Mapping.objects.all()
    serializer_class = MappingSerializer
    def get_queryset(self):

        queryset = Mapping.objects.all()

        graphics_memory = self.request.query_params.get('graphics_memory', None)
        brand = self.request.query_params.get('brand', None)
        ram_type = self.request.query_params.get('ram_type', None)
        ram = self.request.query_params.get('ram', None)
        display_size = self.request.query_params.get('display_size', None)
        sites = self.request.query_params.get('site', None)
        key = self.request.query_params.get('key', None)
        print("brand")
        if brand is not None:
            brand = brand.split(",")
        else:
            brand = []
        print(brand)
        print(type(brand))
        print("sites")
        if sites is not None:
            sites = sites.split(",")
        else:
            sites = []
        print(sites)
        print(type(sites))

        if key is not None:
            print(key)
            queryset = Mapping.objects.filter(product_title__icontains=key)
            print("after key")
            pprint(queryset)
            print("\n\n")
        if graphics_memory is not None:
            # print("graphics memory : " + graphics_memory)
            queryset = queryset.filter(graphics_memory=graphics_memory)
            print("after graphics")
            pprint(queryset)
            print("\n\n")
        if len(brand) > 0:
            print(len(brand))
            if brand[0] != 'false' and brand[0]!='':
                print("printing count")
                print(brand)
                test_name_filter = {'brand__in': brand}
                queryset = queryset.filter(**test_name_filter)
                print("after brand")
                pprint(queryset)
                print("\n\n")

        if ram_type is not None:
            # print("ram tpye : " + ram_type)
            queryset = queryset.filter(ram_type=ram_type)
            print("after ram type")

            pprint(queryset)
            print("\n\n")
        if ram is not None:
            # print("ram : " + ram)
            queryset = queryset.filter(ram=ram)
        if display_size is not None:
            # print("display_size : " + display_size)
            queryset = queryset.filter(display_size=display_size)


        date = datetime.now()
        instance = SearchHit(date=date, count=1)
        instance.save()

        id = self.request.user.id

        if queryset.count() > 0 and id is not None:

            if Search.objects.filter(user_id=id):
                data = Search.objects.filter(user_id=id)
                data = data[0].search_count
                Search.objects.filter(user_id=id).update(search_count = data+1)
            else:
                instance = Search(user_id=id, search_count=1)
                instance.save()
        # print("sending----------------------------------------------------")
        pprint(queryset)
        # if queryset.count() == 0:
        #     return Response({
        #         "nodata": "nodata"
        #     })
        return queryset
