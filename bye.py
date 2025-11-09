import json


def bye(event, context):
    body = {
        "message": "Bye!!"
        "",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
