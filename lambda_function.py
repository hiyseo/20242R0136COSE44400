import boto3
from textblob import TextBlob
import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('reviews-2020320135')
ses = boto3.client('ses')

def lambda_handler(event, context):
    user_name = event['user_name']
    review_text = event['review']
    timestamp = datetime.datetime.now().isoformat()

    # Sentiment Analysis
    polarity = TextBlob(review_text).sentiment.polarity
    '''
    Todo1: Use the Polarity value to determine the sentiment of the review, 
    with the standard set to 0.
    '''
    sentiment = "Positive" if polarity > 0 else "Negative"

    # Save to DynamoDB
    table.put_item(
        Item = {
            "user_name": user_name,
            "review": review_text,
            "sentiment": sentiment,
            "timestamp": timestamp
        }
    )

    # Send Email for Positive Reviews
    if sentiment == "Positive":
        ses.send_email(
            Source="yseo3167@gmail.com",
            Destination={"ToAddresses": ["seo3167@naver.com"]},
            Message={
                "Subject": {"Data": f"Positive Review from {user_name}"},
                "Body": {"Text": {"Data": f"{user_name} wrote: {review_text}"}}
            }
        )

    return {"statusCode": 200, "body": f"Review processed for {user_name}"}
