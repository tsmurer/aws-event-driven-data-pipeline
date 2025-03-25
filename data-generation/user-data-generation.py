import json
import random
import time
import boto3
import os

from dotenv import load_dotenv

load_dotenv()  # Loads environment variables from .env

# Now you can access your credentials like this:
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_DEFAULT_REGION = os.getenv('AWS_DEFAULT_REGION')

# AWS S3 Bucket Name
BUCKET_NAME = 'user-interaction-simulated-data'

# AWS S3 Client
s3 = boto3.client('s3')

def generate_click_data():
    """Simulate a click event."""
    click_data = {
        'event_type': 'click',
        'user_id': random.randint(1, 100),
        'product_id': random.randint(1, 50),
        'timestamp': int(time.time())
    }
    return click_data

def generate_purchase_data():
    """Simulate a purchase event."""
    purchase_data = {
        'event_type': 'purchase',
        'user_id': random.randint(1, 100),
        'product_id': random.randint(1, 50),
        'amount': round(random.uniform(1.0, 100.0), 2),
        'timestamp': int(time.time())
    }
    return purchase_data

def upload_data_to_s3(data, filename):
    """Upload data to S3."""
    s3.put_object(Body=json.dumps(data), Bucket=BUCKET_NAME, Key=filename)

def main():
    for _ in range(10):  # Simulate 10 events
        if random.random() < 0.7:  # 70% chance of a click
            data = generate_click_data()
            filename = f"click-{int(time.time())}.json"
        else:  # 30% chance of a purchase
            data = generate_purchase_data()
            filename = f"purchase-{int(time.time())}.json"
        
        upload_data_to_s3(data, filename)
        print(f"Uploaded {filename} to S3")
        time.sleep(1)  # Wait 1 second before generating the next event

if __name__ == "__main__":
    main()
