"""
-*- coding: utf-8 -*-
"""
import json
import datetime
import boto3

wordlist = ['accord', 'fisc', 'moteur', 'grâce']

def lambda_handler(event, context):
	#Read file from s3
    s3 = boto3.client("s3")
    if event:
        file_obj = event["Records"][0]
        bucketname = str(file_obj['s3']['bucket']['name'])
        filename = str(file_obj['s3']['object']['key'])
        fileObj = s3.get_object(Bucket=bucketname, Key=filename)
        file_content = fileObj["Body"].read().decode('utf-8')
        #text_read = text.read().decode('utf-8')
        text_lower = file_content.lower()
        text_clean = text_lower.replace(',', ' ')
        #whole words are not compared, so the word "cherche" counts for 1 occurence in the word "recherches" 
        dict_w_o = {}
        for word in wordlist:
            occur = text_clean.count(word)
            dict_w_o[word] = occur
        #create the whole dictionary (python object) in the same dataformat as the dynamodb
        dict_data = {
            "user" : "chrisco",
            "text" : filename,
            "date": datetime.datetime.today().strftime('%Y-%m-%d'),
            "words" : dict_w_o
        }
        print (dict_data)
        #print("Received event: " + json.dumps(event, indent=2))
        client = boto3.resource('dynamodb')
        table = client.Table("dynamod2")
        file = json.dumps(dict_data, indent=2)
        dict_object = json.loads(file)
        print(dict_object)
        table.put_item(Item=dict_object)
     