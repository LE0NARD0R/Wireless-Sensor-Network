from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.shortcuts import redirect

from medition.models import Meditions
from medition.serializers import MeditionSerializer
from medition import ttn_storage_api    


@csrf_exempt
def meditionApi(request, id=0):
    if request.method == 'GET':
        meditions = Meditions.objects.all()
        meditions_serializer = MeditionSerializer(meditions, many=True)
        return JsonResponse(meditions_serializer.data, safe=False)
    elif request.method == 'POST':
        payload = ttn_storage_api.sensor_pull_storage()
        volt = payload[0]['result']['uplink_message']['decoded_payload']['sensor_volt']
        ph = payload[0]['result']['uplink_message']['decoded_payload']['Ph_act']
        current = payload[0]['result']['uplink_message']['decoded_payload']['current']
        query = Meditions(Ph=ph, Voltage=volt, Current=current)
        query.save()
        if query.is_valid():
            return JsonResponse("Added Successfully", safe=False)



