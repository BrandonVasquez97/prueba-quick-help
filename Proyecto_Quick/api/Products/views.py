from itertools import product
from api.Tokens.views import verificar_token
from api.responses import Error_response, Out_response
from api.models import Products, Bills_Products

def listar(data):
    id = data.get("id", "")
    if id == "":
        productos = list(Products.objects.values())
        if len(productos) > 0:
            return Out_response(False, "Listar productos", productos)
        else:
            return Out_response(False, "No hay productos para listar")
    else:
        productos = list(Products.objects.filter(id=id).values())
        if len(productos) > 0:
            return Out_response(False, "Listar productos", productos)
        else:
            return Out_response(False, "Producto no encontrado")

def crear(data):
    nombre = data.get("name", "")
    descripcion = data.get("description", "")
    atributo = data.get("attribute", "")
    if nombre == "" or descripcion == "" or atributo == "":
        return Out_response(False, "Debes rellenar todos los campos")
    Products.objects.create(name=nombre, description=descripcion, Attribute_4=atributo)
    return Out_response(False, "Producto creado!")

def actualizar(data):
    id = data.get("id", "")
    nombre = data.get("name", "")
    descripcion = data.get("description", "")
    atributo = data.get("attribute", "")
    if id == "":
        return Out_response(False, "Debes proporcionar un ID para actualizar")
    if nombre == "" or descripcion == "" or atributo == "":
        return Out_response(False, "Debes rellenar todos los campos")
    else:
        productos = list(Products.objects.filter(id=id).values())
        if len(productos) > 0:
            producto = Products.objects.get(id=id)
            producto.name = nombre
            producto.description = descripcion
            producto.Attribute_4 = atributo
            producto.save()
            return Out_response(False, "Producto actualizado")
        else:
            return Out_response(False, "Producto no encontrado")

def eliminar(data):
    id = data.get("id", "")
    if id == "":
        return Out_response(False, "Debes proporcionar un ID para eliminar")
    else:
        factura_producto = list(Bills_Products.objects.filter(product_id_id=id).values())
        if len(factura_producto) > 0:
            return Out_response(False, "No puedes borrar este producto, hay una factura asociada con este")
        productos = list(Products.objects.filter(id=id).values())
        if len(productos) > 0:
            Products.objects.filter(id=id).delete()
            return Out_response(False, "Producto eliminado")
        else:
            return Out_response(False, "Producto no encontado")

def gestion(request):
    opciones = ['listar', "crear", "actualizar", "eliminar"]
    funciones = [listar, crear, actualizar, eliminar]
    op = request.get('op')

    token = request.get('token', None)

    if op in opciones:
        if (op != "login"):
            if not token:
                return Out_response(True, "Data invalida", {"token": token})
            if verificar_token(token) is not True:
                return Error_response(True, "Token invalido", 401)

        resp = funciones[opciones.index(op)](
            request) 
    else:
        resp = Out_response(True, "OP invalida")
    return resp