
import json
import boto3
import requests  # For making HTTP requests to the Jikan API

events = boto3.client("events")
BUS = "default"

def lambda_handler(event, context):
    try:
        # Get the 'title' parameter from the query string
        title = event.get("queryStringParameters", {}).get("title", "")
        
        # Log the event
        print("GET event:", event)

        # Send event to EventBridge for tracking the 'get' action
        events.put_events(Entries=[{
            "Source": "andos.api",
            "DetailType": "ReviewAction",
            "Detail": json.dumps({"action": "get", "title": title}),
            "EventBusName": BUS
        }])

        # Make a request to the Jikan API to get reviews for the given title
        # Example: Fetching the anime info using the Jikan API
        jikan_url = f"https://api.jikan.moe/v4/anime?q={title}&limit=5"  # Example query
        response = requests.get(jikan_url)
        
        if response.status_code == 200:
            # Extract reviews or anime information from the Jikan API response
            anime_data = response.json()

            # If there is no anime data, return an empty list
            if 'data' not in anime_data:
                return {
                    'statusCode': 404,
                    'body': json.dumps({'message': 'No reviews found for this title'})
                }

            # For simplicity, return the first anime in the response (you can extend this to include reviews)
            anime_reviews = anime_data['data']

            return {
                'statusCode': 200,
                'body': json.dumps({
                    "ok": True,
                    "reviews": anime_reviews,
                    "filter": title
                })
            }
        else:
            # Handle Jikan API errors
            return {
                'statusCode': response.status_code,
                'body': json.dumps({'message': 'Error fetching data from Jikan API'})
            }

    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error processing request'})
        }
