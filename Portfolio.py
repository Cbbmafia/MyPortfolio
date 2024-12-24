import streamlit as st
from pathlib import Path
from PIL import Image

title = "My Portfolio"
st.title (f":grey[{title}]")
st.markdown("""___""")

im_1= r"portimg\1.png"
im_2= r"portimg\2.png"
im_3= r"portimg\3.png"
im_4= r"portimg\4.png"
im_5= r"portimg\5.png"
im_6= r"images\1.png"
im_7= r"images\2.png"
im_8= r"images\3.png"
im_9= r"images\4.png"
im_10= r"images\5.png"
im_11= r"images\6.png"
#im_12= r"images\3.png"
#im_13= r"images\3.png"

st.write(" ")
st.image(im_5)

header = "SUBURBAN OASIS"
st.header (f":grey[{header}]")
st.write ("Site: Kalatiya, Keraniganj, Dhaka")




c = st.container()
col1, col2, col3= st.columns (3)
col1.subheader(":grey[Typology]")
col2.subheader(":grey[Year]")
col3.subheader(":grey[Studio]")

st.markdown("""
<style>
.big-font {
    font-size:25px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.mid-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

col1.markdown('<p class="big-font">Urban Design</p>', unsafe_allow_html=True)
col2.markdown('<p class="big-font">2023-2024</p>', unsafe_allow_html=True)
col3.markdown('<p class="big-font">4-1</p>', unsafe_allow_html=True)

st.markdown('<p class="mid-font"> Envisioning Critial Regionalism and lts Application in Urban Design- </p>', unsafe_allow_html=True)
st.write ("Exploring Kalatia of Keraniganj to map and analyze the prevailing settlement and socio-economic dynamics of potential urban growth centers.he objective is to generate place-based urban design strategies that will accommodate aspired urban amenities,ensuring livability, livelihood opportunities, and urban resilience. Students will do speculative urban design exer-cises to test the generated strategies in multiple scales and envision critical regionalism in terms of urban design.")


col4,col5,col6=st.columns([3,3,4])

with col4:
	c = st.container()
	st.image(im_1, width= 400)
	c.write(" ")
	c.write(" ")
	c.write(" ")
	c.write(" ")
	c.write(" ")
	c.write(" ")
	c.write(" ")
	c.write(" ")


with col5:
	c = st.container()
	st.image(im_2, width= 800)
	c.write(" ")
	c.write(" ")
	c.write(" ")
	c.write(" ")
	c.write(" ")
	c.write(" ")
	c.write(" ")
	c.write(" ")
	c.write(" ")
	c.write(" ")
	c.write(" ")


with col6:
	st.image(im_4, width= 400)

c= st.container()
col4.caption("Keraniganj upazilla in Dhaka Division")
col5.caption ("Kalatiya Union in Keraniganj upazilla")
col6.caption ("Kalatiya Union")

st.subheader(":grey[History Profiling | Morphological change of Settlement Pattern]")
st.image(im_3)

c1,c2,c3,c4,c5,c6,c7,c8= st.columns([3,3,3,3,3,3,3,4])

with c2:
	st.caption(":red[1993]")



with c4:
	st.caption(":red[2003]")


with c6:
	st.caption(":red[2015]")


with c8:
	st.caption(":red[2022]")


c10,c11,c12,c13,c14= st.columns([1,3,3,3,3])

c11.caption("Settlement in the riverbank")
c12.caption("River dynamics discourages permanent settlement")
c13.caption("River and Canals Drying out")
c14.caption("Floodplain formed by siltation")

st.subheader(":grey[Frameworks in Macro Level Masterplan]")
c21,c22=st.columns([4,5])
c21.image(im_6, width= 600)

c21.caption("Framework 01: Establishing Green-Blue network and Embracing changes over Time")
c22.image(im_7)
c22.caption(" ")
c22.caption("Framework 02: Promoting Socio-Economic Activities at potential unproductive Landscape")

c31,c32=st.columns(2)
c31.image(im_9)
c32.image(im_10)
c31.caption("Framework 03: Promoting Walkable neighborhood through integration of landscape and built environment")
c32.caption("Framework 04: Integrating Blue-Green network with a system of Public Open Spaces")

st.subheader(":grey[Masterplan]")
st.image(im_8)
st.image(im_11)