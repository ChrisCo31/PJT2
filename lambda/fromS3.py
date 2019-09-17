"""
-*- coding: utf-8 -*-
"""
import json
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
        print (dict_w_o)
        #return dict_w_o
        dict_textresult = {}
        dict_textresult[filename] = dict_w_o
        print(dict_textresult)
        return dict_textresult
