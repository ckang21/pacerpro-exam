import boto3
import logging

def lambda_handler(event, context):
    try:
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        # Connect to ec2 service
        ec2 = boto3.client('ec2')

        # connect to sns as well
        sns = boto3.client('sns')

        # In actual production we wouldn't use hardcoded values
        # wouldn't want sensitive info in the code
        # INSTANCE_ID = os.environ['INSTANCE_ID']
        # SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']

        INSTANCE_ID = 'i-12345'
        SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:12345'

        # Reboot EC2 instance
        ec2.reboot_instances(InstanceIds=[INSTANCE_ID])

        logger.info(f"Restarted EC2 instance: {INSTANCE_ID}")

        # Notification to SNS
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject='EC2 Instance Restarted',
            Message=f'Instance {INSTANCE_ID} was automatically restarted'
        )

        # log again for notfication to sns
        logger.info("SNS notification has been sent")

        return {'statusCode': 200, 'body': 'Done'}
    except Exception as e:
        # If any failure log it and raise
        logger.error(f"Error: {str(e)}")
        raise