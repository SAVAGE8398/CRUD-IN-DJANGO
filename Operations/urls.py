from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('operations/',views.operations,name='operations'),
    path('operations/editrecord/',views.editrecord,name='editchange'),
    path('operations/editrecord/edit',views.edit,name='editrecord'),
    # path('operations/editrecord/edit',views.edit,name='editfinal'),
]
