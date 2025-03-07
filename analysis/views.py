import pprint

from django.shortcuts import render
from django.http import HttpResponse
# import requests
from django.views.decorators.csrf import csrf_exempt
import json
from users.models.user import User
from analysis.models import Analysis, AnalysisType
from users.models.analysis import UserAnalysis


# Create your views here.

@csrf_exempt
def post_data(request):
    data = json.loads(request.body)
    for item in data:
        pprint.pprint(item)
        patient = User.objects.get(id=item['patient_id'])
        orders = item['orders']
        for order in orders:
            analysis = Analysis.objects.get(id=order['order_id'])
            for res in order['results']:
                UserAnalysis.objects.create(
                    user=patient,

                    analysis=analysis,
                    expected_result=res['reference_range'],
                    result=res['value']
                )
    return HttpResponse("Hello, world. You're at the analysis index.")
