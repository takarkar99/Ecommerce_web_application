from django.apps import AppConfig


class ProductCartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Product_Cart'

    def ready(self):
        import Product_Cart.signal