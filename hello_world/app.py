import boto3
import os

ses = boto3.client("ses")

def lambda_handler(event, context):
    response = ses.send_email(
        Source=os.environ["SOURCE_EMAIL"],
        Destination={"ToAddresses": [os.environ["TARGET_EMAIL"]]},
        Message={
            "Subject": {"Data": "Scheduled Task Notification"},
            "Body": {"Text": {"Data": "Your scheduled task has run successfully!"}}
        },
    )
    return {"message": "Email sent", "response": response}