import json

def lambda_handler(event, context):
    message = "Hello, GIM! Hello People"
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
