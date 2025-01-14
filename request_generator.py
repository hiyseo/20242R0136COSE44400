import json
import requests
import random
from datetime import datetime, timedelta

# API Gateway Endpoint (Replace with your actual endpoint)
api_url = "https://oospzpicp3.execute-api.us-east-1.amazonaws.com/prod/reviews"


# Sample review templates
positive_reviews = [
    "This product is fantastic! Highly recommend it.",
    "Absolutely love it! Worth every penny.",
    "Great quality and excellent value.",
    "Exceeded my expectations. Would buy again!"
]

negative_reviews = [
    "Terrible experience. Not worth the money.",
    "Product arrived broken and unusable.",
    "Very poor quality. Do not recommend.",
    "Disappointed. Will not buy again."
]

# Random user name generator
def generate_random_name():
    first_names = [
        "Alice", "Bob", "Charlie", "Dave", "Eve", 
        "Frank", "Grace", "Hannah", "Ivy", "Jack", 
        "Karen", "Leo", "Mona", "Nina", "Oscar", 
        "Paul", "Quinn", "Rachel", "Sam", "Tina"
    ]

    last_names = [
        "Smith", "Johnson", "Brown", "Taylor", "Anderson", 
        "Thomas", "Jackson", "White", "Harris", "Martin", 
        "Thompson", "Garcia", "Martinez", "Robinson", "Clark", 
        "Rodriguez", "Lewis", "Lee", "Walker", "Hall"
    ]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Random review generator
def generate_random_review():
    sentiment = random.choice(["positive", "negative"])
    if sentiment == "positive":
        review = random.choice(positive_reviews)
    else:
        review = random.choice(negative_reviews)

    return {
        "user_name": generate_random_name(),
        "review": review,
        "timestamp": (datetime.now() - timedelta(minutes=random.randint(0, 1000))).isoformat()
    }

# Send random reviews to the API Gateway
def send_random_reviews(num_reviews):
    for _ in range(num_reviews):
        review_data = generate_random_review()
        response = requests.post(api_url, json=review_data)
        print(f"Sent: {review_data}")
        print(f"Response: {response.status_code}, {response.json()}")

# Generate and send 20 random reviews
send_random_reviews(20)
