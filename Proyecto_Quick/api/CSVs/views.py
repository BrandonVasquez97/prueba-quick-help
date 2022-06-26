from api.Tokens.views import verificar_token
from api.responses import Error_response, Out_response
from api.conn import executeCommit, executeQuerydict
from datetime import datetime
from pytz import timezone
import csv

def generarCSV(data):
    header = ['Documento', 'Nombres', 'Apellidos', 'Facturas']
    query = f"SELECT * FROM api_bills"
    res = executeQuerydict(query)
    if(res == "error"):
        return Out_response(False, "Error consultando facturas del cliente")
    if(len(res) < 1):
        return Out_response(False, "No hay facturas asociadas")
    
    query2 = f"SELECT * FROM api_clients"
    res2 = executeQuerydict(query2)
    if(res2 == "error"):
        return Out_response(False, "Error consultando datos de los clientes")
    if(len(res2) < 1):
        return Out_response(False, "No hay datos de clientes")
    
    data = []
    for i in res2:
        client_id = i["id"]
        query3 = f"SELECT * FROM api_bills WHERE client_id_id = {client_id}"
        res3 = executeQuerydict(query3)
        if(res3 == "error"):
            return Out_response(False, "Error consultando facturas del cliente")
        dato = [i["document"], i["first_name"], i["last_name"], len(res3)]
        data.append(dato)

    
    fmt = '%Y_%m_%d_%H_%M_%S'
    eastern = timezone('America/Bogota')
    loc_dt = datetime.now(eastern)
    fecha = loc_dt.strftime(fmt)
    titulo = "archivo_" + str(fecha) + ".csv"

    with open('./CSV_generados/' + titulo, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)
    return Out_response(False, f"CSV generado en la carpeta CSV_generados con el nombre de: {titulo}")

def cargarCSV(csv_file):
    if not csv_file.name.endswith('.csv'):
        return Out_response(True, "El archivo no es un CSV")
    try:
        file_data = csv_file.read().decode("utf-8")
    except Exception as err:
        return Out_response(True, "Hay un dato no valido en la plantilla del CSV")
    lines = file_data.split("\n")
    registros = len(lines) - 2
    if registros == 0:
        return Out_response(True, "No hay datos para registrar")
    i = 0
    for line in lines:						
        fields = line.split(",")
        if (i == 0):
            print("Cabecera")
        elif (i == len(lines) - 1):
            print("No se tiene en cuenta")
        else:
            if len(fields) < 4:
                linea = i + 1
                return Out_response(True, f"Debes completar los campos para el registro de clientes, fila {linea} incompleta")
        i += 1
    i = 0
    for line in lines:						
        fields = line.split(",")
        if (i == 0):
            print("Cabecera")
        elif (i == len(lines) - 1):
            print("No se tiene en cuenta")
        else:
            document = fields[0]
            first = fields[1]
            last = fields[2]
            email = fields[3]
            query = f"INSERT INTO api_clients (document, first_name, last_name, email) VALUES('{document}', '{first}', '{last}', '{email}')"
            res = executeCommit(query)
            if(res == "error"):
                return Out_response(True, "Error en la query para insercion de cliente")
        i += 1
    return Out_response(False, "Cliente(s) creado(s) satisfactoriamente")

def gestion(request):
    opciones = ['generar']
    funciones = [generarCSV]
    op = request.get('op')

    token = request.get('token', None)

    if op in opciones:
        if (op != "login"):
            if not token:
                return Out_response(True, "Invalid Data", {"token": token})
            if verificar_token(token) is not True:
                return Error_response(True, "Invalid Token", 401)

        resp = funciones[opciones.index(op)](
            request) 
    else:
        resp = Out_response(True, "Invalid Operation")
    return resp