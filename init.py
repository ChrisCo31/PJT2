#!/usr/bin/env python3
from utils import s3 
from utils import dynamodb
from utils import apigateway
from utils import lambdaRes

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
    client = boto3.client('lambda')
    FunctionName=config["FUNCTIONL"]
    Runtime= config["RUNTIME"]
    lambdaRes.create_function(
            response = client.create_function(
            FunctionName='FunctionName',
            Runtime='Runtime',
            Role='string',
            Handler='us1',
    )
)
    pass

if __name__ == "__main__":
    main()
    
    
    
   

