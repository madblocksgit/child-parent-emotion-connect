import boto3
import json
import paho.mqtt.client as mqtt

mqtt_client=mqtt.Client()

confi=0
status='Sad'

def emotion_recognizer(a, REGION='eu-west-1', ACCESS_ID='YOUR_ACCESS_KEY_AWS', ACCESS_KEY='ACCESS_KEY_SECRET_AWS'):
    global confi, status
    sourceFile='demo.jpg'
    bucket='bucket'
    client=boto3.client('rekognition',region_name=REGION,aws_access_key_id=ACCESS_ID,
         aws_secret_access_key= ACCESS_KEY)
    imageSource=open(sourceFile,'rb')
    response = client.detect_faces(
        Image={'Bytes': imageSource.read()},Attributes=['ALL'])

    print('Detected faces for ' + sourceFile)    
    for faceDetail in response['FaceDetails']:
        for emotion in faceDetail['Emotions']:
         #print (emotion)
         dummy=emotion['Confidence']
         if(dummy>confi):
           confi=dummy
           status=emotion['Type']
        print (confi, status)
        mqtt_client.connect('broker.hivemq.com',1883)
        print('Sending notification to parent')
        mqtt_client.publish('bits/emotion', status)
        #print(json.dumps(faceDetail, indent=4, sort_keys=True))
