from clientapi.viewsets import client_viewset, product_viewset, bill_viewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('client', client_viewset)
router.register('bill', bill_viewset)
router.register('product', product_viewset)


