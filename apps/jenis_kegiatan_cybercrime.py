import streamlit as st
from PIL import Image

def app():
    jenis_title = '<p style="color:#0a066b; font-size: 50px;">Jenis Cybercrime</p>'
    st.markdown(jenis_title, unsafe_allow_html=True)

    st.write(" Menurut Teguh Wahyono, S. Kom., 2006 jenis cybercrime dikelompokan dalam :")

   
    with st.expander("1. Cybercrime berdasarkan Jenis Aktifitas"):
    #st.header('1. Jenis Aktifitas')
        st.subheader("a. Unauthorized Acces ")
        st.write("Kejahatan yang terjadi ketika seseorang memasuki atau menyusup ke dalam suatu sistem jaringan komputer sedara tidak sah, tanpa izin atau tanpa sepengetahuan dari pemilik sistem jaringan komputer yang dimasukinya, contoh : Probing dan Port Scanning")
        st.subheader("b. Illegal Contents ")
        st.write("Kejahatan yang dilakukan dengan memasukkan data atau informasi ke internet tentang sesuatu hal yang tidak benar, tidak etis, dan dapat dianggap melanggar hukum atau mengganggu ketertiban umum, contoh : penyebarluasan pornografi, isu-isu / fitnah terhadap individu (biasanya public figure).")
        st.subheader("c. Penyebaran Virus Secara Sengaja")
        st.write("Melakukan penyebaran virus yang merugikan seseorang atau institusi dengan sengaja")
        st.subheader("d. Data Forgery")
        st.write("Kejahatan yang dilakukan dengan tujuan memalsukan data pada dokumen-dokumen penting yang ada di internet, biasanya dimiliki oleh institusi atau lembaga yang memiliki situs berbasis web database.")
        st.subheader("e. Cyber Espionage, Sabotage and Extortion")
        st.write("Cyber Espionage merupakan kejahatan yang memanfaaatkan jaringan internet untuk melakukan kegiatan mata-mata terhadap pihak lain, dengan memasuki sistem jaringan komputer pihak sasaran.")
        st.write("Sabotage and Extortion merupakan jenis kejahatan yang dilakukan dengan membuat gangguan, perusakan atau penghancuran terhadap suatu data, program komputer atau sistem jaringan komputer yang terhubung dengan internet.")
        st.subheader("f. Cyberstalking")
        st.write("Kejahatan yang dilakukan untuk mengganggu atau melecehkan seseorang dengan memanfaatkan komputer, misalnya dengan melakukan teror melalui pengiriman e-mail secara berulang-ulang tanpa disertai identitas yang jelas.")
        st.subheader("g. Carding")
        st.write("Kejahatan yang dilakukan untuk mencuri nomor kartu kredit milik orang lain dan digunakan dalam transaksi perdagangan di internet.")
        st.subheader("h. Hacking dan Cracking")
        st.write("Hacker sebenarnya memiliki konotasi yang netral, namun bila kemampuan penguasaan sistem komputer yang tinggi dari seorang hacker ini disalah-gunakan untuk hal negatif, misalnya dengan melakukan perusakan di internet maka hacker ini disebut sebagai cracker. Aktifitas cracking di internet meliputi pembajakan account milik orang lain, pembajakan situs web, probing, penyebaran virus, hingga pelumpuhan target sasaran (menyebabkan hang, crash).")
        st.subheader("i. Cybersquatting and Typosquatting")
        st.write("Cybersquatting merupakan kejahatan yang dilakukan dengan mendaftarkan domain nama perusahaan orang lain dan kemudian berusaha menjualnya kepada perusahaan tersebut dengan harga yang lebih mahal. Pekerjaan ini mirip dengan calo karcis.")
        st.write("Typosquatting adalah kejahatan dengan membuat domain plesetan yaitu domain yang mirip dengan nama domain orang lain, biasanya merupakan nama domain saingan perusahaan.")
        st.subheader("j. Hijacking")
        st.write("Hijacking merupakan kejahatan pembajakan terhadap hasil karya orang lain, biasanya pembajakan perangkat lunak (Software Piracy).")
        st.subheader("k. Cyber Terorism")
        st.write("Kejahatan yang dilakukan untuk mengancam pemerintah atau warga negara, termasuk cracking ke situs pemerintah atau militer.")


    with st.expander("2. Cybercrime berdasarkan Motif Kegiatan"):
    #st.header('2. Motif Kegiatan')

        st.subheader('a. Cybercrime sebagai tindakan murni kriminal')
        st.write("Kejahatan ini murni motifnya kriminal, ada kesengajaan melakukan kejahatan, misalnya carding yaitu pencurian nomor kartu kredit milik orang lain untuk digunakan dalam bertransaksi di internet.")

        st.subheader('b. Cybercrime sebagai kejahatan abu-abu')
        st.write("Perbuatan yang dilakukan dalam jenis ini masuk dalam wilayah abu-abu, karena sulit untuk menentukan apakah hal tersebut merupakan kriminal atau bukan mengingat motif kegiatannya terkadang tidak dimaksudkan untuk berbuat kejahatan, misalnya Probing atau portscanning yaitu tindakan pengintaian terhadap sistem milik orang lain dengan mengumpulkan informasi sebanyak mungkin, namun data yang diperoleh berpotensi untuk dilakukannya kejahatan.")

    with st.expander("3. Cybercrime berdasarkan Sasaran Kejahatan"):
    #st.header('3. Sasaran Kejahatan.')
    
        st.subheader('a. Cybercrime yang menyerang individu (Against Person)')
        st.write("Jenis kejahatan ini sasaran serangannya adalah perorangan/individu yang memiliki sifat atau kriteria tertentu sesuai tujan penyerangan tersebut, contoh : Pornografi, Cyberstalking, Cyber-Tresspass.")

        st.subheader('b. Cybercrime menyerang Hak Milik (Against Property)')
        st.write("Kejahatan yang dilakukan untuk mengganggu atau menyerang hak milik orang lain, contoh : pengaksesan komputer secara tidak sah, pencurian informasi, carding, cybersquatting, typosquatting, hijacking, data forgery.")

        st.subheader('c. Cybercrime Menyerang Pemerintah (Against Government)')
        st.write("Kejahatan ini dilakukan dengan tujuan khusus penyerangan terhadap pemerintah, contoh : cyber terorism, craking ke situs resmi pemerintah.")
        
