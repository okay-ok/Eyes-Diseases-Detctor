import streamlit as st
#import tensorflow.keras
import io
import keras
from PIL import Image, ImageOps
import numpy as np
import time

st.title("DetAll: All HealthCare Detection Tools at one place")
st.write("------------------------------------------")
st.sidebar.title("Command Bar")
choices = ["Home","Eyes", "Skin"]
menu = st.sidebar.selectbox("Menu: ", choices)
st.set_option('deprecation.showfileUploaderEncoding', False)
if menu =="Home":
    progress_bar = st.progress(0)
    status_text = st.empty()
    for i in range(100):
        progress_bar.progress(i + 1)
        status_text.text("Setting up the magic...")
    time.sleep(1)
    status_text.success("All Set!")
    st.write("---------------------------------")
    st.write("DetAll Contains 3 main sections: Explore the sections to your left sidebar. Once you select a section, you'll be asked to upload an image. Once uploaded, buttons will pop-up with function calls to the models. The results will be shown on the same page.")

elif menu == "Eyes":
    st.sidebar.write("It analyzes cataract, diabetic retinopathy and redness levels. Upload or take an image to get started.")
    st.write("---------------------------")
    image_input = st.file_uploader("Choose an eye image: ", type=['png', 'jpg'])
    start_camera = st.checkbox("Start Camera")

    if image_input:
            img = image_input.getvalue()
            st.image(img, width=300)# height=300)
            detect = st.button("Detect Cataract")
            np.set_printoptions(suppress=True)
            model = keras.models.load_model(r'D:\DEP\Eyes-Diseases-Detctor\eye_models\cataract\model.h5')
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            image = Image.open(image_input)
            size = (224, 224)
            image = ImageOps.fit(image, size, Image.ANTIALIAS)
            image_array = np.asarray(image)
            normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
            data[0] = normalized_image_array
            size = st.slider("Adjust Image Size: ", 300, 1000)
            st.image(img, width=size)#, height=size)
            st.write("------------------------------------------------------")
            
            if detect:
                prediction = model.predict(data)
                class1 = prediction[0,0]
                class2 = prediction[0,1]
                if class1 > 2*class2:
                    st.markdown("DetAll thinks this is a Cataract by {:.2f}%".format(class1 * 100) )
                elif class2 > 2*class1:
                    st.markdown("DetAll thinks this is not Cataract by {:.2f}%".format(class2 * 100))
                else:
                    st.write("We encountered an ERROR. This should be temporary, please try again with a better quality image. Cheers!")

    if start_camera:
        picture = st.camera_input("Take a picture", key="eye_photo" ,help="Click a close up photo of your eye so that we can check and analyse it")
        if picture:
            img = picture.getvalue()
            # st.image(img, width=300)# height=300)
            detect = st.button("Detect Cataract")
            np.set_printoptions(suppress=True)
            model = keras.models.load_model(r'D:\DEP\Eyes-Diseases-Detctor\eye_models\cataract\model.h5')
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            image = Image.open(image_input)
            size = (224, 224)
            image = ImageOps.fit(image, size, Image.ANTIALIAS)
            image_array = np.asarray(image)
            normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
            data[0] = normalized_image_array
            size = st.slider("Adjust Image Size: ", 300, 1000)
            st.image(img, width=size)#, height=size)
            st.write("------------------------------------------------------")
                
            if detect:
                prediction = model.predict(data)
                class1 = prediction[0,0]
                class2 = prediction[0,1]
                if class1 > 2*class2:
                    st.markdown("DetAll thinks this is a Cataract by {:.2f}%".format(class1 * 100) )
                elif class2 > 2*class1:
                    st.markdown("DetAll thinks this is not Cataract by {:.2f}%".format(class2 * 100))
                else:
                    st.write("We encountered an ERROR. This should be temporary, please try again with a better quality image. Cheers!")

elif menu == "Skin":
    st.sidebar.write("It detects whether the patient has benign or malignant type of cancer. Further classifications are still under testing. Upload or take an image to get started.")
    st.write("---------------------------")
    image_input = st.file_uploader("Choose an eye image: ", type=['png', 'jpg'])
    start_camera = st.checkbox("Start Camera")

    if image_input:
            img = image_input.getvalue()
            analyze = st.sidebar.button("Analyze")
            size = st.slider("Adjust image size: ", 300, 1000)
            st.image(img, width=size, height=size)
            st.write("-----------------------------------------")
            np.set_printoptions(suppress=True)
            model = keras.models.load_model('skin_model/model.h5')
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            if analyze: 
                image = Image.open(image_input)
                size = (224, 224)
                image = ImageOps.fit(image, size, Image.ANTIALIAS)
                image_array = np.asarray(image)
                normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
                data[0] = normalized_image_array
                prediction = model.predict(data)
                class1 = prediction[0,0]
                class2 = prediction[0,1]
                if class1 - class2 > 0.5:
                    st.markdown("Benign Detected. Confidence: {:.2f}%".format(class1 * 100))
                elif class2 - class1 > 0.5:
                    st.markdown("Malign Detected. Confidence: {:.2f}".format(class2 * 100))
                else:
                    st.write("Error! Please upload a better quality image for accuracy.")

    if(start_camera):
        picture = st.camera_input("Take a picture", key="eye_photo" ,help="Click a close up photo of your eye so that we can check and analyse it")
        if picture:
            img = image_input.getvalue()
            analyze = st.sidebar.button("Analyze")
            size = st.slider("Adjust image size: ", 300, 1000)
            st.image(img, width=size, height=size)
            st.write("-----------------------------------------")
            np.set_printoptions(suppress=True)
            model = keras.models.load_model('skin_model/model.h5')
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            if analyze: 
                image = Image.open(image_input)
                size = (224, 224)
                image = ImageOps.fit(image, size, Image.ANTIALIAS)
                image_array = np.asarray(image)
                normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
                data[0] = normalized_image_array
                prediction = model.predict(data)
                class1 = prediction[0,0]
                class2 = prediction[0,1]
                if class1 - class2 > 0.5:
                    st.markdown("Benign Detected. Confidence: {:.2f}%".format(class1 * 100))
                elif class2 - class1 > 0.5:
                        st.markdown("Malign Detected. Confidence: {:.2f}".format(class2 * 100))
                else:
                    st.write("Error! Please upload a better quality image for accuracy.")
