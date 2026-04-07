"""Streamlit app for yohimbine chiral center R/S visualization."""

from __future__ import annotations

import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Yohimbine Drug Chiral Center Explorer", layout="wide")

st.title("Yohimbine Drug: Chiral Center Explorer")
st.write(
    "Public chemistry project for the **yohimbine drug**: visualize one representative "
    "stereocenter and switch between **R** and **S** configurations in 3D."
)

st.info(
    "Drug focus: **Yohimbine** (an indole alkaloid). "
    "This model is a simplified educational view of a single chiral center."
)

with st.sidebar:
    st.markdown("### Student Details")
    st.markdown(
        """
**Name:** Meka yaswanth sai  
**Reg No:** RA2511026050022  
**Dept:** CSE-AIML  
**Section:** A
"""
    )

config = st.radio("Choose R/S configuration for the Yohimbine center", ["R", "S"], horizontal=True)

stereo_layouts = {
    "R": {
        "Priority 1: Hetero-group": (1.4, 0.6, 0.6),
        "Priority 2: Drug ring fragment": (-1.2, 0.9, 0.35),
        "Priority 3: CH2 side fragment": (0.2, -1.1, 1.25),
        "Priority 4: H": (0.25, 0.05, -1.5),
    },
    "S": {
        "Priority 1: Hetero-group": (1.4, 0.6, 0.6),
        "Priority 2: Drug ring fragment": (0.2, -1.1, 1.25),
        "Priority 3: CH2 side fragment": (-1.2, 0.9, 0.35),
        "Priority 4: H": (0.25, 0.05, -1.5),
    },
}

colors = {
    "C*": "#facc15",
    "Priority 1: Hetero-group": "#f87171",
    "Priority 2: Drug ring fragment": "#60a5fa",
    "Priority 3: CH2 side fragment": "#34d399",
    "Priority 4: H": "#e5e7eb",
}

layout = stereo_layouts[config]

def build_2d_structure_figure() -> go.Figure:
    """Return a benzene-ring style 2D map with atom numbering and chiral marker."""
    fig2d = go.Figure()

    # Benzene ring sketch with atom map indices 1..6
    ring_x = [0.0, 1.0, 2.0, 2.0, 1.0, 0.0, 0.0]
    ring_y = [0.0, 0.9, 0.0, -1.2, -2.1, -1.2, 0.0]
    fig2d.add_trace(
        go.Scatter(
            x=ring_x,
            y=ring_y,
            mode="lines",
            line={"width": 3, "color": "#93c5fd"},
            name="Benzene ring map",
            hoverinfo="skip",
        )
    )

    # Aromatic double-bond guide lines (visual)
    fig2d.add_trace(
        go.Scatter(
            x=[0.2, 1.0, 1.8],
            y=[-0.2, 0.55, -0.2],
            mode="lines",
            line={"width": 2, "color": "#bfdbfe"},
            showlegend=False,
            hoverinfo="skip",
        )
    )
    fig2d.add_trace(
        go.Scatter(
            x=[0.2, 1.0, 1.8],
            y=[-1.0, -1.65, -1.0],
            mode="lines",
            line={"width": 2, "color": "#bfdbfe"},
            showlegend=False,
            hoverinfo="skip",
        )
    )

    # Side-chain to representative stereocenter
    fig2d.add_trace(
        go.Scatter(
            x=[2.0, 2.8, 3.6],
            y=[0.0, 0.4, 0.1],
            mode="lines+text",
            text=["", "", "N/O-group"],
            textposition="top center",
            line={"width": 3, "color": "#fca5a5"},
            showlegend=False,
        )
    )

    # Ring atom map labels
    ring_labels = [("1", 0.0, 0.0), ("2", 1.0, 0.9), ("3", 2.0, 0.0), ("4", 2.0, -1.2), ("5", 1.0, -2.1), ("6", 0.0, -1.2)]
    for atom_id, x, y in ring_labels:
        fig2d.add_trace(
            go.Scatter(
                x=[x],
                y=[y],
                mode="markers+text",
                marker={"size": 10, "color": "#1f2937", "line": {"color": "#cbd5e1", "width": 1}},
                text=[f"C{atom_id}"],
                textposition="bottom center",
                showlegend=False,
                hoverinfo="skip",
            )
        )

    # Highlight representative stereocenter attached to ring
    fig2d.add_trace(
        go.Scatter(
            x=[2.8],
            y=[0.4],
            mode="markers+text",
            marker={"size": 16, "color": "#facc15", "line": {"color": "#111827", "width": 2}},
            text=["C* (Atom 7)"],
            textposition="top right",
            name="Chiral center",
        )
    )

    fig2d.update_layout(
        title="2D structure with benzene-ring atom map (educational)",
        xaxis={"visible": False},
        yaxis={"visible": False, "scaleanchor": "x", "scaleratio": 1},
        margin={"l": 0, "r": 0, "t": 45, "b": 0},
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
    )
    return fig2d


fig = go.Figure()

# 3D benzene ring coordinates (z = 0 plane)
benzene = [
    (0.0, 0.0, 0.0),
    (1.0, 0.9, 0.0),
    (2.0, 0.0, 0.0),
    (2.0, -1.2, 0.0),
    (1.0, -2.1, 0.0),
    (0.0, -1.2, 0.0),
]

for i in range(6):
    x1, y1, z1 = benzene[i]
    x2, y2, z2 = benzene[(i + 1) % 6]
    fig.add_trace(
        go.Scatter3d(
            x=[x1, x2],
            y=[y1, y2],
            z=[z1, z2],
            mode="lines",
            line={"color": "#93c5fd", "width": 7},
            showlegend=False,
            hoverinfo="skip",
        )
    )

for idx, (x, y, z) in enumerate(benzene, start=1):
    fig.add_trace(
        go.Scatter3d(
            x=[x],
            y=[y],
            z=[z],
            mode="markers+text",
            marker={"size": 7, "color": "#cbd5e1"},
            text=[f"C{idx}"],
            textposition="bottom center",
            showlegend=False,
            hoverinfo="skip",
        )
    )

# Representative chiral carbon attached to benzene ring at C3
anchor = benzene[2]
chiral_center = (2.8, 0.45, 0.2)
fig.add_trace(
    go.Scatter3d(
        x=[anchor[0], chiral_center[0]],
        y=[anchor[1], chiral_center[1]],
        z=[anchor[2], chiral_center[2]],
        mode="lines",
        line={"color": "#fcd34d", "width": 8},
        showlegend=False,
        hoverinfo="skip",
    )
)
fig.add_trace(
    go.Scatter3d(
        x=[chiral_center[0]],
        y=[chiral_center[1]],
        z=[chiral_center[2]],
        mode="markers+text",
        marker={"size": 11, "color": colors["C*"]},
        text=["C7*"],
        textposition="top center",
        name="Chiral center",
    )
)

for label, (x, y, z) in layout.items():
    sx, sy, sz = chiral_center[0] + x * 0.6, chiral_center[1] + y * 0.6, chiral_center[2] + z * 0.6
    fig.add_trace(
        go.Scatter3d(
            x=[chiral_center[0], sx],
            y=[chiral_center[1], sy],
            z=[chiral_center[2], sz],
            mode="lines",
            line={"color": "#cbd5e1", "width": 5},
            showlegend=False,
            hoverinfo="skip",
        )
    )
    fig.add_trace(
        go.Scatter3d(
            x=[sx],
            y=[sy],
            z=[sz],
            mode="markers+text",
            marker={"size": 8, "color": colors[label]},
            text=[label],
            textposition="top center",
            name=label,
        )
    )

fig.update_layout(
    margin={"l": 0, "r": 0, "t": 20, "b": 0},
    scene={
        "xaxis": {"visible": False},
        "yaxis": {"visible": False},
        "zaxis": {"visible": False},
        "camera": {"eye": {"x": 1.8, "y": 1.3, "z": 1.3}},
        "aspectmode": "cube",
        "bgcolor": "#020617",
    },
    paper_bgcolor="#020617",
    plot_bgcolor="#020617",
    legend={"orientation": "h", "yanchor": "bottom", "y": -0.1, "x": 0},
)

left_col, right_col = st.columns([1, 1.3])

with left_col:
    st.plotly_chart(build_2d_structure_figure(), use_container_width=True)
    st.caption("2D benzene-ring style atom map with a highlighted representative stereocenter.")

with right_col:
    st.plotly_chart(fig, use_container_width=True)

clockwise = "clockwise" if config == "R" else "counterclockwise"
st.success(
    f"{config} configuration: with priority 4 pointed away, "
    f"1 → 2 → 3 traces {clockwise}."
)

st.subheader("How R/S assignment works")
st.markdown(
    """
1. Assign substituent priorities (1 highest to 4 lowest) using Cahn–Ingold–Prelog rules.
2. Orient priority 4 away from the viewer.
3. Trace 1 → 2 → 3:
   - clockwise = **R**
   - counterclockwise = **S**

Yohimbine contains multiple chiral centers; this app intentionally focuses on one
representative tetrahedral center to teach stereochemistry clearly.
"""
)

st.subheader("Chiral compound details")
st.markdown(
    """
- **Compound name:** Yohimbine  
- **Type:** Chiral indole alkaloid  
- **Molecular formula:** C21H26N2O3  
- **Stereocenters shown in this app:** 1 highlighted center (**Atom 7**)  
- **Estimated stereocenters in Yohimbine:** multiple stereocenters (this model displays one representative center for learning)  
- **Atom map in 2D panel:** Ring atoms **C1–C6**, highlighted chiral atom **C7***.
"""
)
