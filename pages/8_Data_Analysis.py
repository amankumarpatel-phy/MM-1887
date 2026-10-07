import streamlit as st
import numpy as np
import plotly.graph_objects as go
from core.interference import synthetic_fringe_scan
from core.analysis import fit_second_harmonic

st.set_page_config(page_title="Data Analysis | MM-1887", page_icon="📈", layout="wide")
st.title("08 · Data Analysis")
st.subheader("Extract the second-harmonic signal from a rotation scan")

noise=st.slider("Measurement noise σ (fringe)",0.0,0.05,0.004,0.001)
A=st.slider("Synthetic signal amplitude (fringe)",0.0,0.30,0.20,0.005)
angles=np.linspace(0,360,181)
ideal,measured=synthetic_fringe_scan(angles,A,noise)
fit=fit_second_harmonic(angles,measured)

fig=go.Figure()
fig.add_trace(go.Scatter(x=angles,y=measured,mode="markers",name="Synthetic observations",marker=dict(size=5)))
fig.add_trace(go.Scatter(x=angles,y=fit["predicted"],mode="lines",name="2θ fit",line=dict(width=3)))
fig.update_layout(height=520,xaxis_title="θ (°)",yaxis_title="Fringe displacement",hovermode="x unified")
st.plotly_chart(fig,use_container_width=True)

c1,c2,c3,c4=st.columns(4)
c1.metric("Fitted amplitude",f"{fit['amplitude']:.5f}")
c2.metric("A coefficient",f"{fit['A']:.5f}")
c3.metric("B coefficient",f"{fit['B']:.5f}")
c4.metric("R²",f"{fit['r2']:.5f}")

st.latex(r"N(\theta)=A\cos(2\theta)+B\sin(2\theta)+C")
st.caption("The data here are synthetic so the analysis workflow can be explored without pretending to digitize the historical records.")
st.markdown('<div class="mm-footer"><strong>MM-1887 Virtual Laboratory</strong><br>Made with ❤️ by <strong>Aman Kumar Patel</strong></div>',unsafe_allow_html=True)
