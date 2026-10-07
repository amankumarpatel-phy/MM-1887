import math
import numpy as np
import streamlit as st

C = 299_792_458.0
DEFAULT_L = 11.0
DEFAULT_LAMBDA_NM = 550.0
DEFAULT_V_KMS = 29.8

def page_style():
    st.markdown("""
    <style>
    .mm-footer { margin-top: 3rem; padding: 1rem 0 0.25rem 0; border-top: 1px solid rgba(128,128,128,.28); text-align:center; color:#777; font-size:.86rem; }
    .mm-footer strong { color: inherit; }
    </style>
    """, unsafe_allow_html=True)

def footer():
    st.markdown("""
    <div class="mm-footer">
      <strong>MM-1887 Virtual Laboratory</strong><br>
      Made with ❤️ by <strong>Aman Kumar Patel</strong>
    </div>
    """, unsafe_allow_html=True)

def classical_times(L, v):
    beta = v / C
    if abs(beta) >= 1:
        raise ValueError("The assumed speed must be less than c.")
    t_parallel = 2 * L * C / (C**2 - v**2)
    t_perpendicular = 2 * L / (C * math.sqrt(1 - beta**2))
    return t_parallel, t_perpendicular

def predicted_shift(L, wavelength, v):
    return 2 * L * (v / C)**2 / wavelength

def orientation_signal(L, wavelength, v, theta_deg):
    nmax = predicted_shift(L, wavelength, v)
    return 0.5 * nmax * np.cos(2 * np.deg2rad(theta_deg))

def fringe_pattern(phase_cycles, orientation_deg, size=420, span=7.0, noise=0.0, seed=1887):
    x = np.linspace(-span, span, size)
    y = np.linspace(-span, span, size)
    X, Y = np.meshgrid(x, y)
    th = np.deg2rad(orientation_deg)
    carrier = 2*np.pi*0.34*(X*np.cos(th) + Y*np.sin(th))
    envelope = np.exp(-(X**2 + Y**2)/52)
    intensity = 0.5 + 0.5*np.cos(carrier + 2*np.pi*phase_cycles)
    intensity = 0.12 + 0.88*(intensity*envelope + 0.5*(1-envelope))
    if noise > 0:
        rng = np.random.default_rng(seed)
        intensity = np.clip(intensity + rng.normal(0, noise, intensity.shape), 0, 1)
    return intensity

def apparatus_figure(theta_deg=0):
    import plotly.graph_objects as go
    th = np.deg2rad(theta_deg)
    a = np.array([2.7*np.cos(th), 2.7*np.sin(th)])
    b = np.array([2.7*np.cos(th+np.pi/2), 2.7*np.sin(th+np.pi/2)])
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[-2.2,0],y=[0,0],mode="lines",line=dict(width=7),showlegend=False))
    fig.add_trace(go.Scatter(x=[0,a[0]],y=[0,a[1]],mode="lines",line=dict(width=7),showlegend=False))
    fig.add_trace(go.Scatter(x=[0,b[0]],y=[0,b[1]],mode="lines",line=dict(width=7),showlegend=False))
    fig.add_trace(go.Scatter(x=[-0.2,0.2],y=[-0.2,0.2],mode="lines",line=dict(width=9),showlegend=False))
    for p, ang in [(a,th+np.pi/2),(b,th)]:
        q=.27*np.array([np.cos(ang),np.sin(ang)])
        fig.add_trace(go.Scatter(x=[p[0]-q[0],p[0]+q[0]],y=[p[1]-q[1],p[1]+q[1]],mode="lines",line=dict(width=11),showlegend=False))
    fig.add_annotation(x=-1.9,y=.35,text="Light source",showarrow=False)
    fig.add_annotation(x=.35,y=.3,text="Beam splitter",showarrow=False)
    fig.add_annotation(x=a[0]*1.05,y=a[1]*1.05,text="M₁",showarrow=False)
    fig.add_annotation(x=b[0]*1.05,y=b[1]*1.05,text="M₂",showarrow=False)
    fig.add_annotation(x=-1.6,y=-.35,text="Detector / eyepiece",showarrow=False)
    fig.update_layout(height=450,margin=dict(l=10,r=10,t=10,b=10),showlegend=False,paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)")
    fig.update_xaxes(visible=False,range=[-3.2,3.3])
    fig.update_yaxes(visible=False,range=[-3.2,3.2],scaleanchor="x",scaleratio=1)
    return fig
