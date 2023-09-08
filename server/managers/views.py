from django.shortcuts import render, redirect
from .models import *
from vehicle.models import *
import random

# Create your views here.


def CarsView(request):
    myCars = GeneralInfoModel.objects.all()

    context = {
        "myCars": myCars
    }
    return render(request, 'managers/cars.html', context)


def UploadCarView(request):
    carMake = CarMakeMode.objects.all()
    categories = CategoryModel.objects.all().order_by('name')
    safetyFeatures = SafetyFeaturesModel.objects.all().order_by('name')
    province = ProvinceModel.objects.all().order_by('name')
    features_list = request.session.get('feature_data', [])

    # request.session.clear()

    if request.method == 'POST' and 'submit_application' in request.POST:

        # seller informaiton
        saveSellerInfo = SellerInfoModel()
        cityID = request.POST.get('city')
        saveSellerInfo.city = CityModel.objects.get(id=cityID)
        saveSellerInfo.firstName = request.POST.get('firstName')
        saveSellerInfo.lastName = request.POST.get('lastName')
        saveSellerInfo.phone = request.POST.get('phone')
        saveSellerInfo.email = request.POST.get('email')
        saveSellerInfo.save()
        sellerModel = SellerInfoModel.objects.get(id=saveSellerInfo.id)

        #  images
        saveImages = CarImagesModel()
        saveImages.image1 = request.FILES['image1']
        saveImages.image2 = request.FILES['image2']
        saveImages.image3 = request.FILES['image3']
        saveImages.image4 = request.FILES['image4']
        saveImages.save()
        getImagesModel = CarImagesModel.objects.get(id=saveImages.id)

        # Economy
        saveEconomy = EconomyModel()
        saveEconomy.average = request.POST.get('average')
        saveEconomy.urban = request.POST.get('urban')
        saveEconomy.extraUrban = request.POST.get('extraUrban')
        saveEconomy.co2 = request.POST.get('co2')
        saveEconomy.fuelRange = request.POST.get('fuelRange')
        saveEconomy.tankCapacity = request.POST.get('tankCapacity')
        saveEconomy.autoStart = request.POST.get('autoStart')
        saveEconomy.save()
        getEconomyModel = EconomyModel.objects.get(id=saveEconomy.id)

        # car engine
        saveEngine = CarEngineModel()
        saveEngine.powerMax = request.POST.get('powerMax')
        saveEngine.powerrpm = request.POST.get('powerrpm')
        saveEngine.torqueMax = request.POST.get('torqueMax')
        saveEngine.torquerpm = request.POST.get('torquerpm')
        saveEngine.engineSize = request.POST.get('engineSize')
        saveEngine.cylinders = request.POST.get('cylinders')
        saveEngine.charger = request.POST.get('charger')
        saveEngine.enginePosition = request.POST.get('enginePosition')
        saveEngine.gearRatio = request.POST.get('gearRatio')
        saveEngine.gearShift = request.POST.get('gearShift')
        saveEngine.drivenWheels = request.POST.get('drivenWheels')
        saveEngine.paddles = request.POST.get('paddles')
        saveEngine.save()
        engineModel = CarEngineModel.objects.get(id=saveEngine.id)

        # general info
        saveCar = GeneralInfoModel()
        saveCar.referance = random.randrange(0, 1000000)
        carVariantID = request.POST.get('carVariant')
        saveCar.car = CarVariantModel.objects.get(id=carVariantID)
        saveCar.price = request.POST.get('price')
        saveCar.year = request.POST.get('year')
        saveCar.kilometers = request.POST.get('kilometers')
        saveCar.transmission = request.POST.get('transmission')
        saveCar.Fuel = request.POST.get('Fuel')
        saveCar.seller = request.POST.get('seller')
        categoryID = request.POST.get('category')
        saveCar.category = CategoryModel.objects.get(id=categoryID)
        saveCar.color = request.POST.get('color')
        saveCar.description = request.POST.get('description')
        saveCar.engine = engineModel
        saveCar.economy = getEconomyModel
        saveCar.images = getImagesModel
        saveCar.sellerInfo = sellerModel
        saveCar.save()

        # safety
        safety = request.POST.getlist('safety')
        for i in safety:
            safetyModel = SafetyFeaturesModel.objects.get(id=i)
            saveCar.safety.add(safetyModel)

        # Features
        features_list = request.session.get('feature_data', [])
        for data in features_list:
            featureModel = CarFeaturesModel.objects.get(id=data['id'])
            saveCar.features.add(featureModel)

        # Clear session after adding the features
        del request.session['feature_data']
        request.session.save()

        return redirect('car-details', saveCar.id)

    context = {
        "carMake": carMake,
        "categories": categories,
        "safetyFeatures": safetyFeatures,
        "province": province,
        "features_list": features_list

    }
    return render(request, 'managers/upload.html', context)


def CarModelsView(request):
    if request.method == 'POST':
        make = request.POST.get('make')
        carMake = CarMakeMode.objects.get(id=make)
        models = CarModel.objects.filter(make=carMake)
        print('make')

        context = {
            "models": models
        }

    return render(request, 'partials/carModels.html', context)


def CarVariantsView(request):
    if request.method == 'POST':
        variant = request.POST.get('variant')
        models = CarModel.objects.get(id=variant)
        carVariant = CarVariantModel.objects.filter(make=models)

        context = {
            "carVariant": carVariant
        }

    return render(request, 'partials/carVariants.html', context)


def CarFeaturesView(request):
    if request.method == 'POST' and 'feature_filter' in request.POST:
        feature_filter = request.POST.get('feature_filter')
        carFeatures = CarFeaturesModel.objects.filter(
            name__icontains=feature_filter)

        context = {
            "carFeatures": carFeatures
        }

    return render(request, 'partials/featuresPartial.html', context)


def AddFeatureView(request):
    if request.method == 'POST':

        featureID = request.POST.get('featureID')
        selectedFeature = CarFeaturesModel.objects.get(id=featureID)
        features_list = request.session.get('feature_data', [])

        feature_data = {
            'id': selectedFeature.id,
            'name': selectedFeature.name,
        }

        features_list.append(feature_data)

        request.session['feature_data'] = features_list

        features_list = request.session.get('feature_data', [])

        context = {
            "features_list": features_list
        }

    return render(request, 'partials/select_feature.html', context)


def CreateNewFeatureView(request):
    if request.method == 'POST':
        feature_filter = request.POST.get('feature_filter')
        create_feature = CarFeaturesModel()
        create_feature.name = feature_filter
        create_feature.save()

        features_list = request.session.get('feature_data', [])

        feature_data = {
            'id': create_feature.id,
            'name': create_feature.name,
        }

        features_list.append(feature_data)

        request.session['feature_data'] = features_list

        features_list = request.session.get('feature_data', [])

        context = {
            "features_list": features_list
        }

    return render(request, 'partials/select_feature.html', context)


def CityFilterView(request):
    if request.method == 'POST':
        provinceID = request.POST.get('province')
        province = ProvinceModel.objects.get(id=provinceID)
        cities = CityModel.objects.filter(province=province)

        context = {
            "cities": cities
        }

    return render(request, 'formData/location.html', context)


# Car price
def CarPriceView(request):
    if request.method == 'POST':
        print('price')
    return render(request, 'partials/pricePartial.html')
