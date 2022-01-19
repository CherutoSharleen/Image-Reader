import streamlit as st
import os
import cv2 #detect the image
import numpy as np
from PIL import Image,ImageEnhance
import pytesseract #read text from the image
pytesseract.pytesseract.tesseract_cmd=r'C:\Users\user\AppData\Local\Programs\Tesseract-OCR\tesseract.exe' #path where the tesseract is stored
st.header("Student ID Card Reader")
image_file = st.file_uploader("Upload Images",
			type=["png","jpg","jpeg"]) #streamlit image uploader 

if image_file is not None:
    path = os.path.join(r"C:\Users\user\.vscode\Codes\PythonLearning\files\ids",image_file.name)#using the os module to join the paths
    st.image(image_file)
    file_details = {"filename":image_file.name, "filetype":image_file.type,
                              "filesize":image_file.size}
    with open(path,"wb") as f:#open the path of the folder as wb to write into the file in binary mode
        f.write((image_file).getbuffer())
	
    st.write(file_details)
    #pass the path through opencv for it to be read
    img= cv2.imread(path)

    if(img.any() == True):
        #resizing the image then eliminating the colour back to gray scale
        if image_file.size < 30000:
            img = cv2.resize(img, (400,400))
        elif image_file.size >500000:
            img = cv2.resize(img, (2000,1000))
        else:
            img = cv2.resize(img, None, fx=10, fy=10, interpolation=cv2.INTER_CUBIC)#1.2
           
        #changing the color to gray scale making it easy for binarization
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #Applying dilation and erosion to remove the noise 
        #dilation(for thin letters) and extremely thick ones to normal weight
        #erosion to remove external paper bleeds
        kernel = np.ones((1, 1), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)
        cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
        #convert image to string. Pass image variable

        text = pytesseract.image_to_string(img)
        if text is not None:
            st.info(text)
        else:
            st.error("Incompatible Image. Please Try with a different Image")
        cv2.waitKey(1)
        #close all openWindows
        cv2.destroyAllWindows()
    else:
        st.error("Incompatible File Type or image. Please Try with a different Image")

    
    
