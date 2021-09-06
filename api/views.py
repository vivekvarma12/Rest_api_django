from rest_framework.decorators import api_view
from django.http import JsonResponse
import json

# Create your views here.
@api_view(['POST'])
def IdealWeight(height):
    try:
        h = json.loads(height.body)
        w = str(h*10)
        return JsonResponse("Ideal Weight Should be :"+w+" Kg", safe=False)
    except ValueError as v:
        return JsonResponse(v.args[0].status.HTTP_400_BAD_REQUEST)
