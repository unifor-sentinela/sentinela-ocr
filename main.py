import boto3
from ocr import process

bucket_queue = "sentinela-sqs-bucket-ocr-queue-development"
crud_queue = "sentinela-sqs-crud-ocr-queue-development"

sqs = boto3.resource("sqs")
s3 = boto3.resource("s3")

queue = sqs.get_queue_by_name(QueueName=bucket_queue)

def process_message(message_body):
    for record in message_body['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        
        try:
            result = process(bucket, key)

            response = queue.send_message(
                QueueUrl=crud_queue,
                MessageBody=result
            )
            
            print(response)
        except:
            print('Error')

if __name__ == "__main__":
    while True:
        messages = queue.receive_messages(MaxNumberOfMessages=1)
        for message in messages:
            process_message(message.body)
            message.delete()