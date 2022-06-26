import jwt
import api.conn as conn
from datetime import datetime, timedelta
from api.responses import Error_response, Out_response

KEY_SECRET = "MY_SUPER_SECRET_KEY"

def crearTK(data):
    try:
        token = data.get("token")
        activo = data.get("activo")
        fecha_venc = data.get("fecha_venc")
        usuario_id = data.get("usuario_id")
        query = f"INSERT INTO api_tokens (token, active, expiry_date, user_id_id) VALUES ('{token}', {activo}, '{fecha_venc}', {usuario_id})"
        res = conn.executeCommit(query)
        if(res != "error"):
            print("insertados todos los tokens", res)
    except Exception as err:
        res = "error"
        print(Out_response(True, "Error creando token", err))
    return res


def generar_fecha_vencimiento(dias=0, horas=0, minutos=0, segundos=0):
    fecha_actual = datetime.now()
    tiempo_vencimiento = timedelta(
        days=dias, hours=horas, minutes=minutos, seconds=segundos)
    print("fecha_actual", fecha_actual)
    print("tiempo_vencimiento", tiempo_vencimiento)
    fecha_vencimiento = datetime.timestamp(fecha_actual + tiempo_vencimiento)
    print("fecha_vencimiento", fecha_vencimiento)
    return Out_response(datos=fecha_vencimiento)


def generar_token(user, passw, mod):
    try:
        if(mod == "usuarios"):
            fecha_vencimiento = generar_fecha_vencimiento(dias=1)["data"]

        payload = {"exp": fecha_vencimiento,
                   "user_id": user, "user_pass": passw}
        token = jwt.encode(payload, KEY_SECRET, algorithm="HS256")
        res = {
            "token": token,
            "fecha_venc": fecha_vencimiento
        }
    except Exception as err:
        res = "error"
        print(Out_response(True, "Error generando token", err))
    return res


def desactivar_token(todos=True, user_id=None):
    try:
        res = "error"
        if todos:
            query = "UPDATE api_tokens SET active=0 WHERE (expiry_date < sysdate() and active=1)"
            res = conn.executeCommit(query)
            if(res != "error"):
                print("actualizados todos los tokens", res)

        else:
            query = f"UPDATE api_tokens SET active=0 WHERE user_id_id='{user_id}' AND active=1"
            res = conn.executeCommit(query)
            if(res != "error"):
                print("actualizados token del usuario", res)

        return res
    except Exception as err:
        return Out_response(True, "Error desactivando token", err)


def getTokenUser(token):
    try:
        query = f"SELECT user_id_id FROM api_tokens WHERE (active=1 AND token='{token}')"
        res = conn.executeQuery(query)
        resp = res[0]["user_id_id"]
    except Exception as err:
        resp = "error"
        print(Out_response(True, "Error ejecutando getTokenUser", err))
    return resp



def verificar_token(token, mod=""):
    try:
        print("token =>", token)
        q = f"SELECT * FROM api_tokens WHERE token='{token}'"
        res = conn.executeQuery(q)
        if(res != "error"):
            if(len(res) > 0):
                activo = res[0]["active"]
                if(activo == 1):
                    token_verif = jwt.decode(
                        token, KEY_SECRET, algorithms="HS256")
                    if token_verif:
                        print("token válido")
                        resp = True
                    else:
                        print(Out_response(
                            True, "Token Inválido", {"token": token}))
                        resp = False
                else:
                    print(Out_response(
                        True, "Token inactivo", {"token": token}))
                    resp = False
            else:
                print(Out_response(
                    True, "Token no encontrado", {"token": token}))
                resp = False
        else:
            print(Out_response(
                True, "Error consultando el token", {"token": token}))
            resp = False
    except Exception as err:
        return Error_response(err, "Token inválido", 100)
    return resp