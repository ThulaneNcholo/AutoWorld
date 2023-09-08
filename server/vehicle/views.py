from django.shortcuts import render, redirect
from .models import *
from managers.models import *
from leads.models import *
import random

# Create your views here.


def CarDetailView(request, id):
    carData = GeneralInfoModel.objects.get(id=id)

    context = {
        "carData": carData
    }
    return render(request, 'vehicle/carDetails.html', context)


def MessageView(request, id):
    carInfo = GeneralInfoModel.objects.get(id=id)
    province = ProvinceModel.objects.all()

    if request.method == 'POST' and 'message_seller' in request.POST:
        saveMessage = MessageRequestModel()
        saveMessage.ref = random.randrange(0, 1000000)
        saveMessage.car = GeneralInfoModel.objects.get(id=id)
        saveMessage.firstName = request.POST.get('firstName')
        saveMessage.lastName = request.POST.get('lastName')
        saveMessage.email = request.POST.get('email')
        saveMessage.mobile = request.POST.get('Mobile')
        area = request.POST.get('area')
        saveMessage.area = ProvinceModel.objects.get(id=area)
        saveMessage.message = request.POST.get('message')
        saveMessage.save()
        return redirect('message', id)

    context = {
        "carInfo": carInfo,
        "province": province
    }
    return render(request, 'vehicle/messageData.html', context)
