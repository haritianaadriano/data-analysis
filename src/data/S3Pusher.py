import pandas as pd
import numpy as np
import boto3 as bt
import os
from dotenv import load_dotenv
from datetime import datetime

def uploadToS3(data,csvFilePath):
    load_dotenv()
    s3 = bt.resource(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
        aws_secret_access_key=os.getenv('AWS_SECRET_KEY')
    )
    # Convert instant now to string
    current_datetime_string = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')

    filename=data+"-"+current_datetime_string+'.csv'
    s3.Object(os.getenv('BUCKET_NAME'), filename).put(Body=csvFilePath)
