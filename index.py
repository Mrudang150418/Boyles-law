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
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Boyle's Law: P * V = constant
# Assume a constant value for simplicity
constant = 1000  # A constant value (can represent the gas constant for this demonstration)

# Volume range (V cannot be zero)
volumes = np.linspace(1, 100, 100)

# Compute corresponding pressure values using Boyle's Law (P = constant / V)
pressures = constant / volumes

# Set up the figure and axis
fig, ax = plt.subplots()
line, = ax.plot([], [], 'b', lw=2)
ax.set_xlim(0, 110)
ax.set_ylim(0, 1200)
ax.set_xlabel('Volume')
ax.set_ylabel('Pressure')
ax.set_title("Boyle's Law: Pressure vs. Volume")

# Initialization function for animation
def init():
    line.set_data([], [])
    return line,

# Animation function that will update the plot
def update(frame):
    # Update plot with current frame (volume, pressure)
    x = volumes[:frame]  # Volumes up to the current frame
    y = pressures[:frame]  # Corresponding pressures
    line.set_data(x, y)
    return line,

# Create animation using FuncAnimation
ani = FuncAnimation(fig, update, frames=len(volumes), init_func=init, blit=True, interval=100)

# Display the animation
plt.show()
