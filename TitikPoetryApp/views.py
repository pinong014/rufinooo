from django.http import HttpResponse
from TitikPoetryApp.models import Recruit, Tula, TitikEnterprise, ProjectSigya, Comments
from django.shortcuts import render, redirect

def Page(request):
	return render(request, 'Steps.html')
def MainPage(request):
	return render(request, 'Mainpage.html')
def TitikPoetry(request):
	return render(request, 'Titikpoetry.html')
def TitikVideo(request):
	return render(request, 'Titikvideo.html')
def TitikSigya(request):
	return render(request, 'Titiksigya.html')
def TitikEnterprise(request):
	return render(request, 'Titikenterprise.html')
