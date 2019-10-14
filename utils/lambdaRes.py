import boto3


def create_function():
    client = boto3.client('lambda')
    response = client.create_function(
    FunctionName='string',
    Runtime='nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'java8'|'python2.7'|'python3.6'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x',
    Role='string',
    Handler='string',
    Code={
        'ZipFile': b'bytes',
        'S3Bucket': 'string',
        'S3Key': 'string',
        'S3ObjectVersion': 'string'
    },
    Description='string',
    Timeout=123,
    MemorySize=123,
    Publish=True|False,
    DeadLetterConfig={
        'TargetArn': 'string'
    },
    Environment={
        'Variables': {
            'string': 'string'
        }
    },
    KMSKeyArn='string',
    TracingConfig={
        'Mode': 'Active'|'PassThrough'
    },
    Tags={
        'string': 'string'
    }
)
    

