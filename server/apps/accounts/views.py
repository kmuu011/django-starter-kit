from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import RegisterSerializer


class AuthViewSet(viewsets.GenericViewSet):
  permission_classes = [permissions.AllowAny]
  serializer_class = RegisterSerializer

  @action(detail=False, methods=['post'], url_path='register')
  def register(self, request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({'message': 'registered'}, status=status.HTTP_201_CREATED)

  @action(detail=False, methods=['post'], url_path='login')
  def login_session(self, request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is None:
      return Response(
        {'detail': 'Invalid credentials'},
        status=status.HTTP_400_BAD_REQUEST
      )
    login(request, user)
    return Response({'message': 'logged in'}, status=status.HTTP_200_OK)

  @action(detail=False, methods=['post'], url_path='logout',
          permission_classes=[permissions.IsAuthenticated])
  def logout_session(self, request):
    logout(request)
    return Response({'message': 'logged out'}, status=status.HTTP_200_OK)
