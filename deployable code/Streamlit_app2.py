import streamlit as st
from prediction import predict
def app():
    html_temp = '''
               <div style = "background-color:Lime;padding:13px;">
                <h1 style ="color:black;text-align:center;">Pneumothorax Detector</h1></div>
                '''
    st.markdown(html_temp,unsafe_allow_html=True)
    st.header("Identify Pneumothorax disease in chest x-rays")
    file = st.file_uploader("Please upload an image file", type=["jpg", "png","dcm"])
    if file is not None:
        #data = file.read()
        predict(file.name)
        

if __name__ == '__main__':
    app()