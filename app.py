import streamlit as st
from utils import page_style, footer

st.set_page_config(page_title="MM-1887 Virtual Laboratory", page_icon="🔬", layout="wide", initial_sidebar_state="expanded")
page_style()

st.title("MM-1887 Virtual Laboratory")
st.subheader("Computational Reconstruction of the Michelson–Morley Experiment, 1887")
st.markdown("""
Welcome to an interactive reconstruction of the **Michelson–Morley ether-drift experiment**.

Use the pages in the sidebar to move through the experiment in laboratory sequence:

1. **Overview** — historical context, apparatus and experimental question.
2. **Experiment Setup** — configure the optical system and historical parameters.
3. **Interference Pattern** — generate the simulated detector fringes.
4. **Rotation Analysis** — rotate the interferometer through 360° and examine the predicted signal.
5. **Results** — compare the classical ether prediction with the historical null result.
6. **Theory** — inspect the equations and physical assumptions.

### Central question
> If the Earth were moving through a stationary luminiferous ether, would rotating the interferometer change the interference fringes?

The application separates the **classical prediction** from the **historical observation**, rather than treating the experiment as a direct proof of Special Relativity.
""")
c1,c2,c3=st.columns(3)
c1.metric("Experiment","Michelson–Morley")
c2.metric("Year","1887")
c3.metric("Core observable","Fringe displacement")
st.info("Start with **Overview** in the sidebar, then proceed through the laboratory pages in order.")
footer()
