import streamlit as st
import numpy as np
import plotly.graph_objects as go
from utils import page_style, footer, predicted_shift, DEFAULT_L, DEFAULT_LAMBDA_NM, DEFAULT_V_KMS

st.set_page_config(page_title="Rotation Analysis | MM-1887", page_icon="🔄", layout="wide")
page_style()
st.title("04 · Rotation Analysis")
st.subheader("Rotate the interferometer and search for the second-order signal")
c1,c2=st.columns([.8,1.8])
with c1:
    L=st.number_input("L (m)",0.1,1000.0,DEFAULT_L,0.5)
    lam_nm=st.number_input("λ (nm)",350.0,1000.0,DEFAULT_LAMBDA_NM,1.0)
    v_kms=st.number_input("v (km/s)",0.0,300000.0,DEFAULT_V_KMS,0.1)
    envelope=st.number_input("Illustrative null-result envelope (fringe)",0.001,0.10,0.01,0.001)
angles=np.linspace(0,360,721)
Nmax=predicted_shift(L,lam_nm*1e-9,v_kms*1e3)
pred=0.5*Nmax*np.cos(2*np.deg2rad(angles))
obs=0.006*np.sin(3*np.deg2rad(angles))
with c2:
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=angles,y=pred,mode="lines",name="Classical ether prediction",line=dict(width=3)))
    fig.add_trace(go.Scatter(x=angles,y=obs,mode="lines",name="Illustrative null trace",line=dict(width=2,dash="dash")))
    fig.add_hline(y=envelope,line_dash="dot",annotation_text="+ envelope")
    fig.add_hline(y=-envelope,line_dash="dot",annotation_text="− envelope")
    fig.update_layout(height=540,xaxis_title="Orientation θ (°)",yaxis_title="Fringe displacement",hovermode="x unified",margin=dict(l=20,r=20,t=20,b=20))
    st.plotly_chart(fig,use_container_width=True)
st.metric("Classical peak-to-peak signal",f"{Nmax:.4f} fringe")
st.markdown("### Why a 2θ dependence?")
st.markdown("Rotating the two perpendicular arms interchanges their roles relative to the hypothesized ether wind. The second-order differential therefore repeats after 180° and is represented by a cos(2θ) dependence in this compact reconstruction.")
st.latex(r"N(\theta)\propto\cos(2\theta)")
st.warning("The null trace is illustrative. It is not a digitization of the original 1887 fringe records.")
footer()
