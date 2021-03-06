import json
import pymysql
import base64
from datetime import datetime
from pytz import timezone
from api.responses import Error_response

#Funcion para INSERT/UPDATE
def executeCommit(query):
    try:
        print("executeCommit", query)
        #Obtiene las credenciales con el SECRET MANAGER
        #credenciales = json.loads(get_secret_db("commit"))
        #Llamado de datos del JSON
        endpoint = "database-aws.cdg2ikq7roav.us-east-2.rds.amazonaws.com"
        db_user = "admin"
        db_pass = "130197bvb97"
        db_name = "quick_api"
        connection = pymysql.connect(
            host=endpoint, user=db_user, password=db_pass, db=db_name, port=3306)
        #Ejecuta la consulta
        cursor = connection.cursor()
        cursor.execute("SET TIME_ZONE='America/Bogota'")
        cursor.execute("SET @@session.time_zone = 'America/Bogota'")
        res = cursor.execute(query)
        res = cursor.lastrowid
        print("resCommit", res)
        connection.commit()

    except Exception as err:
        res = "error"
        print(Error_response(err, "executeCommit - Error interno", 110))
    finally:
        connection.close()
    return res


#Funcion para SELECT
def executeQuery(query):
    try:
        print("executeQuery", query)
        #Obtiene las credenciales con el SECRET MANAGER
        #credenciales = json.loads(get_secret_db("commit"))
        #Llamado de datos del JSON
        endpoint = "database-aws.cdg2ikq7roav.us-east-2.rds.amazonaws.com"
        db_user = "admin"
        db_pass = "130197bvb97"
        db_name = "quick_api"
        db_name = "quick_api"
        connection = pymysql.connect(
            host=endpoint, user=db_user, password=db_pass, db=db_name, port=3306)

        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query)

        rows = cursor.fetchall()
        print("rows =>", rows, "type(rows)", type(rows))

        rows = json.dumps(rows, indent=4, sort_keys=True, default=str)
        # print("json.dumps rows =>", rows, "type(rows)",type(rows))
        rows = json.loads(rows)
        # print("json.loads rows =>", rows, "type(rows)",type(rows))

    except Exception as err:
        rows = "error"
        print(Error_response(err, "executeQuery - Error interno", 111))
    finally:
        connection.close()
    return rows



def executeQuerydict(query):
    try:
        print("executeQuery", query)
        #Obtiene las credenciales con el SECRET MANAGER
        #credenciales = json.loads(get_secret_db("commit"))
        #Llamado de datos del JSON
        endpoint = "database-aws.cdg2ikq7roav.us-east-2.rds.amazonaws.com"
        db_user = "admin"
        db_pass = "130197bvb97"
        db_name = "quick_api"
        connection = pymysql.connect(
            host=endpoint, user=db_user, password=db_pass, db=db_name, port=3306)

        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query)

        rows = cursor.fetchall()
        print("rows =>", rows, "type(rows)", type(rows))

        rows = json.dumps(rows, indent=4, sort_keys=True, default=str)
        # print("json.dumps rows =>", rows, "type(rows)",type(rows))
        rows = json.loads(rows)
        # print("json.loads rows =>", rows, "type(rows)",type(rows))

    except Exception as err:
        rows = "error"
        print(Error_response(err, "executeQuery - Error interno", 111))
    finally:
        connection.close()
    return rows


def getSysdate():
    try:
        # define date format
        fmt = '%Y-%m-%d %H:%M:%S'
        # fmt = '%Y-%m-%d %H:%M:%S %Z%z'
        # define eastern timezone
        eastern = timezone('US/Eastern')
        # naive datetime
        naive_dt = datetime.now()
        # localized datetime
        loc_dt = datetime.now(eastern)
        loc_dt = loc_dt.strftime(fmt)
        print("naive", naive_dt.strftime(fmt))
        print("loc_dt", loc_dt)
    except Exception as err:
        loc_dt = Error_response(err, "getSysdate - Error interno", 112)
    return loc_dt


def getDatetime():
    try:
        # define date format
        fmt = '%Y-%m-%d %H:%M:%S'
        # fmt = '%Y-%m-%d %H:%M:%S %Z%z'
        # define eastern timezone
        eastern = timezone('US/Eastern')
        # naive datetime
        naive_dt = datetime.now()
        # localized datetime
        loc_dt = datetime.now(eastern)
        print("naive", naive_dt.strftime(fmt))
        print("loc_dt", loc_dt)
    except Exception as err:
        loc_dt = Error_response(
            err, "getDatetime - Error interno", 113)
    return loc_dt


def validarFechas(fecha):
    if(fecha == None or fecha == ""):
        fecha = "null"
    else:
        fecha = f"'{fecha}'"

    return fecha