# Image-Reader
This is an image reader that is implemented using Python.

**How it Works**
The application asks the user to select a file(limited to file type PNG, JPG, JPEG) from the local or connected external strorage. 
Once the file is selected the image is preprocessed(resizing, dilation and erosion). It is then converted to string using Pytesseract and displayed on the interface using Streamlit. 

**Requirements.**
1. Numpy - Used For Image Resizing
2. OpenCV - Used for Image Manipulation and Preprocessing
3. PyTesseract - convert the image to String
4. Streamlit - A Python Front-End Framework



**How To Run It**
Use the command streamlit run thefilename.py in this case it is streamlit run streamlit_image_reader.py
