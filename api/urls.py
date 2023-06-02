from django.urls import path, include
from rest_framework import routers
from api import views

router= routers.DefaultRouter()
router.register(r'api/v1/', views.ProgrammerViewSet, 'projects')

urlpatterns = [
    path('', include(router.urls))
]