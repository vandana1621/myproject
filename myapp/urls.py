from django.urls import path, re_path

from . import views
from .views import index, user_logout, custom_login

from .views import index, user_logout, custom_login, SubcategoryMaster, EquipmentMaster, Orders_Summary, User_master, connects, Calendar, reports

app_name = 'myapp'
urlpatterns = [
    path('', custom_login, name='login'),
    path('index/', index, name='index'),
    path('logout/', user_logout, name='logout'),
    path('custom_login/', custom_login, name='custom_login'),
    path('SubcategoryMaster/', SubcategoryMaster, name='SubcategoryMaster'),
    path('EquipmentMaster/', EquipmentMaster, name='EquipmentMaster'),
    path('Orders_Summary/', Orders_Summary, name='Orders_Summary'),
    path('User_master/', User_master, name='User_master'),
    path('connects/', connects, name='connects'),
    path('Calendar/', Calendar, name='Calendar'),
    path('reports/', reports, name='reports'),

]
