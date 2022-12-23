from django.urls import path
from . import views



urlpatterns = [
    path('add',views.add, name='add'),
    path('edit/<int:command_id>',views.edit, name='edit'),
    path('delete/<int:command_id>',views.delete, name='delete'),
]

handler404 = 'landingpage.views.error_404_view'