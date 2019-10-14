<<<<<<< HEAD
import logging
import boto3
from botocore.exceptions import ClientError

def create_api():
    # Get the service resource.
    client = boto3.client('apigateway')
    response = client.create_resource(
        restApiId='string',
        parentId='string',
        pathPart='string'
    )




