import json


def hi(event, context):
    body = {
        "message": "Hi! Your function executed successfully!!."
        "",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
