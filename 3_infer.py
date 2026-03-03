import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import sklearn as sk
import streamlit as st
import cv2
import os

from PIL import Image
from os import listdir,makedirs
from os.path import isfile,join

sb.set()

st.set_page_config(page_title="Statisics", page_icon="🎥", layout='wide')
option = st.sidebar.selectbox('Select the type of visualisation', ('Image','Video','Real-Time',))

if option == 'Image': #Inferencing trained model using uploaded images
    count       = 0
    upload_mode = st.sidebar.selectbox('Select mode of uploading image', ('Upload','Filepath','Take a picture',))
    if upload_mode == 'Upload':
        img     = st.file_uploader('Upload an image (.jpg or .png)')
        c1, c2  = st.columns(2)

        if img is not None:
            with c1: #Display original images
                st.caption('Original Images: ')
                st.image(img)
            with c2:
                st.caption('Processed Images: ')
                #Process images HERE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        else:
            st.error('Upload an Image')

    elif upload_mode == 'Filepath':
        c5, c6  = st.columns(2)
        with c5:
            fpath = st.text_input("Insert full filepath to original folder", "./data/images/original")
            for f in fpath:
                imglist_1 = listdir(fpath)
                img_len_1 = len(imglist_1)
        
            if img_len_1 == 0 or None:
                st.error("UPLOAD IMAGES TO DIRECTED PATH")
            elif img_len_1 == 1:
                img_name_1 = imglist_1[0]
                show_img_1 = fpath + '/' + str(img_name_1)
                st.image(show_img_1)
            else:
                img_slider_1 = st.slider("Preview original image", 0, img_len_1-1 , 1)
                img_name_1 = imglist_1[img_slider_1]
                show_img_1 = fpath + '/' + str(img_name_1)
                st.image(show_img_1)
        
        with c6:
            dpath = st.text_input("Insert full filepath to destination folder", "./data/images/processed")
            for d in dpath:
                imglist_2 = listdir(dpath)
                img_len_2 = len(imglist_2)

            #Process images HERE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

            if img_len_2 == 0 or None:
                st.error("UPLOAD IMAGES TO DIRECTED PATH")
            elif img_len_2 == 1:
                img_name_2 = imglist_1[0]
                show_img_2 = fpath + '/' + str(img_name_2)
                st.image(show_img_2)
            else:
                img_slider_2 = st.slider("Preview processed image", 0, img_len_2-1 , 1)
                img_name_2 = imglist_2[img_slider_2]
                show_img_2 = dpath + '/' + str(img_name_2)
                st.image(show_img_2)

    elif upload_mode == 'Take a picture':
        count   = 0
        c5, c6  = st.columns(2)
        
        with c5:
            perms = st.button("Allow Access To Webcam", width="stretch", type="primary")
        with c6:
            stop = st.button("Stop", width="stretch", type="primary")

        if not stop:
            img_file = st.camera_input("Capture a picture", disabled=not perms)

            if img_file is not None:
                with open(f"./data/images/{count}.png", 'wb') as f:
                    f.write(img_file.getvalue())
                    st.success(f"Uploaded {count}.png", icon="✅")
        else:
            st.write("Camera has shut down")

        #Process images HERE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        temp_img = f'.\data\images\{count}.png'
        processed_img = f'.\data\images\processed\{count}.png'
        if temp_img is None:
            st.write("Wait!!!")
        else:
            st.image(temp_img)
        count+=1

elif option == 'Video': #Inferencing trained model using uploaded video
    
    upload_mode = st.sidebar.selectbox('Select mode of uploading image', ('Upload','Filepath','URL','Take a video',))
    if upload_mode == 'Upload':
        vid = st.file_uploader('Upload a video (.mp4 or .avi)')
        c1, c2  = st.columns(2)

        if vid is not None:
            with c1: #Display original images
                st.caption('Original video: ')
                st.video(vid)
            with c2:
                st.caption('Processed video: ')
                #Process videos HERE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        else:
            st.error('Upload a Video')

    elif upload_mode == 'Filepath':
        c5, c6  = st.columns(2)
        with c5:
            fpath = st.text_input("Insert full filepath to original folder", "./data/video/original")
            for f in fpath:
                vidlist_1 = listdir(fpath)
                vid_len_1 = len(vidlist_1)
        
            if vid_len_1 == 0 or None:
                st.error("UPLOAD VIDEOS TO DIRECTED PATH")
            elif vid_len_1 == 1:
                vid_name_1 = vidlist_1[0]
                show_vid_1 = fpath + '/' + str(vid_name_1)
                st.image(show_vid_1)
            else:
                vid_slider_1 = st.slider("Preview original video", 0, vid_len_1-1 , 1)
                vid_name_1 = vidlist_1[vid_slider_1]
                show_vid_1 = fpath + '/' + str(vid_name_1)
                st.image(show_vid_1)
        
        with c6:
            dpath = st.text_input("Insert full filepath to destination folder", "./data/video/processed")
            for d in dpath:
                vidlist_2 = listdir(dpath)
                vid_len_2 = len(vidlist_2)

            #Process videos HERE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

            if vid_len_2 == 0 or None:
                st.error("UPLOAD VIDEOS TO DIRECTED PATH")
            elif vid_len_2 == 1:
                vid_name_2 = vidlist_2[0]
                show_vid_2 = fpath + '/' + str(vid_name_2)
                st.image(show_vid_2)
            else:
                vid_slider_2 = st.slider("Preview processed video", 0, vid_len_2-1 , 1)
                vid_name_2 = vidlist_2[vid_slider_2]
                show_vid_2 = dpath + '/' + str(vid_name_2)
                st.image(show_vid_2)
    elif upload_mode == 'URL':
        st.write("Still thinking...")
    elif upload_mode == 'Take a video':
        st.write("Still thinking...")

elif option == 'Real-Time': #Inferencing trained model real time with webcam
    c1, c2 = st.columns(2)
    with c1:
        perms = st.button("Allow Access To Webcam", width="stretch", type="primary")
    with c2:
        stop = st.button("Stop", width="stretch", type="primary")
    
    count   = 0
    cap     = cv2.VideoCapture(0)
    fph     = st.empty() #Frame placeholder

    while cap.isOpened() and perms:
        ret, frame  = cap.read()

        #Process livefeed HERE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        #Check if camera is accessible
        if not ret:
            st.write("The video capture has ended")
            break

        #Replace webcam frames with empty frames and vice versa
        with fph:
            frame = st.image(frame,
                            width="stretch",
                            caption="Real-Time feed via Webcam",
                            channels="BGR")
        if stop:
            break
    
    cap.release()