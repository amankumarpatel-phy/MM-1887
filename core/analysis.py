import numpy as np

def fit_second_harmonic(theta_deg, signal):
    theta = np.deg2rad(np.asarray(theta_deg))
    y = np.asarray(signal)
    X = np.column_stack([np.cos(2*theta), np.sin(2*theta), np.ones_like(theta)])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    pred = X @ beta
    ss_res = np.sum((y-pred)**2)
    ss_tot = np.sum((y-np.mean(y))**2)
    r2 = 1 - ss_res/ss_tot if ss_tot else 1.0
    amplitude = float(np.hypot(beta[0], beta[1]))
    phase_deg = float(np.rad2deg(np.arctan2(-beta[1], beta[0]))/2)
    return {"A":float(beta[0]),"B":float(beta[1]),"offset":float(beta[2]),"amplitude":amplitude,"phase_deg":phase_deg,"r2":float(r2),"predicted":pred}

def detect_fringe_contrast(image):
    im = np.asarray(image)
    return float((np.max(im)-np.min(im))/(np.max(im)+np.min(im)))
