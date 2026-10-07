import streamlit as st
import plotly.graph_objects as go
from core.ether_model import fringe_shift

st.set_page_config(page_title="Prediction vs Observation | MM-1887", page_icon="⚖️", layout="wide")
st.title("09 · Prediction vs Observation")
st.subheader("The central historical comparison")

L=st.number_input("Effective arm length L (m)",0.1,1000.0,11.0,0.5)
lam_nm=st.number_input("Wavelength λ (nm)",350.0,1000.0,550.0,1.0)
v_kms=st.number_input("Assumed Earth-speed scale v (km/s)",0.0,100000.0,29.8,0.1)
obs=st.number_input("Historical observed displacement envelope (fringe)",0.001,0.10,0.01,0.001)

pred=fringe_shift(L,lam_nm*1e-9,v_kms*1000)
fig=go.Figure(go.Bar(x=["Classical prediction","Historical envelope"],y=[pred,obs],text=[f"{pred:.4f}",f"≤ {obs:.3f}"],textposition="auto"))
fig.update_layout(height=480,yaxis_title="Fringe displacement",margin=dict(l=20,r=20,t=30,b=20))
st.plotly_chart(fig,use_container_width=True)

c1,c2,c3=st.columns(3)
c1.metric("Classical prediction",f"{pred:.4f} fringe")
c2.metric("Historical envelope",f"≤ {obs:.3f} fringe")
c3.metric("Scale ratio",f"{pred/obs:.1f}×")

st.warning("The historical observation is represented as an envelope/scale, not as a digitized raw dataset.")
st.markdown("### Interpretation")
st.markdown("The historical result was much smaller than the classical ether-drift signal expected at the assumed orbital-speed scale. This challenged the stationary-ether hypothesis. The experiment should not be described as a standalone experimental 'proof' of Special Relativity.")
st.markdown('<div class="mm-footer"><strong>MM-1887 Virtual Laboratory</strong><br>Made with ❤️ by <strong>Aman Kumar Patel</strong></div>',unsafe_allow_html=True)
