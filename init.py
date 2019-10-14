#!/usr/bin/env python3
from utils import s3 
from utils import dynamodb
from utils import apigateway
import json
import boto3
from utils import functions as utility

def main():

    config = utility.loadConfigFile()
    
    bucket_name = config["BUCKET_NAME"]
    region = config["REGION"]
    dbname = config["DYNAMODB"]
   

    #create s3bucket
    s3.create_bucket(bucket_name, region)
    dynamodb = boto3.resource('dynamodb')
    #dynamodb.create_table()
    table = dynamodb.create_table(
    TableName= dbname,
    KeySchema=[
        {
            'AttributeName': 'word',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'occurence',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'word',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'occurence',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
    apigateway = boto3.resource('apigateway')
    apigateway.create_api('MyApi', 'Myapi', 'stack')

    pass

if __name__ == "__main__":
    main()
    
    
    
   

# https://docs.aws.amazon.com/code-samples/latest/catalog/python-apigateway-aws_service-aws_service.py.html
# https://docs.aws.amazon.com/apigateway/api-reference/resource/resources/
# https://docs.aws.amazon.com/cli/latest/reference/apigateway/create-resource.html
# https://docs.aws.amazon.com/en_pv/code-samples/latest/catalog/python-apigateway-aws_service-aws_service.py.html
#  Deploying and Configuring Lambda Functions for Our API Using the AWS Console 
# https://github.com/cleesmith/boto3_test
# https://github.com/linuxacademy/content-lambda-boto3/tree/master/DynamoDB