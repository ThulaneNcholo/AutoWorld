from django.shortcuts import render, redirect
from managers.models import *
from vehicle.models import *
from news.models import *
from leads.models import *
from django.db.models.functions import Random

from django.db.models import Q, Count
from django.db.models import Max, Min


# Create your views here.


def IndexView(request):
    carBrands = CarMakeMode.objects.all().order_by('name')
    featuredCars = GeneralInfoModel.objects.all().order_by(Random())[:8]
    bodyType = CategoryModel.objects.all().order_by('name')
    latestNews = LatestNewsModel.objects.all()
    carMake = CarMakeMode.objects.all()
    carsCount = GeneralInfoModel.objects.all()
    # carsCount = GeneralInfoModel.objects.filter(make=carMake).count()
    showSubmit = 'No'

    # carMakes = CarMakeMode.objects.annotate(cars_count=Subquery(
    #     GeneralInfoModel.objects.filter(make=OuterRef('pk')).values(
    #         'make').annotate(count=Count('id')).values('count')
    # ))

    # cars = CarMakeMode.objects.annotate(carsCount = GeneralInfoModel.objects.filter(car__make__make=carMake).count())
    # for i in cars:
    #     print(cars)

    # for i in carMake:
    #     cars = GeneralInfoModel.objects.filter(car__make__make=i.id)
    #     carMake = CarMakeMode.objects.annotate(carsCount = Count(cars))
    #     cars = CarMakeMode.objects.annotate(carsCount = GeneralInfoModel.objects.filter(car__make__make=i.id).count())
    #     print(cars.carsCount)

    # Retrieve the highest and lowest totals
    highest = GeneralInfoModel.objects.aggregate(
        highest_total=Max('price'))['highest_total']
    lowest_total = GeneralInfoModel.objects.aggregate(
        lowest_total=Min('price'))['lowest_total']

    highest_total = int(highest)

    # range start
    start = 0
    end = highest_total
    step = 100000

    ranges = [(i, min(i + step, end)) for i in range(start, end, step)]

    rangesList = []

    for r in ranges:
        car_count = GeneralInfoModel.objects.filter(
            price__gte=r[0], price__lt=r[1]).count()
        rangeValue = r
        start, end = r
        start = int(start)
        end = int(end)

        rangeCount = car_count
        range_dict = {
            'range': rangeValue,
            'count': rangeCount,
            'start': start,
            'end': end
        }
        rangesList.append(range_dict)

    # New Car Search View
    make = CarMakeMode.objects.all()

    if request.method == 'POST' and 'submit_search' in request.POST:
        newVariant = request.POST.get('newVariant')
        request.session['variant'] = newVariant
        return redirect('new-car-results')

    context = {
        "carBrands":  carBrands,
        "featuredCars": featuredCars,
        "bodyType": bodyType,
        "latestNews": latestNews,
        "carMake": carMake,
        "showSubmit": showSubmit,
        'ranges': ranges,
        "rangesList": rangesList,
        "carsCount": carsCount,
        # new context
        "make": make

    }
    return render(request, 'client/index.html', context)


def MainSubmitBntView(request):
    showSubmit = 'No'

    if request.method == 'POST':
        showSubmit = 'Yes'

    context = {
        "showSubmit": showSubmit
    }
    return render(request, 'mainSearch/submitBtns.html', context)


def AccountView(request):
    leadsCount = MessageRequestModel.objects.filter(
        openStatus='Pending').count()

    context = {
        "leadsCount": leadsCount
    }
    return render(request, 'account/account.html', context)


def SearchResultsView(request):
    featuredCars = GeneralInfoModel.objects.all()

    if request.method == 'POST' and 'main_search' in request.POST:
        carMakeID = request.POST.get('make')
        carModelID = request.POST.get('variant')
        carVariantID = request.POST.get('carVariant')
        # price = request.POST.get('price')
        newprice = request.POST.get('newprice')

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
            carVariant = CarVariantModel.objects.get(id=carVariantID)
            featuredCars = featuredCars.filter(car=carVariant)

        # price Filter
        if newprice != 'None':
            # range_string = price
            # start, end = range_string.split('-')
            # start = int(start)
            # end = int(end)

            # Remove parentheses and any other unwanted characters
            newprice = newprice.replace(
                '(', '').replace(')', '').replace(' ', '')

            start, end = newprice.split(',')

            start = int(start)
            end = int(end)

            featuredCars = GeneralInfoModel.objects.filter(
                price__gte=start, price__lte=end)

    if request.method == 'POST' and 'submit_filter' in request.POST:
        price = request.POST.get('price')
        Year = request.POST.get('Year')
        mileage = request.POST.get('mileage')
        recent = request.POST.get('recent')
        transmission = request.POST.get('transmission')
        fuel = request.POST.get('fuel')
        body = request.POST.get('body')
        seller = request.POST.get('seller')
        print(price)
        print(Year)
        print(mileage)
        print(recent)
        print(transmission)
        print(fuel)
        print(body)
        print(seller)
        return redirect('search-results')

    context = {
        "featuredCars": featuredCars
    }

    return render(request, 'client/search_reqults.html', context)


def ListCarView(request):
    return render(request, 'client/listCar.html')


def InsuranceView(request):
    return render(request, 'client/insurance.html')
