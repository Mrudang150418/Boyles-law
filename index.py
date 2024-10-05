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

# Boyle's Law: P * V = constant
# Assume a constant value for simplicity
constant = 1000  # Constant (can represent the gas constant for this demonstration)

st.title("Real-time Boyle's Law Graph")
st.write("This graph demonstrates Boyle's Law: Pressure vs Volume (P * V = constant)")

# Create a Streamlit slider for adjusting the volume
volume = st.slider("Adjust Volume", min_value=1, max_value=100, value=50, step=1)

# Calculate the corresponding pressure using Boyle's Law (P = constant / V)
pressure = constant / volume

# Plot the graph using Matplotlib
fig, ax = plt.subplots()
volumes = np.linspace(1, 100, 100)
pressures = constant / volumes

# Plot the Pressure vs Volume curve
ax.plot(volumes, pressures, label="Boyle's Law Curve")
ax.scatter(volume, pressure, color='red', label=f'Volume={volume}, Pressure={pressure:.2f}')

# Set labels and title
ax.set_xlabel('Volume')
ax.set_ylabel('Pressure')
ax.set_title("Pressure vs Volume (Boyle's Law)")
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)

# Show the current pressure value
st.write(f"At Volume = {volume}, Pressure = {pressure:.2f}")
