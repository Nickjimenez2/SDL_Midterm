from tkinter import*
root = Tk()
import streamlit as st
from PIL import Image



st.set_page_config(page_title="SDL Bike Accessories", page_icon=":bike:", layout="wide")


#Header
with st.container():
    st.title("Hello and welcome to our Shop")




#sub_header
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('Diffrent Products that we Offer')
        st.write("##")
    image = Image.open('hm_shop_used.jpg')

    st.image(image, caption='here are some of the Products that we Offer')


with st.container():
    st.write('---')
    st.header('New Arrival')
    st.write('##')
    image_column, text_column = st.columns((1,2))
    with image_column:
        image2 = Image.open('3-1-1024x801.jpg')
        st.image(image2, caption='Hondas  All-New ADV160')
    with text_column:
        st.subheader('Our newest Model')
        st.write('The All-New ADV160 is now equipped with a new generation 157cc, 4-Valve, Liquid-Cooled, eSP+ Engine, offering advanced technology with 4-valve mechanism')
with st.container():
    st.write('---')
    st.header('New Arrival')
    st.write('##')
    image_column, text_column = st.columns((1,2))
    with image_column:
        image3 = Image.open('3-1024x801.jpg')
        st.image(image3, caption='Hondas  HONDA AIRBLADE 160')
    with text_column:
        st.subheader('One of Our newest Model')
        st.write('The All-New AirBlade160 lives up to its name by allowing you to slice through the wind while speeding on the new generation 157cc, 4-Valve, eSP+ engine. It’s the model’s star upgrade that generates peak power of 11.2kW @ 8,000rpm and top torque of 14.6Nm @ 6,500rpm, which proves more than enough in making your way through city traffic or going full throttle in long drives.')





with st.container():
    st.write('---')
    st.header('Order Form')
    st.write('##')
    st.write('Please fill up the form to order One of our Amazing Motorcycles')
    name = st.text_input("Full Name")
    address = st.text_area("Address")
    email = st.text_input("Email")
    number = st.number_input("Contact Number", step=1)
    date = st.date_input("Date of Birth")
    product = st.radio("Product you want to Order", ["Honda ADV 160", "Honda AIRBLADE 160"], index=1)
    if st.button("Order Now"):
        st.write("Thank you for Ordering")




