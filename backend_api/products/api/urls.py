from django.urls import path



from .views import *
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('', StartechViewSet, basename='articles')
# urlpatterns = router.urls





from .views import *

urlpatterns =[
    path('mapping/', MappingListView.as_view()),
    path('brand/', BrandListView.as_view()),
    path('notification/', NotificationListView.as_view()),
    path('notificationwishlistcount/', NotificationWishlistCountView.as_view()),

    path('searchwishlistcountofuser/', AdminSearchWishCountOfUserListView.as_view()),
    path('userregistrationgraph/', AdminUserRegistrationListView.as_view()),
    path('brandproductswebsitesusercount/', AdminBrandProductsWebsitesUserCountListView.as_view()),
    path('searchcountperday/', AdminSearchCountPerDayListView.as_view()),
    path('searchhitbyhour/', AdminSearchCountPerDayListView.as_view()),
    path('useractivity/', AdminUserActivityListView.as_view())
]