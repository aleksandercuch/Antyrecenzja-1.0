from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.postList, name='postList'),
    path('books/', views.bookList, name='bookList'),
    path('aboutMe/', views.aboutMe, name='aboutMe'),
    path('login/', views.loginTemplate, name='loginTemplate'),
    path('reviews/', views.reviewsList, name='reviewsList'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]



