from textwrap import wrap
from nbformat import write
import streamlit as st
from PIL import Image


def app():
    original_title = '<p style="color:#0a066b; font-size: 50px;">Karakteristik Kejahatan Bidang TI</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.write(" ")
    col1, col2 = st.columns([2, 2])
    image_crime = Image.open('apps/people_crime.png')
    col1.image(image_crime, width=250)
    satu_title = '<p style="color:#0a066b; font-size: 30px;">Ruang Lingkup kejahatan</p>'
    col2.markdown(satu_title, unsafe_allow_html=True)
    col2.write("Bersifat global ( melintasi batas negara ) menyebabkan sulit menentukan yuridiksi hukum negara mana yang berlaku terhadapnya.") 
    dua_title = '<p style="color:#0a066b; font-size: 30px;">Sifat Kejahatan</p>'
    col2.markdown(dua_title, unsafe_allow_html=True)
    col2.write("Tidak menimbulkan kekacauan yang mudah terlihat (non-violence), sehingga ketakutan terhadap kejahatan tersebut tidak mudah timbul.")
    st.write(" ")
    col1, col2, col3 = st.columns([2, 2, 2])
    tiga_title = '<p style="color:#0a066b; font-size: 30px;">Pelaku Kejahatan</p>'
    col1.markdown(tiga_title, unsafe_allow_html=True)
    col1.write("Pelaku kejahatan ini tidak mudah didentifikasi, namun memiliki ciri khusus yaitu pelakunya menguasai penggunaan internet / komputer.")
    empat_title = '<p style="color:#0a066b; font-size: 30px;">Modus kejahatan</p>'
    col2.markdown(empat_title, unsafe_allow_html=True)
    col2.write("Modus kejahatan hanya dapat dimengerti oleh orang yang mengerti dan menguasai bidang teknologi informasi.")
    lima_title = '<p style="color:#0a066b; font-size: 30px;">Jenis Kerugian</p>'
    col3.markdown(lima_title, unsafe_allow_html=True)
    col3.write("Kerugian yang ditimbulkan lebih luas, termasuk kerugian dibidang politik, ekonomi, sosial dan budaya.")
    


