from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^najslabsi/', views.najs_10, name='najs_10'),
    url(r'^najboljsi/', views.najb_10, name='najb_10'),
    url(r'^opis/', views.o_nas, name='o_nas'),
    url(r'^prijava/', views.prijava, name='prijava'),
    url(r'^registracija/', views.registracija, name='registracija'),
    url(r'^moja/', views.moja, name='moja'),
    url(r'^racunalo/', views.racunalo, name='racunalo'),
    url(r'^poraba/(?P<car_id>[0-9]+)', views.poraba, name='poraba'),
    url(r'^logout/', views.logout1, name='logout'),
    url(r'^iskanje/', views.iskanje, name='iskanje'),
]
