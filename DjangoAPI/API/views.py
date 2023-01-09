from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json

@csrf_exempt
def fullName(request):
    if (request.method=="POST"):
        request_data=json.loads(request.body)
        Name = request_data['name']
        LastName= request_data['lastname']
        fullName = f"Your name is {Name} {LastName}"
        return JsonResponse ({"Answer":fullName})
    else:
        return HttpResponse("Method Not Allowed")   