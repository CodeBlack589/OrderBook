from django.urls import path

from order import views
app_name="order"
urlpatterns=[
    path('',views.home,name="home"),
    path('shareorder',views.ordershare,name="ordershare"),
    path('changeshareprice',views.chnageshareprice,name="chnageshareprice"),
    path('ordershare',views.order,name="orderss"),
    path('checkbuy',views.checkbuy,name="checkbuy"),
    path('sellshare',views.sellproduct,name="sellshare"),
    path('sellmarket',views.sellmarketshare,name="sellmarket"),
    path('selllimit/<id>',views.sellLimitshare,name="sellLimitshare"),
    path('sellstop/<id>',views.sellStopshare,name="sellStopshare")
]
