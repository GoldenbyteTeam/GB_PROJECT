from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('catalogue/<int:catalogue_id>',views.catalogue, name='catalogue'),
    path('addcmd/',views.addcmd, name='addcmd'),
    path('viewcmd/<int:command_id>',views.viewcmd, name='viewcmd'),
    path('editcmd/<int:command_id>',views.editcmd, name='editcmd'),
]

# handling the 404 error
handler404 = 'landingpage.views.error_404_view'
