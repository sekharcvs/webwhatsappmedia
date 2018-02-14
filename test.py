# -*- coding: utf-8 -*
from webwhatsapi import WhatsAPIDriver as wd
import pdb
import cv2
import numpy as np
import zlib
from base64 import b64encode, b64decode

driver = wd(username="check", client="chrome")

print("Waiting for QR")
driver.wait_for_login()

camera = cv2.VideoCapture(0)
return_value, image = camera.read()
# image = cv2.imread('PassportPhoto.jpg')

h,w,n = image.shape

message = ""
for i in range(h):
    for j in range(w):
        for k in range(n):
            message = message+chr(image[i][j][k])


pdb.set_trace()
for contact in driver.get_all_chats():
    if contact.name == "Rahul Shukla":
        chat = contact.driver.wapi_functions.getAllMessagesInChat(contact.id, 1, 0)
        len1 = len(chat)
        content = chat[len1-1]["content"]
        # pdb.set_trace()

        # Display the last chat message
        contact.send_message(message)
        chat = contact.driver.wapi_functions.getAllMessagesInChat(contact.id, 1, 0)
        len1 = len(chat)
        content = chat[len1-1]["content"]
        im = np.zeros((len(content)))
        for i in range(len(content)):
            im[i] = ord(content[i])
        im = np.reshape(im,  (h, w, n))