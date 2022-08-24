import streamlit as st
from PIL import Image


def app():
    original_title = '<p style="color:#0a066b; font-size: 50px;">Tentang Kami</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.write ("**_Disclaimer_**: Proyek ini merupakan bagian dari Women in Tech Program yang diadakan oleh Kementerian Komunikasi dan Informatika dengan Netacad. Materi dari website ini kami ambil dari pencarian google dan kami hanya gunakan untuk keperluan pelatihan.")
    col1, col2, col3 = st.columns([4, 4, 4])
    
    eka_title = '<p style="color:#0a066b; font-size: 30px;">Eka Rosita</p>'
    col1.markdown(eka_title, unsafe_allow_html=True)
    image_eka = Image.open('apps/eka.png')
    col1.image(image_eka, width=200)
    col1.write("Ibu rumah tangga yang berdomisili di Kabupaten Wajo. Ibu satu anak yang menyukai pendidikan, budaya serta bahasa")

    lud_title = '<p style="color:#0a066b; font-size: 30px;">Ludwinia Putri S</p>'
    col2.markdown(lud_title, unsafe_allow_html=True)
    image_lud = Image.open('apps/ludwinia.png')
    col2.image(image_lud, width=185)
    col2.write("Mahasiswi semester 7 Teknik elektro")    

    sus_title = '<p style="color:#0a066b; font-size: 30px;">Sussanti</p>'
    col3.markdown(sus_title, unsafe_allow_html=True)
    image_santi = Image.open('apps/santi.png')
    col3.image(image_santi, width=190)
    col3.write("Ibu rumah tangga dan mengabdikan diri pada bidang pendidikan di Yogyakarta.")    
