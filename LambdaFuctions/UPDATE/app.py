import json
import boto3

# Initialize DynamoDB and EventBridge clients
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('AnimeReviewsDB')
events = boto3.client("events")
BUS = "default"

def lambda_handler(event, context):
    try:
        # Parse the incoming request body
        body = json.loads(event['body'])
        review_id = body['id']
        updated_review_text = body['review']
        
        # Update the review in DynamoDB
        response = table.update_item(
            Key={'id': review_id},
            UpdateExpression="SET review = :review",
            ExpressionAttributeValues={':review': updated_review_text},
            ReturnValues="UPDATED_NEW"
        )
        
        # Send event to EventBridge for tracking the update
        events.put_events(Entries=[{
            "Source": "andos.api",
            "DetailType": "ReviewAction",
            "Detail": json.dumps({
                "action": "update",
                "id": review_id,
                "review": updated_review_text
            }),
            "EventBusName": BUS
        }])

        # Return a success response
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Review updated successfully!'})
        }

    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error updating review'})
        }

