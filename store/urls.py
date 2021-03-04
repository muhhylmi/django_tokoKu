from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.store, name='store'),
    path('view/<int:id_barang>', views.view, name='detail-view'),
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', views.signup, name='signup'),
    path('logout/', LogoutView.as_view(next_page='store'), name="logout"),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name='process_order')
]
