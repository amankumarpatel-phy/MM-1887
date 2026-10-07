# MM-1887 Virtual Laboratory

## Computational Reconstruction of the Michelson–Morley Experiment, 1887

A multi-page **Python + Streamlit** virtual laboratory for exploring the classical ether-drift prediction, interference fringes, rotation dependence and the historical null result of the Michelson–Morley experiment.

### Laboratory pages

1. **Overview** — historical motivation and experimental question
2. **Experiment Setup** — configure the interferometer and calculate travel times
3. **Interference Pattern** — generate a numerical detector interferogram
4. **Rotation Analysis** — rotate the virtual apparatus and inspect the predicted second-order signal
5. **1887 Result** — compare the classical prediction with the historical null-result scale
6. **Theory** — equations, assumptions and historical context

### Physics

The core classical prediction is

Nmax = 2L/λ × (v/c)²

For the historical-inspired scale L ≈ 11 m, v ≈ 30 km/s and visible light near 550 nm, the predicted displacement is approximately 0.4 fringe.

### Historical note

The original experiment used a massive stone platform floated on mercury to permit rotation and employed multiple reflections to obtain a long effective optical path. The reported result was a null displacement much smaller than the classical prediction.

This repository is a **computational reconstruction**, not a digitization of the original raw observation records. The null trace shown in the Rotation Analysis page is explicitly illustrative.

### Run locally

Install the dependencies and start Streamlit with:

    pip install -r requirements.txt
    streamlit run app.py

### Project identity

**MM-1887 Virtual Laboratory**  
*Computational Interferometry & Historical Experimental Physics*

Made with ❤️ by **Aman Kumar Patel** · Physics Educator · Condensed Matter Physics  
**Aman Edge Physics** · Computational Physics & Scientific Visualization
