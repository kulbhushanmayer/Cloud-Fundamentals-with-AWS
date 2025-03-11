import boto3
from botocore.exceptions import ClientError

def send_email_via_sns(person_name, position_name, topic_arn):
    # Create an SNS client
    sns_client = boto3.client('sns')

    # Subject and Message content
    subject = f"{person_name} applied for {position_name}"
    message = f"Dear Team,\n\n{person_name} has applied for the position of {position_name}.\n\nBest regards,\nYour Recruitment Team"

    # Send the email through SNS
    try:
        response = sns_client.publish(
            TopicArn=topic_arn,  # ARN of the SNS topic that the email will be sent to
            Subject=subject,
            Message=message
        )
        print(f"Email sent successfully. Message ID: {response['MessageId']}")
    except ClientError as e:
        print(f"Error sending email: {e}")

# Example usage
person_name = "John Doe"
position_name = "Software Engineer"
topic_arn = "arn:aws:sns:region:account-id:demo-topic"  # Replace with your SNS topic ARN

send_email_via_sns(person_name, position_name, topic_arn)
