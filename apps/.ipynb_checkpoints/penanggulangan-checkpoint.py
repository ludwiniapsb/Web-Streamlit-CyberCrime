import streamlit as st
from PIL import Image

def app():
    p_title = '<p style="color:#0a066b; font-size: 50px;">Penanggulangan Cybercrime</p>'
    st.markdown(p_title, unsafe_allow_html=True)


    p1_title = '<p style="color:#0a066b; font-size: 30px;">1. Pengamanan Sistem</p>'
    st.markdown(p1_title, unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    col2.write("Tujuan yang paling nyata dari suatu sistem keamanan adalah mencegah adanya perusakan bagian dalam sistem karena dimasuki oleh pemakai yang tidak diinginkan. Pengamanan sitem ini harus terintegrasi pada keseluruhan subsistem untuk mempersempit atau bahkan menutup adanya celah-celah unauthorised actions yang merugikan.")

    image_c= Image.open('apps/cegah.png')
    col1.image(image_c, width=200)
    
    
    p2_title = '<p style="color:#0a066b; font-size: 30px;">2. Penanggulangan Global</p>'
    st.markdown(p2_title, unsafe_allow_html=True)
    st.write("OECD (The Organization for Economic Cooperation and Development) telah merekomendasikan beberapa langkah penting yang harus dilakukan setiap negara dalam penanggulangan Cybercrime, sbb :")
    with st.expander("selengkapnya"):
        st.write("""
                1. Melakukan modernisasi hukum pidana nasional dengan hukum acaranya, yang diselaraskan dengan konvensi internasional.
                2. Meningkatkan sistem pengamanan jaringan komputer nasional sesuai standar internasional.
                3. Meningkatkan pemahaman serta keahlian aparatur penegak hukum mengenai upaya pencegahan, investigasi dan penuntutan perkara perkara yang berhubungan cybercrime.
                4. Meningkatkan kesadaran warga negara mengenai masalah cybercrime serta pentingnya mencegah kejahatan tersebut terjadi.
                5. Meningkatkan kerjasama antar negara, baik bilateral, regional maupun multilateral, dalam upaya penanganan cybercrime, antara lain melalui perjanjian ekstradisi dan mutual assistance treaties.
         """)
    
    p3_title = '<p style="color:#0a066b; font-size: 30px;">3. Perlunya Cyberlaw</p>'
    st.markdown(p3_title, unsafe_allow_html=True)
    st.write("Cybercrime belum sepenuhnya terakomodasi dalam peraturan / Undang-undang yang ada, penting adanya perangkat hukum khusus mengingat karakter dari cybercrime ini berbeda dari kejahatan konvensional.")

    p4_title = '<p style="color:#0a066b; font-size: 30px;">4. Perlunya Dukungan Lembaga Khusus</p>'
    st.markdown(p4_title, unsafe_allow_html=True)
    st.write("Lembaga ini diperlukan untuk memberikan informasi tentang cybercrime, melakukan sosialisasi secara intensif kepada masyarakat, serta melakukan riset-riset khusus dalam penanggulangan cybercrime. Indonesia sendiri sudah memiliki IDCERT (Indonesia Computer Emergency Response Team) https://www.cert.or.id/beranda/id/ yang diperlukan bagi orang-orang untuk melaporkan masalah-masalah keamanan komputer.")
