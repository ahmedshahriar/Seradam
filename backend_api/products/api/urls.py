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
    path('admin/', AdminListView.as_view()),
    path('searchwishlist/', SearchWishlistView.as_view()),
    path('notification/', NotificationListView.as_view()),
    path('notificationwishlistcount/', NotificationWishlistCountView.as_view())




    # path('wishlist/',M)
    # path('ryans/',RyansListView.as_view()),
    # path('ryans/<pk>/',RyansDetailView.as_view()),
    # path('create/', ArticleCreateView.as_view()),
    # path('<pk>', ArticleDetailView.as_view()),
    # path('<pk>/update/', ArticleUpdateView.as_view()),
    # path('<pk>/delete/', ArticleDeleteView.as_view())
]