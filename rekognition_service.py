import boto3

def detect_labels():
    client = boto3.client('rekognition')
    response = client.detect_labels(
    	Image={
        	'S3Object': {
            	'Bucket': 'rekognition-samples',
            	'Name': 'crowd.png'
        	}
    	},
    	MinConfidence=0
	)

    return response['Labels']