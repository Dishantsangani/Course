{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import cv2\n",
    "\n",
    "face_cascade = cv2.CascadeClassifier('face.xml')\n",
    "eye_cascade = cv2.CascadeClassifier('eye.xml')\n",
    "\n",
    "cap = cv2.VideoCapture(0)\n",
    "\n",
    "while 1:\n",
    "    ret, img = cap.read()\n",
    "    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)\n",
    "    faces = face_cascade.detectMultiScale(gray, 1.3, 5)\n",
    "\n",
    "    for (x,y,w,h) in faces:\n",
    "        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)\n",
    "        roi_gray = gray[y:y+h, x:x+w]\n",
    "        roi_color = img[y:y+h, x:x+w]\n",
    "        \n",
    "        eyes = eye_cascade.detectMultiScale(roi_gray)\n",
    "        for (ex,ey,ew,eh) in eyes:\n",
    "            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)\n",
    "\n",
    "    cv2.imshow('img',img)\n",
    "    k = cv2.waitKey(30) & 0xff\n",
    "    if k == 27:\n",
    "        break\n",
    "\n",
    "cap.release()\n",
    "cv2.destroyAllWindows()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}