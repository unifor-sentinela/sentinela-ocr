import json
import time

def process(bucket, key):
    try:
        data = {
            "filename": key,
            "data": {
                "raw": "",
                "saturation": {
                    "value": 0,
                    "alarm": False
                },
                "heartRate": {
                    "value": 0,
                    "alarm": False
                },
                "respiratoryRate": {
                    "value": 0,
                    "alarm": False
                },
                "temperature": {
                    "value": 0,
                    "alarm": False
                },
                "systolicPressure": {
                    "value": 0,
                    "alarm": False
                },
                "diastolicPressure": {
                    "value": 0,
                    "alarm": False
                }
            }
        }
        time.sleep(3)
        return json.dumps(data)
    except:
        raise