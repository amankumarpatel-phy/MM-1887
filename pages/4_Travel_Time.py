import streamlit as st
import numpy as np
import plotly.graph_objects as go
from core.ether_model import round_trip_times, fringe_shift, C

st.set_page_config(page_title="Travel Time | MM-1887", page_icon="⏱️", layout="wide")
st.title("04 · Travel-Time Laboratory")
st.subheader("Resolve the tiny second-order difference predicted by the ether model")

L=st.number_input("Effective arm length L (m)",0.1,1000.0,11.0,0.5)
v_kms=st.number_input("Assumed speed v (km/s)",0.0,100000.0,29.8,0.1)
lam_nm=st.number_input("Wavelength λ (nm)",350.0,1000.0,550.0,1.0)

v=v_kms*1000
tpar,tperp=round_trip_times(L,v)
dt=tpar-tperp
N=fringe_shift(L,lam_nm*1e-9,v)

a,b,c,d=st.columns(4)
a.metric("t∥",f"{tpar:.9e} s")
b.metric("t⊥",f"{tperp:.9e} s")
c.metric("Δt",f"{dt:.3e} s")
d.metric("Predicted shift",f"{N:.4f} fringe")

st.markdown("### Scale of the effect")
x=np.array([tpar,tperp])
fig=go.Figure(go.Bar(x=["Parallel","Perpendicular"],y=x,text=[f"{z:.12e}" for z in x],textposition="outside"))
fig.update_layout(height=400,yaxis_title="Round-trip time (s)",margin=dict(l=20,r=20,t=30,b=20))
st.plotly_chart(fig,use_container_width=True)

st.latex(r"t_{\parallel}=\frac{L}{c-v}+\frac{L}{c+v}")
st.latex(r"t_{\perp}=\frac{2L}{\sqrt{c^2-v^2}}")
st.latex(r"N_{\max}=\frac{2L}{\lambda}\left(\frac{v}{c}\right)^2")
st.caption(f"c = {C:,.0f} m/s. The plotted difference is extremely small because the predicted effect scales as (v/c)².")
st.markdown('<div class="mm-footer"><strong>MM-1887 Virtual Laboratory</strong><br>Made with ❤️ by <strong>Aman Kumar Patel</strong></div>',unsafe_allow_html=True)
