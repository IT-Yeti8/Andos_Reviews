import json, boto3, os, traceback

TABLE_NAME = os.getenv("TABLE_NAME", "AnimeReviewsDB")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body") or "{}")
        review_id = body["id"]  # <-- if your table has a sort key too, see below

        # Soft delete: mark isDeleted = True, only if item exists
        resp = table.update_item(
            Key={"id": review_id},
            UpdateExpression="SET isDeleted = :t",
            ExpressionAttributeValues={":t": True},
            ConditionExpression="attribute_exists(id)",
            ReturnValues="UPDATED_NEW",
        )

        return {"statusCode": 200, "body": json.dumps({"message": "Review deleted (soft) successfully!"})}

    except table.meta.client.exceptions.ConditionalCheckFailedException:
        # id not found
        return {"statusCode": 404, "body": json.dumps({"message": "Review not found"})}
    except Exception as e:
        print("Delete error:", repr(e))
        print(traceback.format_exc())
        return {"statusCode": 500, "body": json.dumps({"message": "Error deleting review", "error": str(e)})}

