from django.urls import path, include
from rest_framework.routers import DefaultRouter
<<<<<<< HEAD
from .views import ProductAdd


router = DefaultRouter()
router.register('',ProductAdd)

urlpatterns = [
    path('',include(router.urls)),
=======
from .views import ProductAdd, order_create,order_list,Customer_create,Customer_list,CustomerDelete,Uom_create,Uom_list,Category_create,Category_list


router = DefaultRouter()
router.register('product',ProductAdd)

urlpatterns = [
    path('',include(router.urls)),
    path('order/', order_create.as_view(), name='order-create'),
    path('order/list/', order_list.as_view(), name='order-list'),
    path('customer/', Customer_create.as_view(), name='customer-create'),
    path('customer/list/', Customer_list.as_view(), name='customer-list'),
    path('customer/delete/<int:pk>/', CustomerDelete.as_view(), name='customer-delete'),
    path('uom/', Uom_create.as_view(), name='uom-create'),
    path('uom/list/', Uom_list.as_view(), name='uom-list'),
    path('category/', Category_create.as_view(), name='category-create'),
    path('category/list/', Category_list.as_view(), name='category-list'),
>>>>>>> c1d3c7f76dd2f2a4d6b3589fccf6c8b88f483f9a
]