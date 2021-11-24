# from django.urls import path, include
# from loader.views import home, about, stop_test
from loader.views import Home, About
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name = 'loader'

urlpatterns = [
    url(r'^about/$', About.as_view(), name='about'),
    url(r'^$', Home.as_view(), name='home'),

]
urlpatterns += static(settings.STATIC_ROOT)
