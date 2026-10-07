import streamlit as st

st.header('Energy Calculator')

col1,col2=st.columns(2)

with col1:

    st.subheader(':red[Kinetic Energy]')
    m=st.number_input('Mass:',key='a')
    v=st.number_input('Velocity:',key='b')
    if st.button('Calculate',key='abc'):
        st.write('the kinetic energy is {0.5 *m*v**2}')


with col2:

    st.subheader(':red[Potential Energy]')
    ma=st.number_input('Mass:' ,key='c')
    h=st.number_input('height:', key='d')
    if st.button('Calculate',key='xyz'):
        st.write('the potential energy is {ma*10*h}')