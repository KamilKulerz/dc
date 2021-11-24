"""bcdc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url('bc/', include('bcdc_viewer.urls')),
    url('lic/', include('lice.urls')),
    url('', include('loader.urls')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)), ]

admin.site.site_header = "BCDC Admin"
admin.site.site_title = "BCDC Admin"
admin.site.index_title = "BCDC Admin Page"
