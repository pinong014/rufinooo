from django.urls import path
from . import views

urlpatterns = [
	path('', views.Page, name="home"),
	path('SecondPage', views.SecondPage, name='SecondPage'),


	path('Poetry', views.Poetry, name="Poetry"),
	path('TitikPoetry', views.TitikPoetry, name="TitikPoetry"),


	path('Sigya', views.Sigya, name="Sigya"),
	path('TitikSigya', views.TitikSigya, name="TitikSigya"),






	path('TitikEnterprise', views.TitikEnterprise, name="TitikEnterprise"),
	path('Titikvideo', views.Titikvideo, name="Titikvideo"),
	path('Titikpoetry2', views.Titikpoetry2, name="Titikpoetry2"),
	path('person/<str:pk_test>/', views.person, name="person"),

	path('update_tula/<str:pk>/', views.updateTula, name="update_tula"),
	path('delete_tula/<str:pk>/', views.deleteTula, name="delete_tula"),
]