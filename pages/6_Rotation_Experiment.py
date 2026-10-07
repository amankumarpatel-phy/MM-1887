import streamlit as st
import numpy as np
import plotly.graph_objects as go
from core.ether_model import fringe_shift
from core.interference import synthetic_fringe_scan

st.set_page_config(page_title="Rotation Experiment | MM-1887", page_icon="🔄", layout="wide")
st.title("06 · Rotation Experiment")
st.subheader("Rotate the virtual apparatus through 360°")

L=st.number_input("Effective arm length L (m)",0.1,1000.0,11.0,0.5)
lam_nm=st.number_input("Wavelength λ (nm)",350.0,1000.0,550.0,1.0)
v_kms=st.number_input("Assumed speed v (km/s)",0.0,100000.0,29.8,0.1)
noise=st.slider("Synthetic measurement noise",0.0,0.05,0.003,0.001)
angles=np.linspace(0,360,721)
N=fringe_shift(L,lam_nm*1e-9,v_kms*1000)
ideal,measured=synthetic_fringe_scan(angles,0.5*N,noise)
fig=go.Figure()
fig.add_trace(go.Scatter(x=angles,y=ideal,name="Classical prediction",line=dict(width=4)))
fig.add_trace(go.Scatter(x=angles,y=measured,name="Synthetic measurement",mode="lines",line=dict(width=1)))
fig.update_layout(height=560,xaxis_title="Orientation θ (°)",yaxis_title="Fringe displacement",hovermode="x unified")
st.plotly_chart(fig,use_container_width=True)
st.metric("Peak-to-peak classical signal",f"{N:.4f} fringe")
st.latex(r"N(\theta)=A\cos(2\theta)")
st.markdown("The two-arm geometry repeats after 180°, giving the characteristic second-harmonic angular dependence in the classical prediction.")
st.markdown('<div class="mm-footer"><strong>MM-1887 Virtual Laboratory</strong><br>Made with ❤️ by <strong>Aman Kumar Patel</strong></div>',unsafe_allow_html=True)
