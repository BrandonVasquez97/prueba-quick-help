from api.Tokens.views import verificar_token
from api.responses import Error_response, Out_response
from api.conn import executeCommit, executeQuerydict

def listar(data):
    id = data.get("id", "")
    if id == "":
        query = f"SELECT * FROM api_clients"
        res = executeQuerydict(query)
        if(res == "error"):
            return Out_response(False, "Error en consulta de lista de clientes")
        else:
            if(len(res)>0):
                clientes = []
                for i in res:
                    cliente = {
                        "id": i["id"],
                        "document": i["document"],
                        "first_name": i["first_name"],
                        "last_name": i["last_name"],
                        "email": i["email"]
                    }
                    clientes.append(cliente)
                return Out_response(False, "Lista clientes", clientes)
            else:
                return Out_response(False, "No hay clientes para listar")
    else:
        query = f"SELECT * FROM api_clients WHERE id = {id}"
        res = executeQuerydict(query)
        if(res == "error"):
            return Out_response(False, "Error en consulta del cliente")
        else:
            if(len(res)>0):
                clientes = []
                for i in res:
                    cliente = {
                        "id": i["id"],
                        "document": i["document"],
                        "first_name": i["first_name"],
                        "last_name": i["last_name"],
                        "email": i["email"]
                    }
                    clientes.append(cliente)
                return Out_response(False, "Lista clientes", clientes)
            else:
                return Out_response(False, "Cliente no encontrado")



def crear(data):
    document = data.get("document", "")
    first_name = data.get("first_name", "")
    last_name = data.get("last_name", "")
    email = data.get("email", "")
    if document == "" or first_name == "" or last_name == "" or email == "":
        return Out_response(False, "Debes rellenar todos los campos")
    query = f"INSERT INTO api_clients (document, first_name, last_name, email) VALUES('{document}', '{first_name}', '{last_name}', '{email}')"
    res = executeCommit(query)
    if(res == "error"):
        return Out_response(False, "Error en consulta de crear cliente")
    else:
        id_cliente = res
        resp = {
            "id_client" : id_cliente
        }
        return Out_response(False, "Cliente Creado Exitosamente", resp)

def actualizar(data):
    id = data.get("id", "")
    document = data.get("document", "")
    first_name = data.get("first_name", "")
    last_name = data.get("last_name", "")
    email = data.get("email", "")
    if(id == ""):
        return Out_response(False, "Debes enviar un ID para actualizar")
    if document == "" or first_name == "" or last_name == "" or email == "":
        return Out_response(False, "Debes rellenar todos los campos")
    query2 = f"SELECT * FROM api_clients WHERE id = {id}"
    res2 = executeQuerydict(query2)
    if(res2 == "error"):
        return Out_response(False, "Error en consulta para buscar cliente")
    if(len(res2) < 1):
        return Out_response(False, "Cliente no encontrado")
    query = f"UPDATE api_clients SET document = '{document}', first_name = '{first_name}', last_name = '{last_name}', email = '{email}' WHERE id = {id}"
    res = executeCommit(query)
    if(res == "error"):
        return Out_response(False, "Error en consulta de actualizar cliente")
    else:
        return Out_response(False, "Client Actualizado exitosamente") 


def eliminar(data):
    id = data.get("id", "")
    if(id == ""):
        return Out_response(False, "Debes enviar un ID para borrar cliente")
    query2 = f"SELECT * FROM api_clients WHERE id = {id}"
    res2 = executeQuerydict(query2)
    if(res2 == "error"):
        return Out_response(False, "Error en consulta para buscar cliente")
    if(len(res2) < 1):
        return Out_response(False, "Client not found")
    query3 = f"SELECT * FROM api_bills WHERE client_id_id = {id}"
    res3 = executeQuerydict(query3)
    if(len(res3) > 0):
        return Out_response(False, "No puedes borrar este cliente, hay una factura asociada con el o ella")

    query = f"DELETE FROM api_clients WHERE id = {id}"
    res = executeCommit(query)
    if(res == "error"):
        return Out_response(False, "Error en query para borrar cliente")
    else:
        return Out_response(False, "Cliente borrado exitosamente") 

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