import streamlit as st
import plotly.graph_objects as go
from core.ether_model import fringe_shift
from core.interference import interferogram, fringe_visibility

st.set_page_config(page_title="Interference | MM-1887", page_icon="〰️", layout="wide")
st.title("05 · Interference")
st.subheader("From phase difference to visible fringes")

L=st.number_input("Effective arm length L (m)",0.1,1000.0,11.0,0.5)
lam_nm=st.number_input("Wavelength λ (nm)",350.0,1000.0,550.0,1.0)
v_kms=st.number_input("Assumed speed v (km/s)",0.0,100000.0,29.8,0.1)
theta=st.slider("Orientation θ (°)",0.0,360.0,0.0,0.5)
visibility=st.slider("Fringe visibility",0.05,1.0,0.92,0.01)
noise=st.slider("Detector noise σ",0.0,0.25,0.015,0.005)

N=fringe_shift(L,lam_nm*1e-9,v_kms*1000)
phase=0.5*N
img=interferogram(phase,theta,visibility=visibility,noise=noise)
fig=go.Figure(go.Heatmap(z=img,colorscale="Gray",zmin=0,zmax=1,colorbar=dict(title="I")))
fig.update_layout(height=650,xaxis_title="Detector x",yaxis_title="Detector y",margin=dict(l=5,r=5,t=20,b=5))
fig.update_yaxes(scaleanchor="x",scaleratio=1)
st.plotly_chart(fig,use_container_width=True)

c1,c2,c3=st.columns(3)
c1.metric("Classical Nmax",f"{N:.4f}")
c2.metric("Phase contribution",f"{phase:.4f} cycles")
c3.metric("Input visibility",f"{visibility:.2f}")
st.latex(r"I(x,y)=I_1+I_2+2\sqrt{I_1I_2}\cos(\Delta\phi)")
st.caption("This is a synthetic numerical interferogram. It is not a digitized photograph of the 1887 detector view.")
st.markdown('<div class="mm-footer"><strong>MM-1887 Virtual Laboratory</strong><br>Made with ❤️ by <strong>Aman Kumar Patel</strong></div>',unsafe_allow_html=True)
