from django.shortcuts import render, redirect
from vehicle.models import *
from managers.models import *
from django.contrib import messages 

# Create your views here.


def CarSearchFilterView(request):
    make = CarMakeMode.objects.all()

    if request.method == 'POST' and 'submit_search' in request.POST:
        newVariant = request.POST.get('newVariant')
        request.session['variant'] = newVariant
        return redirect('new-car-results')

    context = {
        "make": make,

    }
    return render(request, 'carSearch/carSearch.html', context)


def NewResultsView(request, id=None, type=None):
    if id is None and type is None:
        newVariant = 'None'

        if request.method == 'POST' and 'refine_search' in request.POST:
            variantValue = request.session['variant'] = newVariant

            if variantValue != 'None':
                newVariant = request.POST.get('newVariant')

            return redirect('new-car-results')

        cars = GeneralInfoModel.objects.all()
        carBrand = request.session.get('make')

        # check if user selected a car brand if not redict back to make page 
        if carBrand == 'None':
            messages.success(request,'Please select a car Brand')
            return redirect('index')

        carModel = request.session.get('model')
        userVariant = request.session.get('variant')

        make = CarMakeMode.objects.all()
        seletedMake = None

        models = None
        selectedModel = None

        carVariants = None
        selectedVariant = None

        if carBrand:
            carMake = CarMakeMode.objects.get(id=carBrand)
            cars = GeneralInfoModel.objects.filter(car__make__make=carMake)
            seletedMake = carMake
            models = CarModel.objects.filter(make=carMake)

        if carModel != 'None':
            userModel = CarModel.objects.get(id=carModel)
            cars = GeneralInfoModel.objects.filter(car__make=userModel)
            selectedModel = userModel
            models = CarModel.objects.filter(make=carMake)
            carVariants = CarVariantModel.objects.filter(make=userModel)

        if userVariant != 'None':
            variants = CarVariantModel.objects.get(id=userVariant)
            cars = GeneralInfoModel.objects.filter(car=variants)
            selectedVariant = variants
            carVariants = CarVariantModel.objects.filter(make=userModel)

        context = {
            "cars": cars,
            "make": make,
            "seletedMake": seletedMake,
            "models": models,
            "selectedModel": selectedModel,
            "selectedVariant": selectedVariant,
            "carVariants": carVariants
        }

        return render(request, 'carSearch/newResultsPage.html', context)
    else:
        if type == 0:
            newVariant = 'None'

            if request.method == 'POST' and 'refine_search' in request.POST:
                variantValue = request.session['variant'] = newVariant

                if variantValue != 'None':
                    newVariant = request.POST.get('newVariant')

                return redirect('new-car-results')

            make = CarMakeMode.objects.all()
            carMake = CarMakeMode.objects.get(id=id)
            cars = GeneralInfoModel.objects.filter(car__make__make=carMake)
            seletedMake = carMake
            models = CarModel.objects.filter(make=carMake)

            context = {
                "newVariant": newVariant,
                "make": make,
                "cars": cars,
                "seletedMake": seletedMake,
                "models": models,
            }

            return render(request, 'carSearch/newResultsPage.html', context)

        if type == 1:
            newVariant = 'None'

            if request.method == 'POST' and 'refine_search' in request.POST:
                variantValue = request.session['variant'] = newVariant

                if variantValue != 'None':
                    newVariant = request.POST.get('newVariant')

                return redirect('new-car-results')

            cars = GeneralInfoModel.objects.all()
            make = CarMakeMode.objects.all()
            request.session['make'] = 'None'
            request.session['model'] = 'None'
            request.session['variant'] = 'None'

            context = {
                "newVariant": newVariant,
                "cars": cars,
                "make": make,
            }

            return render(request, 'carSearch/newResultsPage.html', context)

# HTMX Partials


def NewModelView(request):
    models = CarModel.objects.all()

    if request.method == 'POST':
        newBrand = request.POST.get('newBrand')
        request.session['make'] = newBrand
        request.session['model'] = 'None'
        request.session['variant'] = 'None'

        carMake = CarMakeMode.objects.get(id=newBrand)
        models = CarModel.objects.filter(make=carMake)

    context = {
        "models": models
    }

    return render(request, 'partials/newModel.html', context)


def NewVarientView(request):
    carVariants = CarVariantModel.objects.all()

    if request.method == 'POST':
        modelID = request.POST.get('newModelSearch')
        model = CarModel.objects.get(id=modelID)
        carVariants = CarVariantModel.objects.filter(make=model)

        # save model ID to session
        request.session['model'] = modelID
        request.session['variant'] = 'None'

    context = {
        "carVariants": carVariants
    }

    return render(request, 'partials/newVariant.html', context)
