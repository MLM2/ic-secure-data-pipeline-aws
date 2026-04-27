import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8')
    
    data = json.loads(content)
    
    data['processed'] = True
    
    s3.put_object(
        Bucket='mckeever-ic-processed-data',
        Key=key,
        Body=json.dumps(data)
    )
    
    return {'statusCode': 200}