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

**Screenshots**
1. The Initial Part For Selecting an Image
<img width="410" alt="IDReader 1" src="https://user-images.githubusercontent.com/92080989/150647729-c36e7466-6bd6-442b-8652-c44a616e42d0.PNG">

2. A Selected Image(Left) and Expected Text Output(Right)
** Some Information has been coloured out since this is a Picture from the internet
![image](https://user-images.githubusercontent.com/92080989/150647704-e085fb90-531f-4680-91da-3dd05fdd63ae.png)

**To Note**
1. The Application is accurate to some extent, that is when working with clear images, with colour contrasting foregrounds and backgrounds. The text should also be legible.
If a trained model is to be used it would improve the accuracy significantly.
2. I had an issue trying to upload the file using streamlit and still reading the same file from the storage. _My workarond:_ Saving uploaded files to a new folder that is being called within the application when I attempt to read the Image.(Suggestions on how to improve this are highly welcomed)
