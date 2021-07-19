import cv2
import paho.mqtt.client as mqtt

client=mqtt.Client()
client.connect('broker.hivemq.com',1883)
print('Broker Connected')

client.subscribe('bits/emotion')
print('Client Subscribed')

def notification(client,userdata,msg):
 t=msg.payload
 t=t.decode('utf-8')
 print(t)
 if (t.lower()=='happy'):
  image=cv2.imread('happy.jpg')
  cv2.imshow('Photo Frame', image)
  cv2.waitKey(0) 
  #closing all open windows 
  cv2.destroyAllWindows() 
 elif (t.lower()=='sad'):
  image=cv2.imread('sad.jpg')
  cv2.imshow('Photo Frame', image)
  cv2.waitKey(0) 
  #closing all open windows 
  cv2.destroyAllWindows() 
 elif (t.lower()=='angry'):
  image=cv2.imread('anger.jpg')
  cv2.imshow('Photo Frame', image)
  cv2.waitKey(0) 
  #closing all open windows 
  cv2.destroyAllWindows() 
 elif(t.lower()=='surprised'):
  image=cv2.imread('surprise.jpg')
  cv2.imshow('Photo Frame', image)
  cv2.waitKey(0) 
  #closing all open windows 
  cv2.destroyAllWindows() 
 elif(t.lower()=='disgust'):
  image=cv2.imread('disgust.jpg')
  cv2.imshow('Photo Frame', image)
  cv2.waitKey(0) 
  #closing all open windows 
  cv2.destroyAllWindows() 
 else:
  image=cv2.imread('neutral.png')
  cv2.imshow('Photo Frame', image)
  cv2.waitKey(0) 
  #closing all open windows 
  cv2.destroyAllWindows() 

client.on_message=notification
client.loop_forever()
