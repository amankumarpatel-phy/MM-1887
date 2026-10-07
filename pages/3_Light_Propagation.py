import streamlit as st
import plotly.graph_objects as go
import numpy as np
from core.interferometer import ray_segments

st.set_page_config(page_title="Light Propagation | MM-1887", page_icon="💡", layout="wide")
st.title("03 · Light Propagation")
st.subheader("Follow the beam through the interferometer")

theta=st.slider("Orientation θ (°)",0.0,360.0,0.0,1.0)
historical=st.checkbox("Use multi-reflection path",True)
progress=st.slider("Propagation progress",0.0,1.0,1.0,0.01)

pts=np.array(ray_segments(theta,historical))
if len(pts)>1:
    d=np.sqrt(np.sum(np.diff(pts,axis=0)**2,axis=1))
    s=np.r_[0,np.cumsum(d)]
    target=progress*s[-1]
    j=np.searchsorted(s,target)
    if j>=len(pts): j=len(pts)-1
    if j==0: current=pts[0]
    else:
        frac=(target-s[j-1])/(s[j]-s[j-1]) if s[j]!=s[j-1] else 0
        current=pts[j-1]+frac*(pts[j]-pts[j-1])
    drawn=pts[:j+1]
    if j>0: drawn=np.vstack([drawn,current])

fig=go.Figure()
fig.add_trace(go.Scatter(x=pts[:,0],y=pts[:,1],mode="lines",line=dict(width=3,dash="dot"),name="Optical path"))
fig.add_trace(go.Scatter(x=drawn[:,0],y=drawn[:,1],mode="lines",line=dict(width=7),name="Propagating beam"))
fig.add_trace(go.Scatter(x=[current[0]],y=[current[1]],mode="markers",marker=dict(size=18),name="Photon packet"))
fig.update_layout(height=560,xaxis=dict(visible=False,range=[-3.3,3.3]),yaxis=dict(visible=False,range=[-3.3,3.3],scaleanchor="x",scaleratio=1),margin=dict(l=10,r=10,t=10,b=10))
st.plotly_chart(fig,use_container_width=True)
st.progress(progress,text=f"Propagation: {progress*100:.0f}%")
st.markdown("The visualization is a ray-path representation of the interferometric geometry. The underlying timing and fringe calculations remain wave/phase calculations.")
st.markdown('<div class="mm-footer"><strong>MM-1887 Virtual Laboratory</strong><br>Made with ❤️ by <strong>Aman Kumar Patel</strong></div>',unsafe_allow_html=True)
