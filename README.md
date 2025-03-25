# AWS Event-Driven Data Pipeline

This project demonstrates an event-driven data processing pipeline using AWS services. It simulates real-world data generation, processes the data in real-time using AWS Lambda, and stores the processed data in AWS DynamoDB.

## Overview

- **Data Generation:** Simulated user interactions (e.g., clicks, purchases) are stored in AWS S3.
- **Event Triggering:** AWS EventBridge triggers workflows when new data is uploaded to S3.
- **Data Processing:** AWS Lambda functions process the data in real-time.
- **Data Storage:** Processed data is stored in AWS DynamoDB for further analysis.

## Technologies Used

- **AWS S3:** For storing raw data.
- **AWS EventBridge:** For triggering workflows based on events.
- **AWS Lambda:** For real-time data processing.
- **AWS DynamoDB:** For storing processed data.
- **AWS CloudWatch:** For monitoring and logging.

## Project Structure

- `data-generation/`: Scripts for simulating user interactions.
- `lambda-functions/`: AWS Lambda functions for data processing.
- `dynamodb-schema/`: DynamoDB schema definitions.
- `cloudwatch-config/`: CloudWatch configuration for monitoring.

## Setup Instructions

1. **AWS Account Setup:** Ensure you have an AWS account with necessary permissions.
2. **Environment Variables:** Set up environment variables for AWS credentials.
3. **Deploy Infrastructure:** Use AWS CLI or SDKs to deploy the infrastructure (S3, EventBridge, Lambda, DynamoDB).

## Usage

1. **Run Data Generation Scripts:** Execute Python scripts to simulate data.
2. **Trigger EventBridge:** New data uploads trigger workflows via EventBridge.
3. **Monitor with CloudWatch:** Use CloudWatch to monitor Lambda performance and logs.


