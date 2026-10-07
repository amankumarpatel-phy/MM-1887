import streamlit as st

st.set_page_config(page_title="Theory | MM-1887", page_icon="📐", layout="wide")
st.title("11 · Theory")
st.subheader("From the ether hypothesis to the null result")

sections=[
("Parallel arm",r"t_{\parallel}=\frac{L}{c-v}+\frac{L}{c+v}=\frac{2Lc}{c^2-v^2}"),
("Perpendicular arm",r"t_{\perp}=\frac{2L}{\sqrt{c^2-v^2}}"),
("Differential time",r"\Delta t=t_{\parallel}-t_{\perp}"),
("Second-order fringe shift",r"N_{\max}=\frac{2L}{\lambda}\left(\frac{v}{c}\right)^2"),
("Rotation dependence",r"N(\theta)\propto\cos(2\theta)")
]
for title,equation in sections:
    st.markdown(f"### {title}")
    st.latex(equation)

st.markdown("### Historical interpretation")
st.markdown("Michelson and Morley were testing the luminiferous-ether hypothesis. Their null result became a major experimental fact in the development of modern relativity, but it is historically inaccurate to describe the 1887 experiment alone as a direct proof of Einstein's 1905 Special Relativity.")
st.markdown("### Computational scope")
st.markdown("This laboratory models the classical ether prediction, interferometric phase/fringe visualization, rotation analysis and synthetic measurement fitting. It intentionally labels synthetic data separately from historical observations.")
st.markdown('<div class="mm-footer"><strong>MM-1887 Virtual Laboratory</strong><br>Made with ❤️ by <strong>Aman Kumar Patel</strong></div>',unsafe_allow_html=True)
