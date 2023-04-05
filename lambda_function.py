import json

def lambda_handler(event, context):
    message = "Hello, GIM! Hello People, What's Going on? free or work on..! Hope everything goes well. We will meet soon"
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
