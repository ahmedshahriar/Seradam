from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import UserActivity

from datetime import  datetime
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        if user.is_staff:
            user_type = "admin"
        else:
            user_type = "normaluser"

        date = datetime.now()
        # date = datetime(date.year, date.month, date.day)
        if UserActivity.objects.filter(date=date, user=user.id):
            pass
        else:
            instance = UserActivity(date=date, user=user)
            instance.save()

        return Response({
            'key': token.key,
            'user_type': user_type
        })