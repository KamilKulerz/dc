# from django.urls import path, include
from lice.views import home, license_detail_view, sign_license_view, license_clear_view, no_access, license_create_view
from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'lice'

urlpatterns = [

    url(r'^$', home, name='home'),
    path('<str:id>', license_detail_view, name='license_detail_view'),
    path('clear/<str:id>', license_clear_view, name='license_clear_view'),
    path('sign/<str:id>', sign_license_view, name='sign_license_view'),
    url(r'^no_access/$', no_access, name='no_access'),
    url(r'^create/$', license_create_view, name='create'),


]
urlpatterns += static(settings.STATIC_ROOT)
