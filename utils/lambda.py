import boto3


def create_lambda_resource():
    client = boto3.client('lambda')
    