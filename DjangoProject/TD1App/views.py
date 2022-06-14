from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from TD1App.models import Machine
from TD1App.models import Infra
from TD1App.models import Moi
from datetime import datetime

def index (request) :
	date = datetime.today()
	context = {}
	return render(request,'index.html',context={"date": date})

def machine_list_view(request):
	machines = Machine.objects.all()
	context={'machines':machines}
	return render(request,'computerapp/machine_list.html',context)

def machine_detail_view(request, pk):
	machine = get_object_or_404(Machine, id=pk )
	context ={'machine': machine }
	return render(request,'computerapp/machine_detail.html',context )

def infra_list_view(request):
	infrastructures = Infra.objects.all()
	context={'infrastructures':infrastructures}
	return render(request,'computerapp/infra_list.html',context)

def infra_detail_view(request, pk):
	infrastructure = get_object_or_404(Infra, id=pk )
	context={'infrastructure':infrastructure}
	return render(request,'computerapp/infra_detail.html',context)

def person_list_view(request):
	personnes = Moi.objects.all()
	context={'personnes':personnes}
	return render(request,'computerapp/person_list.html',context)

def person_detail_view(request, pk):
	personne = get_object_or_404(Moi, id=pk )
	context={'personne':personne}
	return render(request,'computerapp/person_detail.html',context)