from django.db import models

# Create your models here.


class CarMakeMode(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    make = models.ForeignKey(CarMakeMode, null=True, on_delete=models.CASCADE,
                             blank=True, default=None, related_name='car_make')
    name = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class CarVariantModel(models.Model):
    make = models.ForeignKey(CarModel, null=True, on_delete=models.CASCADE,
                             blank=True, default=None, related_name='car_variant')
    name = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class CategoryModel(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class SafetyFeaturesModel(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class CarFeaturesModel(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class ProvinceModel(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class CityModel(models.Model):
    province = models.ForeignKey(ProvinceModel, null=True, on_delete=models.CASCADE,
                                 blank=True, default=None, related_name='city_province')
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class SuburbModel(models.Model):
    city = models.ForeignKey(CityModel, null=True, on_delete=models.CASCADE,
                             blank=True, default=None, related_name='suburb_city')
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
    





