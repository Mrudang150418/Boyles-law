import streamlit as st

# Boyle's Law function
def calculate_boyles_law(P1=None, V1=None, P2=None, V2=None):
    """
    Calculate the missing variable using Boyle's Law: P1 * V1 = P2 * V2.
    One of P2 or V2 should be None, and the function will calculate it.
    """
    if P2 is None and V2 is not None:
        P2 = (P1 * V1) / V2
        return P2, V2
    elif V2 is None and P2 is not None:
        V2 = (P1 * V1) / P2
        return P2, V2
    else:
        raise ValueError("Either P2 or V2 must be provided, but not both.")

# Streamlit UI setup
st.title("Boyle's Law Calculator")

# Input fields for Initial Pressure (P1) and Initial Volume (V1)
P1 = st.number_input("Enter Initial Pressure (P1):", min_value=0.0, format="%.2f")
V1 = st.number_input("Enter Initial Volume (V1):", min_value=0.0, format="%.2f")

# Choice for user to either input Final Pressure (P2) or Final Volume (V2)
calculation_type = st.radio("What do you want to calculate?", ("Final Pressure (P2)", "Final Volume (V2)"))

if calculation_type == "Final Pressure (P2)":
    V2 = st.number_input("Enter Final Volume (V2):", min_value=0.0, format="%.2f")
    if st.button("Calculate Final Pressure"):
        try:
            P2, _ = calculate_boyles_law(P1=P1, V1=V1, V2=V2)
            st.success(f"Final Pressure (P2) is: {P2:.2f}")
        except Exception as e:
            st.error(f"Error: {e}")

elif calculation_type == "Final Volume (V2)":
    P2 = st.number_input("Enter Final Pressure (P2):", min_value=0.0, format="%.2f")
    if st.button("Calculate Final Volume"):
        try:
            _, V2 = calculate_boyles_law(P1=P1, V1=V1, P2=P2)
            st.success(f"Final Volume (V2) is: {V2:.2f}")
        except Exception as e:
            st.error(f"Error: {e}")


import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

# Boyle's Law: P1 * V1 = P2 * V2
def calculate_volume(P1, V1, P2):
    return (P1 * V1) / P2

# Streamlit UI setup
st.title("Boyle's Law Animation")

# User inputs for initial conditions
P1 = st.number_input("Enter Initial Pressure (P1):", min_value=0.0, value=1.0, format="%.2f")
V1 = st.number_input("Enter Initial Volume (V1):", min_value=0.0, value=1.0, format="%.2f")

# Pressure range for the animation (final pressure range)
P2_min = st.number_input("Enter minimum Final Pressure (P2):", min_value=0.1, value=0.5, format="%.2f")
P2_max = st.number_input("Enter maximum Final Pressure (P2):", min_value=P2_min, value=10.0, format="%.2f")
num_steps = st.slider("Number of steps in the animation", min_value=10, max_value=100, value=50)

# Create pressure values for the animation
P2_values = np.linspace(P2_min, P2_max, num_steps)

# Initialize plot
fig = go.Figure()
fig.update_layout(
    xaxis_title="Pressure (P)",
    yaxis_title="Volume (V)",
    title="Boyle's Law: Pressure vs Volume",
    xaxis=dict(range=[P2_min, P2_max]),
    yaxis=dict(range=[0, 1.2 * V1])  # Dynamic range for volume based on the initial volume
)

# Button to start the animation
if st.button("Start Animation"):
    # Iterate through the pressure values, calculate volume, and update the plot
    for P2 in P2_values:
        V2 = calculate_volume(P1, V1, P2)

        # Update the graph
        fig.data = []  # Clear previous data
        fig.add_trace(go.Scatter(x=[P2], y=[V2], mode='markers', marker=dict(size=10, color='red')))
        
        # Update the trace showing Boyle's law as a curve (P * V = constant)
        pressures = np.linspace(P2_min, P2_max, 100)
        volumes = calculate_volume(P1, V1, pressures)
        fig.add_trace(go.Scatter(x=pressures, y=volumes, mode='lines', name="Boyle's Law Curve"))

        # Render the plot
        st.plotly_chart(fig)

        # Add a delay for the animation effect
        time.sleep(0.1)


