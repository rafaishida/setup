import json

def handler(event, context):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"results": event["texto"]}),
    }

if __name__ == "__main__":
    pass