#!/bin/env python3

import boto3
import logging
from botocore.exceptions import ClientError
import requests


def create_presigned_post(bucket, key,
                          fields=None, conditions=None, expiration=3600):
    # Generate a presigned S3 POST URL
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_post(bucket,
                                                     key,
                                                     Fields=fields,
                                                     Conditions=conditions,
                                                     ExpiresIn=expiration)
        return response
    except ClientError as e:
        logging.error(e)
        return None

#print (create_presigned_post('s3p2.chrisco.fr', 'text.txt'))


def upload_file(bucket, file):
    response = create_presigned_post(bucket, file)
    with open('../data/'+file, 'r') as f:
        files = {'file': (file, f)}
        http_response = requests.post(response['url'], data = response['fields'], files = files)
        print(http_response)
    logging.info(f'File upload HTTP status code: {http_response.status_code}')


upload_file('s3p2.chrisco1970.fr', 'text.txt')
