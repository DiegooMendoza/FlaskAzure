from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2

import imutils

from scipy.spatial import distance as dist
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.models import load_model


# Initialize the Flask application
app = Flask(__name__)


# route http posts to this method
@app.route('/api/size', methods=['POST'])
def test():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    image = img_to_array(img) / 255.0
    '''
    # -- Resize image ---
    down_width = 224
    down_height = 224
    down_points = (down_width, down_height)
    image = cv2.resize(image, down_points, interpolation=cv2.INTER_LINEAR)
    image = np.expand_dims(image, axis=0)


    starken_mod = load_model('assets/starken_cnn_weights_15062022')

    preds = starken_mod.predict(image)[0]
    (startX, startY, endX, endY) = preds

    pixelsPerMetric = 4.38#4.46 #4.955555555555556

    (tl, tr, bl, br) = [[startX,startY],[endX,startY],[startX,endY],[endX,endY]]

    (tltrX, tltrY) = midpoint(tl, tr)
    (blbrX, blbrY) = midpoint(bl, br)
    # compute the midpoint between the top-left and top-right points,
    # followed by the midpoint between the top-righ and bottom-right
    (tlblX, tlblY) = midpoint(tl, bl)
    (trbrX, trbrY) = midpoint(tr, br)

    dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
    dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
    dimA = (dA / pixelsPerMetric) - 2
    dimB = (dB / pixelsPerMetric) - 2

    # -- Calcula alto --
    FocLenght = 648  # F
    CamHeight = 194
    PalletHeight = 51
    Cam2Pallet = CamHeight - PalletHeight  # Calculate the distance from the camera to the pallet

    DistA = (dimA * FocLenght) / dA
    DistB = (dimB * FocLenght) / dB
    DisProm = (DistA + DistB) / 2
    Dist = Cam2Pallet - DisProm


    '''
    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
    #            ,'Largo': '{:.1f} cm.'.format(dimA)
    #            ,'Ancho': '{:.1f} cm.'.format(dimB)
    #            ,'Alto': '{:.1f} cm.'.format(Dist)
    #            ,'Volumen': '{:.1f} cm.'.format((dimA*dimB*Dist)/ 1.000)
                }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")

def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

#app.run(host="0.0.0.0", port=5000)

# start flask app
