import app1
import app2
from multiapp import MultiApp
import streamlit as st

app = MultiApp()
app.add_app("Introduction", app1.app)
app.add_app("Get Prediction", app2.app)
app.run()