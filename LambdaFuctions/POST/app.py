import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('AnimeReviewsDB')
events = boto3.client("events")
BUS = "default"

def lambda_handler(event, context):
    try:
        # Log the incoming event
        print("Received event:", json.dumps(event))

        body = json.loads(event['body'])
        review_id = body['id']
        review_text = body['review']

        # Add new review to DynamoDB
        print(f"Adding review with id: {review_id} and review text: {review_text}")
        response = table.put_item(
            Item={
                'id': review_id,  # Unique review ID
                'review': review_text,  # Review content
                'isDeleted': False  # Flag to indicate review is not deleted
            }
        )

        # Log the response from DynamoDB
        print("DynamoDB response:", response)

        # Send event to EventBridge for tracking the creation
        events.put_events(Entries=[{
            "Source": "andos.api",
            "DetailType": "ReviewAction",
            "Detail": json.dumps({
                "action": "create",
                "id": review_id,
                "review": review_text
            }),
            "EventBusName": BUS
        }])

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Review added successfully!'})
        }

    except Exception as e:
        # Log the error
        print("Error:", e)
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error saving review'})
        }

