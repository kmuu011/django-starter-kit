from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from server.apps.memo.views import MemoViewSet

router = DefaultRouter()
router.register(r'memos', MemoViewSet, basename='memo')

urlpatterns = [
  path('admin/', admin.site.urls),
  path('api/v1/', include(router.urls)),
  path('api/v1/auth/', include('server.apps.accounts.urls')),
]
