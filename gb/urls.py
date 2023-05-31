"""gb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os.path import join
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
# from .settings import BASE_DIR
# import random

# def get_hash_from_quotes(hash_lenght,templates_dir='templates',templetase_subdir='pages', quote_file='quotes.html'):
#
#     try:
#         with open(join(join(join(BASE_DIR,templates_dir),templetase_subdir),quote_file), "r") as f:
#             fquotes_lenght = len(f.read())
#     except:
#         pass
#
#     if fquotes_lenght > 0:
#         hash = random.getrandbits(fquotes_lenght)
#
#     return str(hash)[:hash_lenght]
#
#
# try:
#     from .local_settings import gb_admin_page
# except ImportError:
#     print('local settings file not found!!')
#     pass

urlpatterns = [
    path('', include('landingpage.urls')),
    path('accounts/',include('accounts.urls')),
    path('catalogue/',include('catalogue.urls')),
    re_path(r'cmd/',include('clicommands.urls')),
    path('admin/',admin.site.urls),
    re_path(r"^chaining/", include("smart_selects.urls")),
]  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

handler404 = 'landingpage.views.error_404_view'