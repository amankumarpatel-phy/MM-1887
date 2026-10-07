import streamlit as st
from utils import page_style, footer, apparatus_figure, classical_times, predicted_shift, DEFAULT_L, DEFAULT_LAMBDA_NM, DEFAULT_V_KMS

st.set_page_config(page_title="Experiment Setup | MM-1887", page_icon="⚙️", layout="wide")
page_style()
st.title("02 · Experiment Setup")
st.subheader("Configure the reconstructed 1887 interferometer")
c1,c2=st.columns([1,1.15])
with c1:
    L=st.number_input("Effective arm length, L (m)",0.1,1000.0,DEFAULT_L,0.5)
    lam_nm=st.number_input("Wavelength, λ (nm)",350.0,1000.0,DEFAULT_LAMBDA_NM,1.0)
    v_kms=st.number_input("Assumed ether-relative speed (km/s)",0.0,300000.0,DEFAULT_V_KMS,0.1)
    theta=st.slider("Orientation θ (°)",0.0,360.0,0.0,0.5)
    st.caption("The historical-inspired preset uses L ≈ 11 m and an Earth-orbital speed scale of ≈ 30 km/s.")
with c2:
    st.plotly_chart(apparatus_figure(theta),use_container_width=True)
lam=lam_nm*1e-9
v=v_kms*1e3
tpar,tperp=classical_times(L,v)
N=predicted_shift(L,lam,v)
st.markdown("### Live calculation")
a,b,c=st.columns(3)
a.metric("t∥",f"{tpar:.6e} s")
b.metric("t⊥",f"{tperp:.6e} s")
c.metric("Predicted fringe shift",f"{N:.4f}")
st.markdown("### Classical model")
st.latex(r"t_{\parallel}=\frac{L}{c-v}+\frac{L}{c+v}")
st.latex(r"t_{\perp}=\frac{2L}{\sqrt{c^2-v^2}}")
st.latex(r"N_{\max}=\frac{2L}{\lambda}\left(\frac{v}{c}\right)^2")
st.info("These equations describe the classical ether-drift prediction used for the historical test. They are not the relativistic description of light propagation.")
footer()
