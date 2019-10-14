import boto3
import json


def putDynamodb(file):
    client = boto3.resource('dynamodb')
    table = client.Table("dynamodb")
    table.put_item(Item= file)

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    file = json.dumps(event, indent=2)
    dict_object = json.loads(file)
    putDynamodb(dict_object)

    