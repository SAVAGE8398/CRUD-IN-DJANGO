from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name='index'),
    path('operations/',views.operations,name='operations'),
    path('operations/editrecord/',views.editrecord,name='editchange'),
    path('operations/deleterecord/',views.deleterecord,name='delete'),
    path('operations/editrecord/edit',views.edit,name='editrecord'),
    # path('operations/editrecord/edit',views.edit,name='editfinal'),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
