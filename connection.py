import boto3
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

class Connection:
    def __init__(self):

        #print(os.environ)

        self.firehose = boto3.client(
            'firehose',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
            aws_secret_access_key=os.getenv('AWS_SECRET_KEY'),
            aws_session_token=os.getenv('AWS_SESSION_TOKEN'),
            region_name=os.getenv('AWS_REGION')
        )
