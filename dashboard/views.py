from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .decorators import auth_users, allowed_users
# Create your views here.


@login_required(login_url='user-login')
def index(request):
    aporteSalud = 0
    aportePension = 0
    auxilioTransporte = 0
    adminFondoPesion = 0
    ingresoNeto = 0
    totalIngreso = 0
    sueldo = 0
    periodo = 2

    try:
        if request.method=="POST":
            sueldo = eval(request.POST.get('sueldo'))
            periodo = eval(request.POST.get('periodo'))

            aporteSalud = sueldo * 0.04
            aportePension = sueldo *0.04
            auxilioTransporte = 117172 if sueldo <= 2000000 else 0
            adminFondoPesion = sueldo * 0.045
            ingresoNeto = sueldo - aportePension - aporteSalud + auxilioTransporte
            totalIngreso = sueldo + auxilioTransporte


            if periodo == 1:
                aporteSalud = aporteSalud * 12
                aportePension = aportePension * 12
                auxilioTransporte = auxilioTransporte * 12
                adminFondoPesion = adminFondoPesion * 12
                ingresoNeto = ingresoNeto * 12
                totalIngreso = totalIngreso * 12

            if periodo == 3:
                aporteSalud = aporteSalud * 0.5
                aportePension = aportePension * 0.5
                auxilioTransporte = auxilioTransporte * 0.5
                adminFondoPesion = adminFondoPesion * 0.5
                ingresoNeto = ingresoNeto * 0.5
                totalIngreso = totalIngreso * 0.5

            if periodo == 4:
                aporteSalud = aporteSalud * 0.25
                aportePension = aportePension * 0.25
                auxilioTransporte = auxilioTransporte * 0.25
                adminFondoPesion = adminFondoPesion * 0.25
                ingresoNeto = ingresoNeto * 0.25
                totalIngreso = totalIngreso * 0.25

            if periodo == 5:
                aporteSalud = aporteSalud * 0.03
                aportePension = aportePension * 0.03
                auxilioTransporte = auxilioTransporte * 0.03
                adminFondoPesion = adminFondoPesion * 0.033
                ingresoNeto = ingresoNeto * 0.033
                totalIngreso = totalIngreso * 0.033

            if periodo == 6:
                aporteSalud = aporteSalud * 0.013
                aportePension = aportePension * 0.013
                auxilioTransporte = auxilioTransporte * 0.013
                adminFondoPesion = adminFondoPesion * 0.013
                ingresoNeto = ingresoNeto * 0.013
                totalIngreso = totalIngreso * 0.013



    except:
        print(e)

    return render(request,"dashboard/index.html",{'sueldo' : sueldo,'periodo':periodo,'aporteSalud':aporteSalud,'aportePension': aportePension,'auxilioTransporte':auxilioTransporte,'adminFondoPesion':adminFondoPesion,'ingresoNeto':ingresoNeto,'totalIngreso':totalIngreso})

