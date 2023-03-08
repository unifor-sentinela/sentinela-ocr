import boto3
import json
from ocr import process

bucket_queue_name = "sentinela-sqs-bucket-ocr-queue-development"
crud_queue_name = "sentinela-sqs-ocr-crud-queue-development"

sqs = boto3.resource(
    service_name='sqs',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='root',
    aws_secret_access_key='root'
    )

bucket_queue = sqs.get_queue_by_name(QueueName=bucket_queue_name)
crud_queue = sqs.get_queue_by_name(QueueName=crud_queue_name)

def process_message(message_body):
    for record in message_body['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        
        try:
            result = process(bucket, key)
            response = crud_queue.send_message(
                MessageBody=result
            )
            
            print(response)
        except:
            print('Error')

if __name__ == "__main__":
    while True:
        messages = bucket_queue.receive_messages(MaxNumberOfMessages=1)
        for message in messages:
            process_message(json.loads(message.body))
            message.delete()