from django.urls import path
from .views import ProductList, ProductDetails , AddtoCard , displayview  , UpdateCart, deletefromcart


urlpatterns = [
    path("li/", ProductList.as_view(), name='product_list'),
    # path('li/', ProductList, name='product_list'),
    path('de/<int:pk>/', ProductDetails.as_view(), name='product_detail'),
    path('card/<int:pk>/', AddtoCard, name='productincart'),
    path('displayinfo/', displayview.as_view(), name='displayview'),
    path("updatecart/<int:pk>/", UpdateCart.as_view(), name='updatecart'),
    path("deletefromcart/<int:pk>/", deletefromcart.as_view(), name='deletefromcart')
]