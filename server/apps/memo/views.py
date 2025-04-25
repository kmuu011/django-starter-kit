from rest_framework import viewsets, permissions
from .models import Memo
from .serializers import MemoSerializer


class MemoViewSet(viewsets.ModelViewSet):
  serializer_class = MemoSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    return Memo.objects.filter(author=self.request.user).order_by('-created_at')

  def perform_create(self, serializer):
    serializer.save(author=self.request.user)
