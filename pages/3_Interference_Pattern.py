import streamlit as st
import plotly.graph_objects as go
from utils import page_style, footer, fringe_pattern, orientation_signal, DEFAULT_L, DEFAULT_LAMBDA_NM, DEFAULT_V_KMS

st.set_page_config(page_title="Interference Pattern | MM-1887", page_icon="〰️", layout="wide")
page_style()
st.title("03 · Interference Pattern")
st.subheader("Visualize the recombined detector field")
c1,c2=st.columns([.8,1.6])
with c1:
    L=st.number_input("L (m)",0.1,1000.0,DEFAULT_L,0.5)
    lam_nm=st.number_input("λ (nm)",350.0,1000.0,DEFAULT_LAMBDA_NM,1.0)
    v_kms=st.number_input("v (km/s)",0.0,300000.0,DEFAULT_V_KMS,0.1)
    theta=st.slider("Orientation θ (°)",0.0,360.0,0.0,0.5)
    noise=st.slider("Detector noise",0.0,0.25,0.02,0.005)
with c2:
    phase_cycles=orientation_signal(L,lam_nm*1e-9,v_kms*1e3,theta)
    img=fringe_pattern(phase_cycles,theta,noise=noise)
    fig=go.Figure(go.Heatmap(z=img,colorscale="Gray",zmin=0,zmax=1,colorbar=dict(title="Intensity")))
    fig.update_layout(height=610,margin=dict(l=5,r=5,t=20,b=5),xaxis_title="Detector x",yaxis_title="Detector y")
    fig.update_yaxes(scaleanchor="x",scaleratio=1)
    st.plotly_chart(fig,use_container_width=True)
st.markdown("### What is being visualized?")
st.markdown("The detector intensity is generated from the phase difference between the recombined beams. The image is a numerical interferogram: it is designed to expose fringe motion and phase changes rather than reproduce a historical photograph.")
st.latex(r"I=I_1+I_2+2\sqrt{I_1I_2}\cos(\Delta\phi)")
st.metric("Orientation-dependent phase contribution",f"{phase_cycles:.6f} cycles")
footer()
