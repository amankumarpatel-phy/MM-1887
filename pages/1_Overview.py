import streamlit as st
from utils import page_style, footer

st.set_page_config(page_title="Overview | MM-1887", page_icon="📜", layout="wide")
page_style()
st.title("01 · Overview")
st.subheader("Why was the experiment performed?")
st.markdown("""
In the nineteenth-century ether picture, light was assumed to propagate through a stationary **luminiferous ether**. Because Earth moves around the Sun, the laboratory should then experience an effective "ether wind" whose direction changes as the apparatus rotates.

Michelson and Morley designed an interferometer to search for the resulting difference in light travel time along two perpendicular arms.
""")
c1,c2=st.columns(2)
with c1:
    st.markdown("### Experimental idea")
    st.markdown("""
    - Split one beam into two perpendicular paths.
    - Reflect both beams back to the beam splitter.
    - Recombine them to form interference fringes.
    - Rotate the apparatus.
    - Search for a systematic fringe displacement.
    """)
with c2:
    st.markdown("### Historical features reproduced here")
    st.markdown("""
    - Long effective optical path produced by multiple reflections.
    - Massive rotating platform floated on mercury.
    - Orientation scan through 360°.
    - Classical ether-wind prediction.
    - Comparison with the reported null result.
    """)
st.warning("The application is a computational reconstruction. The apparatus illustration is schematic and is not a scale drawing of the 1887 instrument.")
st.markdown("### The experimental question")
st.latex(r"\text{Does rotation produce the predicted change in optical path difference?}")
st.markdown("### Historical outcome")
st.markdown("""
The 1887 paper reported that the displacement attributable to the Earth's motion through the ether was much smaller than the classical prediction. This became an important experimental challenge to the stationary-ether picture, although the experiment itself should not be described as a standalone derivation or proof of Special Relativity.
""")
footer()
