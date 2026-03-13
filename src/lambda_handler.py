#Main entry point for the Orion-Dispatch Lambda function
import json
import logging

# Set up professional logging - crucial for a TPM to show observability
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    """
    Main entry point for Orion-Dispatch triggers.
    In a real scenario, this would send a message to SQS or SNS.
    """
    try:
        # Log the incoming event for traceability
        logger.info(f"Received dispatch request: {json.dumps(event)}")
        
        # Simulate logic: checking for a 'payload' in the request
        body = event.get('body', {})
        
        if not body:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Empty dispatch payload received'})
            }

        # Success Response
        return {
            'statusCode': 202, # 202 = Accepted (Industry standard for async tasks)
            'body': json.dumps({
                'message': 'Dispatch instruction queued successfully',
                'engine': 'Orion-V1'
            })
        }

    except Exception as e:
        logger.error(f"System Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal Orion Engine Error'})
        }
