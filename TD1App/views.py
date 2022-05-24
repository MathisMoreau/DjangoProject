from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from TD1App.models import Machine
def index (request) :
	context = {}
	return render(request,'index.html',context)

def machine_list_view(request):
	machines = Machine.objects.all()
	context={'machines':machines}
	return render(request,'computerapp/machine_list.html',context)

def machine_detail_view(request, pk):
	machine = get_object_or_404(Machine, id=pk )
	context ={'machine': machine }
	return render(request,'computerapp/machine_detail.html',context )