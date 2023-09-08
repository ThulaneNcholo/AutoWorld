from django.shortcuts import render, redirect
from managers.models import *
from vehicle.models import *

# Create your views here.


def CarSearchResultsView(request):
    make = request.session.get('make')
    model = request.session.get('model')
    variant = request.session.get('variant')
    print(make)
    print(model)
    featuredCars = GeneralInfoModel.objects.all()

    # car make filter
    if make != 'None':
        carMake = CarMakeMode.objects.get(id=make)
        featuredCars = GeneralInfoModel.objects.filter(
            car__make__make=carMake)
    else:
        # filter objects
        carMake = CarMakeMode.objects.all()
        carModel = CarModel.objects.all()
        carVariant = CarVariantModel.objects.all()

    # car model filter
    if model != 'None':
        carModel = CarModel.objects.get(id=model)
        featuredCars = featuredCars.filter(car__make=carModel)
    else:
        # filter objects
        carMake = CarMakeMode.objects.all()
        carModel = CarModel.objects.all()
        carVariant = CarVariantModel.objects.all()

    # car varitent filter
    if variant != 'None':
        carVariant = CarVariantModel.objects.get(id=variant)
        featuredCars = featuredCars.filter(car=carVariant)
    else:
        # filter objects
        carMake = CarMakeMode.objects.all()
        carModel = CarModel.objects.all()
        carVariant = CarVariantModel.objects.all()

    if request.method == 'POST' and 'refineSearchPost' in request.POST:
        # Clear session after adding the features
        request.session['make'] = 'None'
        request.session['model'] = 'None'
        request.session['variant'] = 'None'

        carMakeID = request.POST.get('make')
        carModelID = request.POST.get('variant')
        carVariantID = request.POST.get('carVariant')

        # car make filter
        if carMakeID != 'None':
            carMake = CarMakeMode.objects.get(id=carMakeID)
            featuredCars = GeneralInfoModel.objects.filter(
                car__make__make=carMake)

        # car model filter
        if carModelID != 'None':
            carModel = CarModel.objects.get(id=carModelID)
            featuredCars = featuredCars.filter(car__make=carModel)

        # car varitent filter
        if carVariantID != 'None':
            carVariantPost = CarVariantModel.objects.get(id=carVariantID)
            featuredCars = featuredCars.filter(car=carVariantPost)

        # filter objects
        carMake = CarMakeMode.objects.all()
        carModel = CarModel.objects.all()
        carVariant = CarVariantModel.objects.all()

        context = {
            "featuredCars": featuredCars,
            "carMake": carMake,
            "carModel": carModel,
            "carVariant": carVariant,
        }

        return render(request, 'searchfunction/searchResults.html', context)

    context = {
        "featuredCars": featuredCars,
        "carMake": carMake,
        "carModel": carModel,
        "carVariant": carVariant,
    }

    return render(request, 'searchfunction/searchResults.html', context)


# Filter Testing Start

def CarsResultsView(request, id=None, brand=None):
    if id is None and brand is None:
        cars = GeneralInfoModel.objects.all()
        Search = request.session.get('Search')
        refineBrands = CarMakeMode.objects.all()

        if Search == 'Yes':
            brandID = request.session.get('brand')
            modelID = request.session.get('model')
            variantID = request.session.get('variant')

            brand = CarMakeMode.objects.get(id=brandID)
            cars = GeneralInfoModel.objects.filter(car__make__make=brand)

            if modelID != 'None':
                model = CarModel.objects.get(id=modelID)
                cars = cars.filter(car__make=model)

            if variantID != 'None':
                variant = CarVariantModel.objects.get(id=variantID)
                cars = cars.filter(car=variant)

            request.session['Search'] = 'No'

        context = {
            "cars": cars,
            "refineBrands": refineBrands
        }

        return render(request, 'SearchFunc/resultsFunc.html', context)
    else:
        refineBrands = CarMakeMode.objects.all()

        if brand == 1:
            brand = CarMakeMode.objects.get(id=id)
            cars = GeneralInfoModel.objects.filter(car__make__make=brand)

            context = {
                "cars": cars,
                "refineBrands": refineBrands
            }

        else:
            print('body type')

        return render(request, 'SearchFunc/resultsFunc.html', context)


def NewFilterTest(request):
    brand = CarMakeMode.objects.all()

    if request.method == 'POST' and 'filter_testing' in request.POST:
        brandID = request.POST.get('brand')
        modelID = request.POST.get('Model')
        variantID = request.POST.get('Variants')

        if brandID != 'None':
            request.session['Search'] = 'Yes'
            request.session['brand'] = brandID
            request.session['model'] = 'None'
            request.session['variant'] = 'None'

        if modelID != 'None':
            request.session['model'] = modelID
            request.session['variant'] = 'None'

        if variantID != 'None':
            request.session['variant'] = variantID

        return redirect('cars-results')

    context = {
        "brand": brand
    }

    return render(request, 'SearchFunc/filter.html', context)


def BrandSelect(request):
    return render(request, 'partials/brand.html')


def ModelCarView(request):
    if request.method == 'POST':
        brandID = request.POST.get('brand')
        brand = CarMakeMode.objects.get(id=brandID)
        carModels = CarModel.objects.filter(make=brand)

        context = {
            "carModels": carModels
        }

    return render(request, 'partials/modelCar.html', context)


def VariantsCarsView(request):

    if request.method == 'POST':
        ModelID = request.POST.get('Model')
        model = CarModel.objects.get(id=ModelID)
        variants = CarVariantModel.objects.filter(make=model)

        context = {
            "variants": variants
        }

    return render(request, 'partials/whipsVariants.html', context)


# Refine data
def CarsDataView(request):
    if request.method == 'POST':
        brandID = request.POST.get('refineBrand')
        modelID = request.POST.get('refineModel')
        variantID = request.POST.get('Variants')

        if brandID != 'None':
            brand = CarMakeMode.objects.get(id=brandID)
            cars = GeneralInfoModel.objects.filter(car__make__make=brand)
           

        if modelID != 'None':
            model = CarModel.objects.get(id=modelID)
            cars = cars.filter(car__make=model)

        if variantID != 'None':
            variant = CarVariantModel.objects.get(id=variantID)
            cars = cars.filter(car=variant)

        context = {
            "cars": cars
        }

    return render(request, 'SearchFunc/carsData.html', context)


def RefineModelView(request):
    if request.method == 'POST':
        brandID = request.POST.get('refineBrand')
        brand = CarMakeMode.objects.get(id=brandID)
        carModels = CarModel.objects.filter(make=brand)

        context = {
            "carModels": carModels
        }

    return render(request, 'refine/refineModel.html', context)


def RefineVariantView(request):

    if request.method == 'POST':
        modelID = request.POST.get('refineModel')
        model = CarModel.objects.get(id=modelID)
        variants = CarVariantModel.objects.filter(make=model)

        context = {
            "variants": variants
        }

    return render(request, 'refine/refineVariant.html', context)


# Testing Form

def RedirectFormView(request):
    brand = CarMakeMode.objects.all()

    if request.method == 'POST':
        brandID = request.POST.get('refineBrand')
        modelID = request.POST.get('refineModel')
        variantID = request.POST.get('Variants')
        print(brandID)

        return redirect('cars-results')

    context = {
        "brand": brand
    }

    return render(request, 'refine/redirectForm.html', context)
