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
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

# Boyle's Law function
def calculate_volume(P1, V1, P2):
    return (P1 * V1) / P2

# Streamlit UI setup
st.title("Boyle's Law Animation using Matplotlib")

st.write("""
Boyle's Law states that, for a fixed amount of gas at constant temperature, 
the pressure of the gas is inversely proportional to its volume:  
\[ P_1 \times V_1 = P_2 \times V_2 \]
Use the inputs below to see how pressure and volume interact!
""")

# User inputs for initial conditions
P1 = st.number_input("Enter Initial Pressure (P1 in atm):", min_value=0.1, value=1.0, format="%.2f")
V1 = st.number_input("Enter Initial Volume (V1 in liters):", min_value=0.1, value=1.0, format="%.2f")

# Pressure range for the animation (final pressure range)
P2_min = st.number_input("Enter minimum Final Pressure (P2 in atm):", min_value=0.1, value=0.5, format="%.2f")
P2_max = st.number_input("Enter maximum Final Pressure (P2 in atm):", min_value=P2_min, value=10.0, format="%.2f")
num_steps = st.slider("Number of steps in the animation", min_value=10, max_value=100, value=50)

# Create pressure values for the animation
P2_values = np.linspace(P2_min, P2_max, num_steps)

# Set up the figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(P2_min, P2_max)
ax.set_ylim(0, 1.2 * V1)
ax.set_xlabel("Pressure (atm)")
ax.set_ylabel("Volume (liters)")
ax.set_title("Boyle's Law: Pressure vs Volume")

# Initialize the line object
line, = ax.plot([], [], lw=2)

# Initialize the point object
point, = ax.plot([], [], 'ro')

# Function to initialize the plot
def init():
    line.set_data([], [])
    point.set_data([], [])
    return line, point

# Function to update the plot in each animation step
def animate(i):
    P2 = P2_values[i]
    V2 = calculate_volume(P1, V1, P2)

    # Update the line and point for animation
    pressures = np.linspace(P2_min, P2_max, 100)
    volumes = calculate_volume(P1, V1, pressures)
    line.set_data(pressures, volumes)
    point.set_data(P2, V2)
    
    return line, point

# Button to start the animation
if st.button("Start Animation"):
    # Create the animation using FuncAnimation
    anim = FuncAnimation(fig, animate, init_func=init, frames=len(P2_values), interval=100, blit=True)

    # Display the plot using Streamlit
    st.pyplot(fig)

    # To ensure the animation runs smoothly, introduce some delay after each frame
    for _ in P2_values:
        time.sleep(0.1)
