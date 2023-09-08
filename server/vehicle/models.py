from django.db import models
from managers.models import *

# Create your models here.


class SellerInfoModel(models.Model):
    city = models.ForeignKey(CityModel, null=True, on_delete=models.CASCADE,
                             blank=True, default=None, related_name='car_city')
    firstName = models.CharField(max_length=200, null=True, blank=True)
    lastName = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.firstName


class CarImagesModel(models.Model):
    image1 = models.ImageField(
        null=True, blank=True, upload_to='static/images')
    image2 = models.ImageField(
        null=True, blank=True, upload_to='static/images')
    image3 = models.ImageField(
        null=True, blank=True, upload_to='static/images')
    image4 = models.ImageField(
        null=True, blank=True, upload_to='static/images')


class EconomyModel(models.Model):
    average = models.CharField(max_length=200, null=True, blank=True)
    urban = models.CharField(max_length=200, null=True, blank=True)
    extraUrban = models.CharField(max_length=200, null=True, blank=True)
    co2 = models.CharField(max_length=200, null=True, blank=True)
    fuelRange = models.CharField(max_length=200, null=True, blank=True)
    tankCapacity = models.CharField(max_length=200, null=True, blank=True)
    autoStart = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.average


class CarEngineModel(models.Model):
    powerMax = models.CharField(max_length=200, null=True, blank=True)
    powerrpm = models.CharField(max_length=200, null=True, blank=True)
    torqueMax = models.CharField(max_length=200, null=True, blank=True)
    torquerpm = models.CharField(max_length=200, null=True, blank=True)
    engineSize = models.CharField(max_length=200, null=True, blank=True)
    cylinders = models.CharField(max_length=200, null=True, blank=True)
    charger = models.CharField(max_length=200, null=True, blank=True)
    enginePosition = models.CharField(max_length=200, null=True, blank=True)
    gearRatio = models.CharField(max_length=200, null=True, blank=True)
    gearShift = models.CharField(max_length=200, null=True, blank=True)
    drivenWheels = models.CharField(max_length=200, null=True, blank=True)
    paddles = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.powerMax


class GeneralInfoModel(models.Model):
    referance = models.CharField(max_length=200, null=True, blank=True)
    car = models.ForeignKey(CarVariantModel, null=True, on_delete=models.CASCADE,
                            blank=True, default=None, related_name='car')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    year = models.CharField(max_length=200, null=True, blank=True)
    kilometers = models.CharField(max_length=200, null=True, blank=True)
    transmission = models.CharField(max_length=200, null=True, blank=True)
    Fuel = models.CharField(max_length=200, null=True, blank=True)
    seller = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(CategoryModel, null=True, on_delete=models.CASCADE,
                                 blank=True, default=None, related_name='category')
    color = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True)
    engine = models.ForeignKey(CarEngineModel, null=True, on_delete=models.CASCADE,
                               blank=True, default=None, related_name='car_engine')
    economy = models.ForeignKey(EconomyModel, null=True, on_delete=models.CASCADE,
                                blank=True, default=None, related_name='car_economy')
    safety = models.ManyToManyField(
        SafetyFeaturesModel, blank=True, default=None, related_name='car_safety')
    features = models.ManyToManyField(
        CarFeaturesModel, blank=True, default=None, related_name='car_features')
    images = models.ForeignKey(CarImagesModel, null=True, on_delete=models.CASCADE,
                               blank=True, default=None, related_name='car_images')
    sellerInfo = models.ForeignKey(SellerInfoModel, null=True, on_delete=models.CASCADE,
                                   blank=True, default=None, related_name='seller_info')
    status = models.CharField(
        max_length=200, null=True, blank=True, default='Pending')
    payment = models.CharField(
        max_length=200, null=True, blank=True, default='Pending')
    featuredStatus = models.CharField(
        max_length=200, null=True, blank=True, default='Pending')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.referance
