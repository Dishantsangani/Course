import csv
import copy
import argparse
import itertools
from collections import counter
from collections import deque

import cv2 as cv
import numpy as np
import mediapipe as mp

from utils import mediapipe
from model import keypointclassifier
from model import pointhistoryclassifier

def grt_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("__device",type=int,default=0)
    parser.add_argument("__width",help='cap width',type=int,default=960)
    parser.add_argument("__height",help='cap height',type=int,default=540)

    parser.add_argument("__use_static_image_mode",action="store_true")
    parser.add_argument("__min_detection_confidence",help="min_detection_confidence",type=float,default=0.7)

    parser.add_argument("__min_tracking_confidence",help="min_tracking_confidence",type=int,default=0.5)

    args = parser.parse_args()
    return args