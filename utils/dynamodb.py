import logging
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

def create_table(table_name, key_schema, attribute_definition, provisioned_throughput={'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1}):
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')

    # Create the DynamoDB table.
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=key_schema,
        AttributeDefinitions=attribute_definition,
        ProvisionedThroughput=provisioned_throughput
    )

    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName=table_name)

    # return out some data about the table.
    return table.item_count
