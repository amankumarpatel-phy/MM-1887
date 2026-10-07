import streamlit as st
import plotly.graph_objects as go
from utils import page_style, footer, predicted_shift, DEFAULT_L, DEFAULT_LAMBDA_NM, DEFAULT_V_KMS

st.set_page_config(page_title="Results | MM-1887", page_icon="📊", layout="wide")
page_style()
st.title("05 · 1887 Result")
st.subheader("Classical prediction versus the historical null result")
L=st.number_input("Effective arm length, L (m)",0.1,1000.0,DEFAULT_L,0.5)
lam_nm=st.number_input("Wavelength, λ (nm)",350.0,1000.0,DEFAULT_LAMBDA_NM,1.0)
v_kms=st.number_input("Assumed speed, v (km/s)",0.0,300000.0,DEFAULT_V_KMS,0.1)
observed=st.number_input("Historical observed displacement envelope (fringe)",0.001,0.10,0.01,0.001)
pred=predicted_shift(L,lam_nm*1e-9,v_kms*1e3)
ratio=pred/observed
c1,c2=st.columns([1.2,1])
with c1:
    fig=go.Figure(go.Bar(x=["Classical prediction","Historical envelope"],y=[pred,observed],text=[f"{pred:.4f}",f"≤ {observed:.3f}"],textposition="auto"))
    fig.update_layout(height=450,yaxis_title="Fringe displacement",margin=dict(l=20,r=20,t=20,b=20))
    st.plotly_chart(fig,use_container_width=True)
with c2:
    st.metric("Classical prediction",f"{pred:.4f} fringe")
    st.metric("Historical envelope",f"≤ {observed:.3f} fringe")
    st.metric("Prediction / envelope",f"{ratio:.1f}×")
st.markdown("### Historical interpretation")
st.markdown("The 1887 paper reported a displacement much smaller than the classical ether-wind prediction. For the historical-inspired parameters, the expected signal is of order 0.4 fringe, while the reported displacement was no more than about 0.01 fringe.")
st.success("The reconstructed classical ether-drift signal is therefore inconsistent with the reported null result at the expected scale.")
st.info("This is the historical inference: the experiment strongly challenged the stationary-ether interpretation. It should not be phrased as “Michelson–Morley proved Special Relativity.”")
footer()
