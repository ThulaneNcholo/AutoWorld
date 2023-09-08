from django.contrib import admin
from .models import *

# Register your models here.


class CarMakeAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'id'
    )


admin.site.register(CarMakeMode, CarMakeAdmin)
admin.site.register(CarModel)
admin.site.register(CarVariantModel)
admin.site.register(CategoryModel)
admin.site.register(SafetyFeaturesModel)
admin.site.register(CarFeaturesModel)
admin.site.register(ProvinceModel)
admin.site.register(CityModel)
admin.site.register(SuburbModel)
