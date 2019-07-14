from django.conf.urls import url 
from fifton import views 

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^fifton/about/', views.about, name='about'),
	url(r'^add_userinfo/$', views.add_userinfo, name='add_userinfo')

	#The URL's below are for the pages to be created 

	#url(r'^filmacad/$', views.filmacad, name='filmacad'),
	#url(r'^musicaacad/$', views.musicaacad, name='musicacad'),
	#url(r'^photoacad/$', views.photoacad, name='photoacad'), 

]