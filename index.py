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
import matplotlib.pyplot as plt
import numpy as np

# Streamlit App
st.title('Real-time Boyle\'s Law Graph Calculator')

# Boyle's Law: P1 * V1 = P2 * V2
# Constants for initial conditions (P1, V1)
initial_pressure = st.slider('Initial Pressure (P1) in Pascals:', min_value=1000, max_value=100000, value=50000, step=1000)
initial_volume = st.slider('Initial Volume (V1) in liters:', min_value=1.0, max_value=10.0, value=5.0, step=0.1)

# Generate a range of volumes to calculate pressures using Boyle's Law
volumes = np.linspace(1.0, 10.0, 100)  # Volume range
pressures = (initial_pressure * initial_volume) / volumes  # Boyle's Law formula P2 = (P1 * V1) / V2

# Plotting the Boyle's Law curve
fig, ax = plt.subplots()
ax.plot(volumes, pressures, color='blue', label='Pressure vs Volume')
ax.set_xlabel('Volume (liters)')
ax.set_ylabel('Pressure (Pascals)')
ax.set_title(f'Boyle\'s Law: P1 * V1 = P2 * V2\nInitial Pressure = {initial_pressure} Pa, Initial Volume = {initial_volume} L')
ax.legend()
ax.grid(True)

# Display the graph in Streamlit
st.pyplot(fig)

# Animation loop
for t in range(len(time_steps)):
    update_plot(pressure, t)
    time.sleep(0.9)  # Slow down the animation for visibility
