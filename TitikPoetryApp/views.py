from TitikPoetryApp.models import Recruit, Tula, ProjectSigya, Comments
from django.shortcuts import render, redirect
from .forms import TulaForm
def Page(request):
	return render(request, 'Steps.html')
def SecondPage(request):
	jenjie=Recruit.objects.create(
		name = request.POST['name'],
		email = request.POST['email'],
		gender = request.POST['gender'],
		birthday = request.POST['birthday']
		)
	return redirect('Poetry')	
	return render(request, 'Steps.html')


def Poetry(request):
	return render(request, 'Titikpoetry.html')
def TitikPoetry(request):
	rufino=Tula.objects.create(
		title_tula = request.POST['name'],
		text = request.POST['Tula'],
		video_file = request.FILES['video'],
		)
	return redirect('Sigya')
	return render(request, 'Titikpoetry.html')

def Sigya(request):
	return render(request, 'Titiksigya.html')

def TitikSigya(request):
	redem=ProjectSigya.objects.create(
		book_donation = request.FILES['picture'],
		messagebox = request.POST['texts'],
		integer = request.POST['nums'],
		date1 = request.POST['dates'],
		)
	return redirect('TitikEnterprise')
	return render(request, 'Titiksigya.html')

def TitikEnterprise(request):
	return render(request, 'TitikEnterprise.html')
def TitikEnterprise(request):
	jenjie=Recruit.objects.all()
	redem=Tula.objects.all()
	lawrence=ProjectSigya.objects.all()
	context ={'jenjie':jenjie,'redem':redem, 'lawrence':lawrence}
	return render(request, 'Titikenterprise.html', context)

def Titikvideo(request):
	return render(request, 'Titikvideo.html')
def Titikvideo(request):
	jenjie=Recruit.objects.all()
	redem=Tula.objects.all()
	lawrence=ProjectSigya.objects.all()
	context ={'jenjie':jenjie,'redem':redem, 'lawrence':lawrence}
	return render(request, 'Titikvideo.html', context)
def Titikpoetry2(request):
	return render(request, 'Titikpoetry2.html')
def Titikpoetry2(request):
	jenjie=Recruit.objects.all()
	redem=Tula.objects.all()
	lawrence=ProjectSigya.objects.all()
	context ={'jenjie':jenjie,'redem':redem, 'lawrence':lawrence}

	return render(request, 'Titikpoetry2.html', context)

def person(request, pk_test):
	person = Recruit.objects.get(id=pk_test)
	acey = person.tula_set.all()


	context = {'person':person, 'acey':acey}
	return render(request, 'person.html',context)






def updateTula(request, pk):

	jenjie = Tula.objects.get(id=pk)
	form = TulaForm(instance=jenjie)

	if request.method == 'POST':
		form = TulaForm(request.POST, instance=jenjie)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'update.html', context)

def deleteTula(request, pk):
	jenjie = Tula.objects.get(id=pk)
	if request.method == "POST":
		jenjie.delete()
		return redirect('/')

	context = {'item':jenjie}
	return render(request, 'delete.html', context)
