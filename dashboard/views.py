from django.shortcuts import render


from django.contrib import messages

from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


# Create your views here.

def DashboardView(request):
	context = {
			
            }
	
	return render(request, "dashboard/dashboard.html", context )