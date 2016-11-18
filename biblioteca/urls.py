from django.conf.urls import include, url
from . import views



urlpatterns = [
        url(r'^$', views.postear_libros),
        url(r'^libro/nuevo/$', views.post_new, name='libro_nuevo'),
    ]
