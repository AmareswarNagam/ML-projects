import streamlit as st
import pickle


global Language_Detector_Model

model_file = open("language_detection_model.pckl", "rb")
Language_Detector_Model = pickle.load(model_file)
model_file.close()

st.title("Language Detection Tool")

input_text = st.text_input("provide your input text here", "Hello my name is Tony")

button_clicked = st.button("Get Language")
if button_clicked:
    language = Language_Detector_Model.predict([input_text])[0]
    st.success(f"Detected Language: {language}")




