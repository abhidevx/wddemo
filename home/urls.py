# imports
from django.urls import include, path
from rest_framework import routers
from . import views

# defining home app router
router = routers.DefaultRouter()
router.register(r'customer', views.CustomerViewSet, basename='customer')

# exposed endpoints of home app
urlpatterns = [
    path('', include(router.urls))
]