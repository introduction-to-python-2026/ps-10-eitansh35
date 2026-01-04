import numpy as np
from PIL import Image
from scipy.signal import convolve2d

def load_image(image_path):
    [span_2](start_span)"""טעינת תמונה והפיכתה למערך np.array[span_2](end_span)"""
    img = Image.open(image_path)
    return np.array(img)

def edge_detection(image_array):
    [span_3](start_span)"""זיהוי קצוות בתמונה[span_3](end_span)"""
    # [span_4](start_span)המרה לגווני אפור על ידי מיצוע שלושת ערוצי הצבע[span_4](end_span)
    gray_image = np.mean(image_array, axis=2)
    
    # [span_5](start_span)הגדרת פילטרים לזיהוי שינויים אנכיים ואופקיים[span_5](end_span)
    kernelY = np.array([[1, 2, 1], 
                        [0, 0, 0], 
                        [-1, -2, -1]])
                        
    kernelX = np.array([[1, 0, -1], 
                        [2, 0, -2], 
                        [1, 0, -1]])
    
    # [span_6](start_span)ביצוע קונבולוציה עם padding=0 (מצב same שומר על האורך והרוחב)[span_6](end_span)
    edgeY = convolve2d(gray_image, kernelY, mode='same', boundary='fill', fillvalue=0)
    edgeX = convolve2d(gray_image, kernelX, mode='same', boundary='fill', fillvalue=0)
    
    # [span_7](start_span)חישוב עוצמת הקצוות לפי הנוסחה המבוקשת[span_7](end_span)
    edgeMAG = np.sqrt(edgeX**2 + edgeY**2)
    
    return edgeMAG

