import streamlit as st
import plotly.graph_objects as go
import numpy as np
from core.interferometer import ray_segments

st.set_page_config(page_title="Historical Reconstruction | MM-1887", page_icon="🏛️", layout="wide")
st.title("01 · Historical Reconstruction")
st.subheader("Rebuilding the optical idea behind the 1887 experiment")

st.markdown("""
The historical instrument was not simply a two-mirror classroom interferometer. Michelson and Morley used
additional reflections to obtain a long effective optical path and mounted the optical assembly on a massive
stone platform floated in mercury so that its orientation could be changed.
""")

extended = st.toggle("Show multi-reflection historical-inspired path", True)
theta = st.slider("Platform orientation θ (°)", 0.0, 360.0, 0.0, 1.0)

fig = go.Figure()
pts = ray_segments(theta, extended=extended)
xy=np.array(pts)
fig.add_trace(go.Scatter(x=xy[:,0],y=xy[:,1],mode="lines+markers",line=dict(width=5),marker=dict(size=7)))
fig.add_trace(go.Scatter(x=[0],y=[0],mode="markers",marker=dict(size=18,symbol="diamond"),name="Beam splitter"))
fig.add_annotation(x=-2.2,y=.25,text="Source",showarrow=False)
fig.add_annotation(x=0.2,y=.28,text="Beam splitter",showarrow=False)
fig.update_layout(height=600,margin=dict(l=10,r=10,t=10,b=10),showlegend=False,
                  xaxis=dict(visible=False,range=[-3.3,3.3]),
                  yaxis=dict(visible=False,range=[-3.3,3.3],scaleanchor="x",scaleratio=1))
st.plotly_chart(fig,use_container_width=True)

c1,c2,c3=st.columns(3)
c1.metric("Platform angle",f"{theta:.0f}°")
c2.metric("Configuration","Multi-reflection" if extended else "Simplified")
c3.metric("Historical feature","Mercury-floated rotation")

st.info("The geometry is a physics-oriented reconstruction, not a scale drawing. Its purpose is to make the long optical path and rotational measurement concept explicit.")
st.markdown("### Why the long path mattered")
st.markdown("The expected ether-drift effect is second order in v/c. Increasing the effective optical path increased the phase sensitivity of the interferometer.")
st.latex(r"N_{\max}=\frac{2L}{\lambda}\left(\frac{v}{c}\right)^2")
st.markdown('<div class="mm-footer"><strong>MM-1887 Virtual Laboratory</strong><br>Made with ❤️ by <strong>Aman Kumar Patel</strong></div>',unsafe_allow_html=True)
