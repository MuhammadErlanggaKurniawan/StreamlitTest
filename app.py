# Import Streamlit

import streamlit as st

st.title('Testo Testo This is My First Streamlit Project')
st.header('This is Header')
st.write('Its just a text that written')

# Data Masuk
import pandas as pd
st.write('Streamlit can show / write data too')
df = pd.DataFrame({
    'Nama': ['Steven','Shake','Spear','All the other guy'],
    'Nilai': [90, 85, 95, 80]
})

st.header('Streamlit can also make interactive dataframe')
st.dataframe(df)

st.header('And Static Dataframe too')
st.table(df)

# Its time to make some widget
st.header('Interactive Widget')

# 1. Tombol (Button)
if st.button('Click me bitch!'):
    st.success('Thanks for clicking dickhead!')
    st.balloons() # Efek bonus!

# 2. Input Teks (Text Input)
nama = st.text_input('Your name?')
if nama:
    st.write(f'Halo, {nama}! kamu ganteng/cantik!')

# 3. Pilihan (Select Box)
pilihan_mk = st.selectbox(
    'Select your favorite person!',
    ('Eris', 'Angel', 'Diana')
)
st.write(f'Your choice is: **{pilihan_mk}**')

# 4. Slider
love_level = st.slider('How much you love her? (1-10)', 1, 10, 5)
st.write(f'You love her: {love_level}')