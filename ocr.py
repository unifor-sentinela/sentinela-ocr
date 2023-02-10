from io import BytesIO
import json

def process(image: BytesIO):
    try:
        placeholder = {
            "foo": "bar",
        } 
        result = json.dumps(placeholder)
        return result
    except:
        raise