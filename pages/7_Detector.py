import streamlit as st
import numpy as np
import plotly.graph_objects as go
from core.interference import interferogram, fringe_visibility

st.set_page_config(page_title="Detector | MM-1887", page_icon="📷", layout="wide")
st.title("07 · Detector")
st.subheader("Explore finite contrast, noise and fringe visibility")

visibility=st.slider("Fringe visibility",0.05,1.0,0.85,0.01)
noise=st.slider("Detector noise σ",0.0,0.30,0.03,0.005)
phase=st.slider("Phase offset (cycles)",-1.0,1.0,0.0,0.005)
orientation=st.slider("Fringe orientation (°)",0.0,180.0,0.0,0.5)
img=interferogram(phase,orientation,visibility=visibility,noise=noise)
fig=go.Figure(go.Heatmap(z=img,colorscale="Gray",zmin=0,zmax=1,colorbar=dict(title="I")))
fig.update_layout(height=620,margin=dict(l=5,r=5,t=20,b=5))
fig.update_yaxes(scaleanchor="x",scaleratio=1)
st.plotly_chart(fig,use_container_width=True)
c1,c2=st.columns(2)
c1.metric("Image contrast",f"{fringe_visibility(float(img.max()),float(img.min())):.3f}")
c2.metric("Noise σ",f"{noise:.3f}")
st.info("The detector page is intentionally synthetic: it demonstrates how finite contrast and noise can obscure a very small fringe displacement.")
st.markdown('<div class="mm-footer"><strong>MM-1887 Virtual Laboratory</strong><br>Made with ❤️ by <strong>Aman Kumar Patel</strong></div>',unsafe_allow_html=True)
