import json

def process(bucket, key):
    try:
        placeholder = {
            bucket: key,
        } 
        result = json.dumps(placeholder)
        return result
    except:
        raise