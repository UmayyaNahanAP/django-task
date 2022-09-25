from xml.dom.minidom import NamedNodeMap
from django.urls import path
from hostels.views import hostel,employee,new,update,delete

app_name='hostels'

urlpatterns = [
    path('',hostel,name='hostel'),
    path('new/',new,name='new'),
    path('<int:id>/',employee,name='details'),
    path('<int:id>/update/',update,name='update'),
    path('<int:id>/delete/',delete,name='delete'),
]

