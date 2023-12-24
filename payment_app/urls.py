from django.urls import path, include
from . import views

urlpatterns = [
    path('buy/<int:pk>/', views.CreateCheckoutItemSessionView.as_view(), name='create-checkout-item-session'),
    path('item/<int:pk>/', views.ItemIndexPageView.as_view(), name='item-detail'),
    path('order/<int:pk>/', views.OrderIndexPageView.as_view(), name='order-detail'),
    path('buy_order/<int:pk>/', views.CreateCheckoutOrderSessionView.as_view(), name='create-checkout-order-session')
]
