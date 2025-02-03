import json

def hello(event, context):
    body = {
        "message": "Hello, Devendra.Never forget to  Work hard and fight back the enemies."
    }

    response = {"statusCode": 200, "body": json.dumps(body)}
    return response

def bye(event, context):
    body = {
        "message": "Bye, Devendra. Work hard and fight back the enemies."
    }

    response = {"statusCode": 200, "body": json.dumps(body)}
    return response

