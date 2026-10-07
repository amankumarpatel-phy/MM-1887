import numpy as np

def interferogram(phase_cycles=0.0, orientation_deg=0.0, size=500, span=7.0, visibility=0.92, noise=0.0, seed=1887):
    x = np.linspace(-span, span, size)
    y = np.linspace(-span, span, size)
    X, Y = np.meshgrid(x, y)
    th = np.deg2rad(orientation_deg)
    carrier = 2*np.pi*0.34*(X*np.cos(th) + Y*np.sin(th))
    envelope = np.exp(-(X**2 + Y**2)/52)
    field = 0.5 + 0.5*visibility*np.cos(carrier + 2*np.pi*phase_cycles)
    image = 0.10 + 0.90*(field*envelope + 0.5*(1-envelope))
    if noise:
        rng = np.random.default_rng(seed)
        image = np.clip(image + rng.normal(0, noise, image.shape), 0, 1)
    return image

def fringe_visibility(Imax, Imin):
    return (Imax-Imin)/(Imax+Imin)

def synthetic_fringe_scan(angles, amplitude, noise_sigma=0.0, seed=1887):
    rng = np.random.default_rng(seed)
    ideal = amplitude*np.cos(2*np.deg2rad(angles))
    measured = ideal + rng.normal(0, noise_sigma, len(angles))
    return ideal, measured
