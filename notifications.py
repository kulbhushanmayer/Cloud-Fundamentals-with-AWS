# notification.py

import boto3
from botocore.exceptions import ClientError
import os

def send_email_via_sns(person_name, position_name, topic_arn):
    # Get the region from the environment variable 'AWS_REGION', default to 'us-east-1' if not set
    region = os.getenv('AWS_REGION', 'us-east-1')  # 'us-east-1' is the default region if AWS_REGION is not set
    
    # Initialize the SNS client with the region
    sns_client = boto3.client('sns', region_name=region)

    subject = f"{person_name} applied for {position_name}"
    message = f"Dear Team,\n\n{person_name} has applied for the position of {position_name}.\n\nBest regards,\nYour Recruitment Team"

    try:
        response = sns_client.publish(
            TopicArn=topic_arn,  # ARN of the SNS topic
            Subject=subject,
            Message=message
        )
        print(f"Email sent successfully. Message ID: {response['MessageId']}")
    except ClientError as e:
        print(f"Error sending email: {e}")
