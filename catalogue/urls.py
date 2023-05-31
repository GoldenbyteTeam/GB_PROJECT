from django.urls import path

from . import views

urlpatterns = [
    path('search/<int:catalogue_id>',views.search, name='search'),
]
handler404 = 'landingpage.views.error_404_view'