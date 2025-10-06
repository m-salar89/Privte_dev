import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dump("zum testen der Änderungen an durch workflow")
    }
