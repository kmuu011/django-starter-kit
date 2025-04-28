from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response


class TestViewSet(viewsets.GenericViewSet):
  permission_classes = [permissions.IsAuthenticated]

  @action(detail=False, methods=['get'],
          permission_classes=[permissions.AllowAny],
          url_path='public')
  def public(self, request):
    return Response({'message': 'public request'})

  @action(detail=False, methods=['get'],
          permission_classes=[permissions.IsAuthenticated],
          url_path='protected')
  def protected(self, request):
    return Response(
      {'message': 'auth request', 'user': request.user.username}
    )
