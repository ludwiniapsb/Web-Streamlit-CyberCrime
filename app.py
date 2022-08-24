import streamlit as st
from multiapp import MultiApp
from apps import Pendahuluan, Karakteristik, dataindia, kami, penanggulangan, jenis_kegiatan_cybercrime # import your app modules here

app = MultiApp()

st.set_page_config(page_title="CYBERCRIME", page_icon=":iphone:", layout="wide")

# Add all your application here
app.add_app("Pendahuluan", Pendahuluan.app)
app.add_app("Karakteristik", Karakteristik.app)
app.add_app("Jenis Cybercrime", jenis_kegiatan_cybercrime.app)
app.add_app("Penanggulangan", penanggulangan.app)
app.add_app("Data", dataindia.app)
app.add_app("Tentang Kami", kami.app)


# The main app
app.run()