from api.Tokens.views import verificar_token
from api.responses import Error_response, Out_response
from api.conn import executeCommit, executeQuerydict

def listar(data):
    id = data.get("id", "")
    if id == "":
        query = f"SELECT * FROM api_bills AS A INNER JOIN api_bills_products AS B ON A.id = B.bill_id_id"
        res = executeQuerydict(query)
        if(res == "error"):
            return Out_response(False, "Error en consulta para listar facturas")
        else:
            if(len(res)>0):
                facturas = []
                for i in res:
                    factura = {
                        "id": i["id"],
                        "company_name": i["company_name"],
                        "nit": i["nit"],
                        "code": i["code"],
                        "client_id": i["client_id_id"],
                        "product_id": i["product_id_id"]
                    }
                    facturas.append(factura)
                return Out_response(False, "Listar facturas", facturas)
            else:
                return Out_response(False, "No hay clientes para listar")
    else:
        query = f"SELECT * FROM api_bills AS A INNER JOIN api_bills_products AS B ON A.id = B.bill_id_id WHERE A.id = {id}"
        res = executeQuerydict(query)
        if(res == "error"):
            return Out_response(False, "Error en consulta para listar la factura")
        else:
            if(len(res)>0):
                facturas = []
                for i in res:
                    factura = {
                        "id": i["id"],
                        "company_name": i["company_name"],
                        "nit": i["nit"],
                        "code": i["code"],
                        "client_id": i["client_id_id"]
                    }
                    facturas.append(factura)
                return Out_response(False, "Listar facturas", facturas)
            else:
                return Out_response(False, "factura no encontrada")



def crear(data):
    company_name = data.get("company_name", "")
    nit = data.get("nit", "")
    code = data.get("code", "")
    client_id = data.get("client_id", "")
    product_id = data.get("product_id", "")
    if company_name == "" or nit == "" or code == "":
        return Out_response(False, "Debes rellenar todos los campos")
    if(client_id == ""):
        return Out_response(False, "Debes enviar una ID de cliente para crear la factura")
    if(product_id == ""):
        return Out_response(False, "Debes enviar una ID de producto para crear la factura")
    q = f"SELECT * FROM api_clients WHERE id = {client_id}"
    r = executeQuerydict(q)
    if(len(r) < 1):
        return Out_response(False, f"No existe ID cliente {client_id}")
    q2 = f"SELECT * FROM api_products WHERE id = {product_id}"
    r2 = executeQuerydict(q2)
    if(len(r2) < 1):
        return Out_response(False, f"No existe ID producto {product_id}")
    query = f"INSERT INTO api_bills (company_name, nit, code, client_id_id) VALUES('{company_name}', '{nit}', '{code}', {client_id})"
    res = executeCommit(query)
    if(res == "error"):
        return Out_response(False, "Error en consulta de crear factura")
    else:
        id_bill = res
        query2 = f"INSERT INTO api_bills_products (bill_id_id, product_id_id) VALUES ({id_bill}, {product_id})"
        res2 = executeCommit(query2)
        if(res2 == "error"):
            return Out_response(False, "Error en consulta al crear factura_producto")
        else:
            resp = {
                "id_bill" : id_bill
            }
            return Out_response(False, "Factura creada exitosamente", resp)

def actualizar(data):
    id = data.get("id", "")
    company_name = data.get("company_name", "")
    nit = data.get("nit", "")
    code = data.get("code", "")
    client_id = data.get("client_id", "")
    product_id = data.get("product_id", "")
    if(id == ""):
        return Out_response(False, "Debes enviar un ID de la factura para actualizarla")
    if company_name == "" or nit == "" or code == "":
        return Out_response(False, "Debes rellenar todos los campos")
    if(client_id == ""):
        return Out_response(False, "Debes enviar una ID de cliente para actualizar la factura")
    if(product_id == ""):
        return Out_response(False, "Debes enviar una ID de producto para actualizar la factura")
    q = f"SELECT * FROM api_clients WHERE id = {client_id}"
    r = executeQuerydict(q)
    if(len(r) < 1):
        return Out_response(False, f"No existe ID cliente {client_id}")
    q2 = f"SELECT * FROM api_products WHERE id = {product_id}"
    r2 = executeQuerydict(q2)
    if(len(r2) < 1):
        return Out_response(False, f"No existe ID producto {product_id}")
    query2 = f"SELECT * FROM api_bills WHERE id = {id}"
    res2 = executeQuerydict(query2)
    if(res2 == "error"):
        return Out_response(False, "Error en consulta para buscar factura")
    if(len(res2) < 1):
        return Out_response(False, "Factura no encontrada")
    query = f"UPDATE api_bills SET company_name = '{company_name}', nit = '{nit}', code = '{code}', client_id_id = '{client_id}' WHERE id = {id}"
    res = executeCommit(query)
    if(res == "error"):
        return Out_response(False, "Error en consulta para actualizar factura")
    else:
        query3 = f"SELECT * FROM api_bills_products WHERE bill_id_id = {id}" 
        res3 = executeQuerydict(query3)
        if(res3 == "error"):
            return Out_response(False, "Error en consulta de la tabla factura_producto")
        else:
            id_bill_product = res3[0]["id"]
            query4 = f"UPDATE api_bills_products SET product_id_id = {product_id} WHERE id = {id_bill_product}"
            res4 = executeCommit(query4)
            if(res4 == "error"):
                return Out_response(False, "Error en consulta para actualizar factura_producto")
            else:
                return Out_response(False, "Factura actualizada exitosamente") 


def eliminar(data):
    id = data.get("id", "")
    if(id == ""):
        return Out_response(False, "Debes enviar un ID para borrar factura")
    
    query2 = f"SELECT * FROM api_bills WHERE id = {id}"
    res2 = executeQuerydict(query2)
    if(res2 == "error"):
        return Out_response(False, "Error en consulta de buscar factura")
    if(len(res2) < 1):
        return Out_response(False, "Factura no encontrada")
    query = f"DELETE FROM api_bills_products WHERE bill_id_id = {id}"
    res = executeCommit(query)
    if(res == "error"):
        return Out_response(False, "Error en consulta parar borrar factura_producto")
    else:
        query3 = f"DELETE FROM api_bills WHERE id = {id}"
        res3 = executeCommit(query3)
        if(res3 == "error"):
            return Out_response(False, "Error en consulta para borrar factura")
        else:
            return Out_response(False, "Factura borrada exitosamente")

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