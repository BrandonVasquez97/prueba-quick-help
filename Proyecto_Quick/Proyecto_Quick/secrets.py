import boto3
import base64
from botocore.exceptions import ClientError
import json


def get_secret_db():
    secret_name = "credenciales_db"
    region_name = "us-east-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    # In this sample we only handle the specific exceptions for the 'GetSecretValue' API.
    # See https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
    # We rethrow the exception by default.

    
    get_secret_value_response = client.get_secret_value(
        SecretId=secret_name
    )
    
        # Decrypts secret using the associated KMS key.
        # Depending on whether the secret is a string or binary, one of these fields will be populated.
    if 'SecretString' in get_secret_value_response:
        secret = get_secret_value_response['SecretString']
    else:
        secret = base64.b64decode(get_secret_value_response['SecretBinary'])
    
    return secret


cred = json.loads(get_secret_db())
HOST = cred["endpoint"]
USER = cred["user"]
PASS = cred["password"]