from django.urls import path
from . import views

urlpatterns = [
	path ('', views.index, name ='index') ,
	path ('machines/', views.machine_list_view , name ='machines'),
	path ('machine/<pk>',views.machine_detail_view,name ='machine_detail'),
	path ('personnes/', views.person_list_view , name ='personnes'),
	path ('person/<pk>',views.person_detail_view,name ='person_detail'),
	path ('infrastructures/', views.infra_list_view , name ='infrastructures'),
	path ('infra/<pk>', views.infra_detail_view , name ='infra_detail'),
	
]
