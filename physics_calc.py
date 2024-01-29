import streamlit as st
import math

def main():
    st.title("Physics Equations Calculator")

    equation_choice = st.sidebar.selectbox("Select an equation", (
        "Newton's Second Law",
        "Einstein's Mass-Energy Equivalence",
        "Projectile Motion",
        "Wave Speed",
        "Simple Harmonic Motion"
    ))

    if equation_choice == "Newton's Second Law":
        newtons_second_law()
    elif equation_choice == "Einstein's Mass-Energy Equivalence":
        mass_energy_equivalence()
    elif equation_choice == "Projectile Motion":
        projectile_motion()
    elif equation_choice == "Wave Speed":
        wave_speed()
    elif equation_choice == "Simple Harmonic Motion":
        simple_harmonic_motion()

def newtons_second_law():
    st.header("Newton's Second Law Calculator")

    mass = st.number_input("Enter the mass (kg)", min_value=0.0)
    acceleration = st.number_input("Enter the acceleration (m/s^2)", min_value=0.0)

    force = mass * acceleration

    st.write(f"Force = {force} Newtons")

def mass_energy_equivalence():
    st.header("Einstein's Mass-Energy Equivalence Calculator")

    mass = st.number_input("Enter the mass (kg)", min_value=0.0)

    speed_of_light = 3.0e8  # meters per second
    energy = mass * speed_of_light**2

    st.write(f"Energy = {energy} Joules")

def projectile_motion():
    st.header("Projectile Motion Calculator")

    initial_velocity = st.number_input("Enter the initial velocity (m/s)", min_value=0.0)
    launch_angle = st.number_input("Enter the launch angle (degrees)", min_value=0.0, max_value=90.0)
    g = 9.8  # acceleration due to gravity

    launch_angle_rad = math.radians(launch_angle)
    time_of_flight = (2 * initial_velocity * math.sin(launch_angle_rad)) / g
    horizontal_range = (initial_velocity**2 * math.sin(2 * launch_angle_rad)) / g
    max_height = (initial_velocity**2 * (math.sin(launch_angle_rad))**2) / (2 * g)

    st.write(f"Time of Flight = {time_of_flight} seconds")
    st.write(f"Horizontal Range = {horizontal_range} meters")
    st.write(f"Max Height = {max_height} meters")

def wave_speed():
    st.header("Wave Speed Calculator")

    frequency = st.number_input("Enter the frequency (Hz)", min_value=0.0)
    wavelength = st.number_input("Enter the wavelength (meters)", min_value=0.0)

    wave_speed = frequency * wavelength

    st.write(f"Wave Speed = {wave_speed} meters/second")

def simple_harmonic_motion():
    st.header("Simple Harmonic Motion Calculator")

    amplitude = st.number_input("Enter the amplitude (meters)", min_value=0.0)
    angular_frequency = st.number_input("Enter the angular frequency (rad/s)", min_value=0.0)
    time = st.number_input("Enter the time (seconds)")

    displacement = amplitude * math.cos(angular_frequency * time)

    st.write(f"Displacement = {displacement} meters")

if __name__ == "__main__":
    main()
