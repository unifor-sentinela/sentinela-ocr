import boto3

from io import BytesIO
from ocr import process

queue_name = "sentinela-sqs-bucket-ocr-queue-development"

sqs = boto3.resource("sqs")
s3 = boto3.resource("s3")

queue = sqs.get_queue_by_name(QueueName=queue_name)

def process_message(message_body):
    for record in message_body['Records']:
        image_file = BytesIO()

        bucket = record['s3']['bucket']['name']
        filename = record['s3']['object']['key']
        
        s3.Bucket(bucket).download_fileobj(filename, image_file)

        try:
            process(image_file)
        except:
            print('Error')

if __name__ == "__main__":
    while True:
        messages = queue.receive_messages(MaxNumberOfMessages=1)
        for message in messages:
            process_message(message.body)
            message.delete()