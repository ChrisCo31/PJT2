#!/usr/bin/env python3
from utils import s3 

def main():

    bucket_name = "s3p2.chrisco.fr"
    region = "eu-west-1"

    s3.create_bucket(bucket_name, region)

    pass

if __name__ == "__main__":
    main()