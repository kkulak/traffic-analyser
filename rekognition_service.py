import boto3


def detect_labels_for(image):
    client = boto3.client('rekognition')
    response = client.detect_labels(
        Image={'Bytes': image},
        MinConfidence=0
    )

    return response['Labels']
