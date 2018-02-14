# -*- coding: utf-8 -*
from webwhatsapi import WhatsAPIDriver as wd
# import pdb
import cv2
import numpy as np
import sys
from multiprocessing import Pool
import time

def sendHeader(contact):
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    # image = cv2.imread('PassportPhoto.jpg')

    ndim = len(image.shape)
    shape = np.asarray(image.shape)
    
    message="\_|__"
    message = message+str(ndim)+" "
    for i in range(ndim):
        message = message+str(shape[i])+' '
        
    contact.send_message(message)
    del(camera)
    
def receiveHeader(contact):
    message = unicode("?????")
    
    while message[0:5] != unicode("\_|__"):
        chat = contact.driver.wapi_functions.getAllMessagesInChat(contact.id, 0, 0)
        message = chat[len(chat)-1]["content"]
        time.sleep(0.1)
    
    message = message[5:].split(' ')
    
    ndim = int(message[0])
    
    if ndim >= 1:
        x = np.zeros((1, ndim))
        for i in range(ndim):
            x[i] = int(message[i+1])
        shape = tuple(x)
        return ndim, shape
    else:
        return -1, (0,0,0)

def sendNewImage(contact):
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    # image = cv2.imread('PassportPhoto.jpg')

    h,w,n = image.shape

    message = ""
    for i in range(h):
        for j in range(w):
            for k in range(n):
                message = message+chr(image[i][j][k])
                
    contact.send_message(message)

def receivenewImage(contact, last_timestamp, shape):
    chat = contact.driver.wapi_functions.getAllMessagesInChat(contact.id, 0, 0)
    messageLatest = chat[len(chat)-1]["content"]
    
    im = np.zeros((len(messageLatest)))
    for i in range(len(content)):
        im[i] = ord(content[i])
    im = np.reshape(im,  shape).astype(np.uint8)
    
    timestamp = chat[len(chat)-1]["timestamp"]
    if timestamp > last_timestamp:
        return timestamp, im
    
    
# Main function
driver = wd(username="check", client="chrome")
print("Waiting for QR")
driver.wait_for_login()

for contact in driver.get_all_chats():
    if contact.name == sys.argv[1]:
        break

# pdb.set_trace()

sendHeader(contact)
ndim, shape = receiveHeader(contact)

pool = Pool(processes=2)

timestamp = 0
receive = pool.apply_async(receiveNewImage, [contact, timestamp, shape])
pool.apply_async(sendNewImage, [contact])

timestamp, im = get(receive)

cv2.imwrite('check.jpg', im)

pool.close()