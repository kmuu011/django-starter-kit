from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from server.apps.accounts.views import AuthViewSet
from server.apps.memo.views import MemoViewSet
from server.apps.test.views import TestViewSet

router = DefaultRouter()
router.register(r'memo', MemoViewSet, basename='memo')
router.register(r'auth', AuthViewSet, basename='auth')
router.register(r'test', TestViewSet, basename='test')

urlpatterns = [
  path('admin/', admin.site.urls),
  path('api/v1/', include(router.urls)),
]
