import streamlit as st
import pandas as pd
from PIL import Image


def app():

    original_title = '<p style="color:#0a066b; font-size: 50px;">Cybercrime</p>'
    st.write("")
 
    st.markdown(original_title, unsafe_allow_html=True)
    st.write("Merupakan suatu perbuatan melawan hukum yang dilakukan dengan menggunakan internet yang berbasis pada kecanggihan teknologi komputer dan telekomunikasi ( Teguh Wahyono, S. Kom, 2006 )")
    st.write("")

    col1, col2 = st.columns([2,2])
    col1.write("Cybercrime diatur dalam Undang-Undang Transaksi Elektronik Nomor 8 Tahun 2011 sebagaimana telah diubah menjadiUndang- Undang Nomor 19 Tahun 2016, ( “UU ITE”) khususnya pada pasal 27 sampai 30 mengenai perbuatan yang dilarang. Lebih lanjut,  aturan tentang hacking diatur dalam  pasal 30 ayat (1), (2) dan (3) mengatakan bahwa:")
    image = Image.open('cybe.jpg')
    col2.image(image, caption='Ilustrasi Cybercrime, www.google.com', width=300)
    
    st.write("1. Dengan sengaja tanpa hak dan tanpa hak atau melawan hukum mengakses dan/ atau sistem elektronik orang lain dengan cara apapun ")
    st.write("2. Dengan sengaja dan tanpa hak atau melawan hukum  mengakses komputer dan/ atau sistem orang lain dengan cara apapun untuk tujuan memperoleh Informasi Elektronik dan/atau Dokumen Elektronik. ")
    st.write("3. Dengan sengaja dan tanpa hak atau melawan hukum mengakses komputer dan/ atau sistem elektronik dengan tujuan melanggar menerobos, melampaui, menjebol sistem pengaman")

    st.video("https://www.youtube.com/watch?v=JSMxXZrY6es", format="video/mp4")  
