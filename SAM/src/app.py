import json

print('Loading function')

def lambda_handler(event, context):
    return event['key1']
