from django.urls import path,re_path
from . import views


urlpatterns=[
    path("",views.home),
    path("dishes/<str:dish>",views.menu_items,name="menu_items"),
    re_path(r"^match_item/([0-9]{2})/$",views.item_number)
]