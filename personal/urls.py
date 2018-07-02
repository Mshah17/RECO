from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login/', views.login, name="login"),
    url(r'^auth/', views.authentication, name="Authentication"),
    url(r'^result/', views.result, name="result"),
    url(r'^thanks/', views.thanks, name="thanks"),
    url(r'^privacy/',views.privacy, name="privacy"),
    url(r'^contactus/',views.contactus, name="contactus"),
    url(r'^disclaimer/',views.disclaimer, name="disclaimer"),
    url(r'^logout/',views.logout, name="logout"),
    url(r'^pharmacy/',views.pharmacy, name="pharmacy"),
]

