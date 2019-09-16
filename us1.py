import logging
import boto3
from botocore.exceptions import ClientError
from utils import functions as utility
from utils import s3 
from utils import dynamodb

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


config = utility.loadConfigFile()
    
bucket_name = config["BUCKET_NAME"]
region = config["REGION"]
dbname = config["DYNAMODB"]
key_name = 'text.txt'
file_name = "data/" + key_name
s3.upload_file(file_name, bucket_name, key_name)
