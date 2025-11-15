# serverless-task-scheduler

Serverless Task Scheduler :

This project implements a fully serverless automation system that runs a scheduled task at regular time intervals using AWS Lambda, Amazon EventBridge, and Amazon SES.
The system is deployed using AWS SAM (Serverless Application Model) and logs all executions in CloudWatch Logs.

Overview :

This application automatically triggers a Lambda function based on a cron schedule. The function sends an email notification through Amazon SES.
The project demonstrates the use of serverless architecture to build automated, scalable, and cost-efficient workflows.

Architecture :

EventBridge (Cron Schedule)
          ->
     AWS Lambda
          ->
     Amazon SES
          ->
      Email Inbox


Project Structure :
serverless-task-scheduler/
│
├── hello_world/
│   ├── app.py
│   ├── requirements.txt
│   └── __init__.py
│
├── template.yaml
├── samconfig.toml
├── tests/
└── .aws-sam/   (auto-generated)


How It Works :

EventBridge triggers Lambda based on the cron expression.
Lambda reads sender and receiver emails from environment variables.
Lambda sends an email using Amazon SES.
Execution logs are stored in CloudWatch Logs.


Cron Expression Used (This runs the Lambda function every 1 minute.) :

cron(* * * * ? *)

AWS Services Used :

AWS Lambda
Amazon EventBridge (Cron Scheduler)
Amazon SES
Amazon CloudWatch Logs
AWS IAM
AWS SAM / CloudFormation


After deployment, AWS SAM creates all required resources including Lambda, the schedule rule, and permissions.

Future Enhancements :

HTML-based email templates
Customizable schedules
Multi-user notifications
Support for SMS/AWS SNS
Dashboard for monitoring executions

Author :
Aditya Ayan Singh
