from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer


class AuthViewSet(viewsets.GenericViewSet):
  permission_classes = [permissions.AllowAny]
  serializer_class = RegisterSerializer

  @action(detail=False, methods=['post'], url_path='register')
  def register(self, request):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=status.HTTP_201_CREATED)

  @action(detail=False, methods=['post'], url_path='login')
  def login(self, request):
    view = ObtainAuthToken.as_view()
    return view(request._request)
