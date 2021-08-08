from django.shortcuts import render
from .models import TopFoods,CustomerSays
# Create your views here.

def home(request):



    food=TopFoods.objects.all()
    rev=CustomerSays.objects.all()
    return render(request,'home.html',{'food':food,'rev':rev})