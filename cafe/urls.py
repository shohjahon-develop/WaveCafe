from django.urls import path
from .views import (index,icedetailview,hotdetailview,fruitdetailview,aboutdetailview,itemdetailview)

urlpatterns = [
    path('', index, name='index'),
    path('ice/<slug:slug>',icedetailview,name='iceDetail'),
    path('hot/<slug:slug>',hotdetailview,name="hotDetail"),
    path('fruit/<slug:slug>',fruitdetailview,name="fruitDetail"),
    path('about/<slug:slug>',aboutdetailview,name="aboutDetail"),
    path('item/<slug:slug>',itemdetailview,name='itemDetail')
    ]