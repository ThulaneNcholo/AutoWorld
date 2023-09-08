from django.db import models
from managers.models import ProvinceModel
from vehicle.models import GeneralInfoModel

# Create your models here.


class MessageRequestModel(models.Model):
    ref = models.CharField(max_length=200, null=True, blank=True)
    car = models.ForeignKey(GeneralInfoModel, null=True, on_delete=models.CASCADE,
                            blank=True, default=None, related_name='user_car')
    firstName = models.CharField(max_length=200, null=True, blank=True)
    lastName = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    mobile = models.CharField(max_length=200, null=True, blank=True)
    area = models.ForeignKey(ProvinceModel, null=True, on_delete=models.CASCADE,
                             blank=True, default=None, related_name='user_area')
    status = models.CharField(
        max_length=200, null=True, blank=True, default='Pending')
    openStatus = models.CharField(
        max_length=200, null=True, blank=True, default='Pending')
    message = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.firstName
