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
import time

# Streamlit App
st.title("Real-time Boyle's Law Graph Calculator")

# Boyle's Law: P1 * V1 = P2 * V2
# Initial conditions (P1, V1)
initial_pressure = st.slider("Initial Pressure (P1) in Pascals:", min_value=1000, max_value=100000, value=50000, step=1000)
initial_volume = st.slider("Initial Volume (V1) in liters:", min_value=1.0, max_value=10.0, value=5.0, step=0.1)

# Create a placeholder for the graph
plot_placeholder = st.empty()

# Time steps for animation
time_steps = np.linspace(0, 10, 100)  # 100 time steps
volume_range = np.linspace(1, 10, 100)  # Simulating volume changes

# Animation loop
for t in range(len(time_steps)):
    # Simulated Volume (V2)
    current_volume = volume_range[t % len(volume_range)]
    
    # Calculate Pressure (P2) using Boyle's Law: P1 * V1 = P2 * V2 => P2 = (P1 * V1) / V2
    current_pressure = (initial_pressure * initial_volume) / current_volume

    # Generate the plot
    fig, ax = plt.subplots()
    
    # Plot the current pressure and volume
    ax.plot(volume_range[:t+1], (initial_pressure * initial_volume) / volume_range[:t+1], color='blue', label='Pressure (P)')
    ax.scatter(current_volume, current_pressure, color='red')  # Mark the current point

    # Set plot labels and limits
    ax.set_xlabel('Volume (liters)')
    ax.set_ylabel('Pressure (Pascals)')
    ax.set_title("Boyle's Law: Pressure vs Volume")
    ax.set_xlim([1, 10])
    ax.set_ylim([0, max(initial_pressure * initial_volume / volume_range)])
    ax.legend()

    # Update the plot in Streamlit
    plot_placeholder.pyplot(fig)

    # Slow down the animation for visualization
    time.sleep(0.1)
