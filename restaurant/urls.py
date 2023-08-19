from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"tables", views.BookingViewSet)

urlpatterns = [

    path('', views.index, name='index'),
    path('menu-items', views.MenuItemsView.as_view(), name='menu-list'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', include(router.urls))
]