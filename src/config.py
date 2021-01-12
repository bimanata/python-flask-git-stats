"""
All the config of the APP (db URI, API creds, etc)
will be here
"""
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../'))
import urllib
import json
import boto3
from dotenv import load_dotenv

from pathlib import Path  # python3 only
directory = os.path.dirname(os.path.realpath(__file__))

##################### Load Environment Setup #########################
env_path = '.app.env'
load_dotenv(dotenv_path=env_path)
print("Environment File : ",str(env_path))

########################## Load Key Setup #############################
app_port = int(os.getenv('APP_PORT'))

app_port = int(os.getenv('APP_PORT'))

AWS_ACCESS_KEY = str(os.getenv('AWS_ACCESS_KEY'))
AWS_SECRET_KEY = str(os.getenv('AWS_SECRET_KEY'))
S3_BUCKET_NAME = str(os.getenv('S3_BUCKET_NAME'))

s3_client = boto3.client('s3',aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,)
