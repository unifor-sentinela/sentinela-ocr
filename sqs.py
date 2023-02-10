import boto3
from ocr import process

queue_name = "sentinela-sqs-bucket-ocr-queue-development"

sqs = boto3.resource("sqs")
s3 = boto3.resource("s3")

queue = sqs.get_queue_by_name(QueueName=queue_name)

def process_message(message_body):
    for record in message_body['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        
        try:
            result = process(bucket, key)
            # TODO: publish this result to ocr-crud queue.
            print(result)
        except:
            print('Error')

if __name__ == "__main__":
    while True:
        messages = queue.receive_messages(MaxNumberOfMessages=1)
        for message in messages:
            process_message(message.body)
            message.delete()