from .orders_urls import *
from .product_urls import *
from .user_urls import *

urlpatterns = product_urlpattern + user_urlpatterns + order_urlpatterns
