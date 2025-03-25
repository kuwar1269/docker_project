from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

# Title and Introduction
st.title("🌌 Spiral Visualization App")
st.markdown(
    "This interactive app lets you generate stunning spiral patterns. "
    "Use the sliders to adjust the number of points and turns, and choose your favorite color! 🎨"
)

with st.echo(code_location='below'):
    # User controls
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)
    color = st.color_picker("Pick a color for the spiral", "#0068c9")
    opacity = st.slider("Point opacity", 0.1, 1.0, 0.5)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    # Visualizing with Altair
    st.altair_chart(
        alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color=color, opacity=opacity)
        .encode(x='x:Q', y='y:Q')
    )

