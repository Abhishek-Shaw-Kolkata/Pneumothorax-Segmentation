import cv2
from PIL import Image
import os
import pandas as pd
import tensorflow as tf
import streamlit as st
from tensorflow import keras
import pydicom
import matplotlib.pyplot as plt
from keras.losses import binary_crossentropy
IMG_WIDTH = IMG_HEIGHT = 256
N_CHANNELS=3
smooth = 1e-5
def dice_coef(y_true, y_pred):
    y_true_f = tf.keras.layers.Flatten()(y_true)
    y_pred_f = tf.keras.layers.Flatten()(y_pred)
    intersection = tf.reduce_sum(y_true_f * y_pred_f)
    return (2. * intersection + smooth) / (tf.reduce_sum(y_true_f) + tf.reduce_sum(y_pred_f) + smooth)


def combined_loss(y_true, y_pred):
    return 1.0 - dice_coef(y_true, y_pred) + binary_crossentropy(y_true, y_pred)

@st.cache
def get_model():
    model_seg= tf.keras.models.load_model('Uefficientnetb4',custom_objects={'combined_loss' :combined_loss, 
                                                                             'dice_coef' : dice_coef})
    return  model_seg                                                                   
def predict(file):
    delete_flag = False
    extension = os.path.splitext(file)[1] 
    if extension == '.dcm':
        dataset = pydicom.dcmread(file)
        d = {}
        d['patientID'] = dataset.PatientID
        d['age'] = dataset.PatientAge
        d['sex'] = dataset.PatientSex
        d['view_position'] = dataset.ViewPosition
        d['pixel_spacing']  = dataset.PixelSpacing
        d["modality"] = dataset.Modality
        d["body_part_examined"] =  dataset.BodyPartExamined
        df_meta = pd.DataFrame(d)
        st.subheader('Metadata info stored in the file')
        st.write(df_meta.drop_duplicates())
        file = file[:-4] + ".png"
        delete_flag = True
        cv2.imwrite(file,dataset.pixel_array)
    # Create a text element and let the reader know status.
    state = st.text('Loading Saved Model...')
    model_seg = get_model()
    state.text('Model loading done!')                                                                        
    img = tf.io.read_file(file)
    img = tf.image.decode_png(img, channels= N_CHANNELS)
    img = tf.image.convert_image_dtype(img, tf.float32) 
    img = tf.image.resize(img, [IMG_WIDTH, IMG_HEIGHT]) 
    img.set_shape((IMG_HEIGHT,IMG_WIDTH,3))
    state.text('Predicting...') 
    pred_mask= model_seg.predict(tf.expand_dims(img,axis=0)).reshape((IMG_HEIGHT,IMG_WIDTH)) 
    pred_mask = cv2.resize(pred_mask,(1024,1024))
    pred_mask = (pred_mask > .5).astype(int)
    img = cv2.resize(img.numpy(),(1024,1024))
    col1, col2,col3 = st.beta_columns(3)
    col1.header("Original")
    col1.image(img, use_column_width=True)
    col2.header("Prediction")
    col2.image(pred_mask*255, use_column_width=True)
    state.text('Prediction Done')
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1) 
    ax.imshow(img)
    ax.imshow(pred_mask,alpha=0.5,cmap='Reds')
    plt.axis('off')
    col3.header("Merged")
    col3.write(fig)
    if delete_flag:
        os.remove(file)
    #print(pred_mask[pred_mask > 0])
    #st.image([img,pred_mask], caption=[ 'Original Image','Prediction Image'],width=100,use_column_width=True)

#predict('test.png') #'ID_0acfa68b1.png'