from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from django.urls import path
# from .views import sayHello

from . import views
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    # path('', sayHello, name='sayHello'),
    path('', views.index, name='index'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('menu/', views.MenuItemsView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
    path('menu-items/', views.MenuItemsView.as_view(), name='menu-list'),
    path('menu-items/<int:pk>/',
         views.SingleMenuItemView.as_view(), name='menu-detail'),
    path('message/', views.msg, name='message'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
