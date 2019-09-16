import boto3

def create_api(restApiId, parentId, pathPart):
    client = boto3.client('apigateway')

    response = client.create_resource(
    restApiId='string',
    parentId='string',
    pathPart='string'
)
   