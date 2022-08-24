import pandas as pd
import streamlit as st




def app():
	st.markdown("# Data Cyber Crime di India 2016-2018")
	
	data = pd.read_csv('data.csv')

	start_station_list = ['All'] + data['State/UT'].unique().tolist()

	s_station = st.selectbox('Kota mana yang ingin kalian ketahui?', start_station_list, key='start_station')

	st.write('Kamu pilih: ' + str(s_station))

	st.write('Tabel Data sesuai yang dipilih')
	if s_station != 'All':
		display_data = data[data['State/UT'] == s_station]

	else:
		display_data = data.copy()

	st.write(display_data)



	
	
	


