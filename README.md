# Yohimbine Drug Chiral Center Analyzer (Python)

This project is implemented in **Python only** as a Streamlit public website for the
**yohimbine drug**. It visualizes a simplified 3D chiral center for yohimbine and
lets users switch between **R** and **S** configurations.

## Features

- Python-only web app (`app.py`)
- 2D benzene-ring style structure sketch with atom map labels (C1–C6) and highlighted chiral atom (C7*)
- Interactive 3D benzene-ring model rendered with Plotly, including an attached representative chiral center
- R/S toggle for stereochemistry learning
- Stereocenter summary (highlighted center in view + total estimated stereocenters)
- CIP-based explanation for assignment rules
- Student details shown in the app sidebar corner

## Run locally

```bash
python3 -m pip install -r requirements.txt
streamlit run app.py
```
