import streamlit as st
import plotly.graph_objects as go
import numpy as np
from core.interferometer import rotated_arms

st.set_page_config(page_title="Interferometer Setup | MM-1887", page_icon="⚙️", layout="wide")
st.title("02 · Interferometer Setup")
st.subheader("Configure the virtual optical bench")

L=st.number_input("Effective arm length L (m)",0.1,1000.0,11.0,0.5)
lam_nm=st.number_input("Wavelength λ (nm)",350.0,1000.0,550.0,1.0)
v_kms=st.number_input("Assumed ether-relative speed (km/s)",0.0,100000.0,29.8,0.1)
theta=st.slider("Orientation θ (°)",0.0,360.0,0.0,0.5)
show_beams=st.checkbox("Show bidirectional beam paths",True)

a,b=rotated_arms(theta)
fig=go.Figure()
fig.add_trace(go.Scatter(x=[-2.3,0],y=[0,0],mode="lines",line=dict(width=8),name="Incident beam"))
for p,name in [(a,"Arm 1"),(b,"Arm 2")]:
    fig.add_trace(go.Scatter(x=[0,p[0]],y=[0,p[1]],mode="lines",line=dict(width=8),name=name))
    if show_beams:
        fig.add_trace(go.Scatter(x=[p[0],0],y=[p[1],0],mode="lines",line=dict(width=4,dash="dot"),showlegend=False))
fig.add_trace(go.Scatter(x=[-0.2,0.2],y=[-0.2,0.2],mode="lines",line=dict(width=10),name="Beam splitter"))
fig.update_layout(height=520,xaxis=dict(visible=False,range=[-3.2,3.2]),yaxis=dict(visible=False,range=[-3.2,3.2],scaleanchor="x",scaleratio=1),margin=dict(l=10,r=10,t=10,b=10))
st.plotly_chart(fig,use_container_width=True)

c1,c2,c3=st.columns(3)
c1.metric("L",f"{L:.2f} m")
c2.metric("λ",f"{lam_nm:.1f} nm")
c3.metric("v",f"{v_kms:.2f} km/s")
st.markdown("### Historical-inspired instrument controls")
st.markdown("Use **L** as the effective optical-arm scale rather than treating the visible drawing length as a literal historical dimension. The original design used multiple reflections to increase the optical path.")
st.markdown('<div class="mm-footer"><strong>MM-1887 Virtual Laboratory</strong><br>Made with ❤️ by <strong>Aman Kumar Patel</strong></div>',unsafe_allow_html=True)
