from . import views
from django.urls import path

urlpatterns = [
    path("",views.index,name="index"),
    path("data_tables",views.data_tables,name="data_tables"),
    path("data_tables_api",views.data_tables_api,name="data_tables_api"),
    path("server_side_search",views.server_side_search,name="server_side_search"),
    path("server_side_search_api",views.server_side_search_api,name="server_side_search_api"),
]