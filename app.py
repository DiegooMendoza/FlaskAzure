from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

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

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/api')
def api():
   print('Request for api page received')
   return 'HOLAA!!!'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
