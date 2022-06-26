from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .Users.views import gestion as gestionUser
from .Products.views import gestion as gestionProduct
from .Clients.views import gestion as gestionClient
from .Bills.views import gestion as gestionBill
from .CSVs.views import gestion as gestionCSV
from .CSVs.views import cargarCSV
from .Tokens.views import verificar_token
import json

# Create your views here.
#Clase que redirecciona a Products/views.py
class ProductView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body)
        response = gestionProduct(data)
        return JsonResponse(response)

#Clase que redirecciona a Clients/views.py
class ClientView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body)
        response = gestionClient(data)
        return JsonResponse(response)

#Clase que redirecciona a Bills/views.py
class BillView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body)
        response = gestionBill(data)
        return JsonResponse(response)

#Clase que redirecciona a Users/views.py
class UserView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body)
        response = gestionUser(data)
        return JsonResponse(response)

#Clase que redirecciona a CSVs/views.py
class CSView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body)
        response = gestionCSV(data)
        return JsonResponse(response)


#Esta clase es esclusiva para cuando se sube el CSV
class CSVUploadView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        #Verifica el token
        token = request.POST["token"]
        if verificar_token(token) is not True:
            error = True,
            mensaje = "Token invalido"
            response = {
                "error": error,
                "message": mensaje
            }
            return JsonResponse(response)
        
        csv_file = request.FILES["csv_file"]
        response = cargarCSV(csv_file)
        return JsonResponse(response)