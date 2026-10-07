import streamlit as st
import numpy as np
import plotly.graph_objects as go
from core.ether_model import fringe_shift

st.set_page_config(page_title="Parameter Explorer | MM-1887", page_icon="🧪", layout="wide")
st.title("10 · Parameter Explorer")
st.subheader("Investigate what controls the experimental sensitivity")

L=st.slider("Effective path length L (m)",1.0,50.0,11.0,0.5)
v_kms=st.slider("Assumed speed v (km/s)",1.0,100.0,29.8,0.1)
lam_nm=st.slider("Wavelength λ (nm)",400.0,800.0,550.0,1.0)

wavelengths=np.linspace(400,800,250)
lengths=np.linspace(1,50,250)
shift_lambda=fringe_shift(L,wavelengths*1e-9,v_kms*1000)
shift_L=fringe_shift(lengths,lam_nm*1e-9,v_kms*1000)

c1,c2=st.columns(2)
with c1:
    fig=go.Figure(go.Scatter(x=wavelengths,y=shift_lambda,mode="lines"))
    fig.update_layout(height=420,xaxis_title="Wavelength (nm)",yaxis_title="Nmax (fringe)",title="Sensitivity to wavelength")
    st.plotly_chart(fig,use_container_width=True)
with c2:
    fig=go.Figure(go.Scatter(x=lengths,y=shift_L,mode="lines"))
    fig.update_layout(height=420,xaxis_title="Effective path length (m)",yaxis_title="Nmax (fringe)",title="Sensitivity to path length")
    st.plotly_chart(fig,use_container_width=True)

st.metric("Current predicted shift",f"{fringe_shift(L,lam_nm*1e-9,v_kms*1000):.4f} fringe")
st.markdown("### Scaling laws")
st.latex(r"N_{\max}\propto L")
st.latex(r"N_{\max}\propto \frac{1}{\lambda}")
st.latex(r"N_{\max}\propto v^2")
st.markdown("These scaling relationships explain why a long effective optical path and a sufficiently sensitive fringe measurement were central to the experimental design.")
st.markdown('<div class="mm-footer"><strong>MM-1887 Virtual Laboratory</strong><br>Made with ❤️ by <strong>Aman Kumar Patel</strong></div>',unsafe_allow_html=True)
