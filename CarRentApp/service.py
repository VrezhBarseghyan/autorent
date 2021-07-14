from django.http import JsonResponse

from .models import *
from django.core import serializers

#
# def add_car (request):
#     if request.method == "POST":
#         brand_str = request.POST.get('brand')
#         brand = CarBrand(name = brand_str)
#         created_brand = brand.save()
#         model_str = request.POST.get('model')
#         model = CarModel(brand = created_brand, name = model_str)
#         model.save()

def get_json_items_data(request):
    # val = serializers.serialize('json', CarModel.objects.filter(brand_name = brand_name))
    val = serializers.serialize('json', CarModel.objects.all())
    return JsonResponse(val)