# from django.urls import path
#
#

from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', WishlistViewSet, basename='wishlists')
urlpatterns = router.urls


#
#
#
# # from .views import *
# #
# # urlpatterns =[
# #     path('',WishlistListView.as_view()),
# #     # path('create/',WishlistCreateView.as_view()),
# # ]