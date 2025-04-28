from rest_framework import viewsets, permissions
from .serializers import MemoSerializer
from .service import MemoService

class MemoViewSet(viewsets.ModelViewSet):
  serializer_class = MemoSerializer
  permission_classes = [permissions.IsAuthenticated]

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.memo_service = MemoService()

  def get_queryset(self):
    return self.memo_service.list_memos(self.request.user)

  def perform_create(self, serializer):
    memo = self.memo_service.create_memo(serializer.validated_data, self.request.user)
    serializer.instance = memo
