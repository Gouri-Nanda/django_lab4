from django.shortcuts import render,redirect
from .forms import CalculationForm
from .models import Calculation


# Create your views here.
# functions

def index(request):
    if request.method=='POST':
        form = CalculationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.result = instance.principal*(instance.rate/100)*instance.time
            instance.save()
            return redirect('index')
    else:
        form = CalculationForm()
    calculations = Calculation.objects.all().order_by('timestamp')

    return render(request,'index.html',{'form':form,'calculations':calculations})
