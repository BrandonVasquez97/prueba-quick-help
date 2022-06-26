def Out_response(error=False, mensaje="OK", datos=None):
    res = {
        "error": error,
        "message": mensaje,
        "data": datos,
    }
    return res


def Error_response(err, mensaje, codigo_error=None):
    res = {
        "error": True,
        "message": mensaje,
        "data": {
            "Code": codigo_error,
            "Error message": err
        }
    }
    return res