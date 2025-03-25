import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


st.title("Interactive Streamlit App")
st.header("Explore Data, Visualize Trends & Interact with Widgets")


st.sidebar.title("Navigation")
selected_option = st.sidebar.radio("Choose a section:", ["Home", "Data Entry", "Visualization"])


if selected_option == "Home":
    st.write("""
    ### Welcome to the Enhanced Streamlit App
    This app demonstrates:
    - Dynamic Data Entry
    - Interactive Visualizations
    - Conditional Button Actions
    """)


elif selected_option == "Data Entry":
    st.subheader("Enter Your Details Below:")
    
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=1, max_value=100)
    gender = st.radio("Select your gender:", ["Male", "Female", "Other"])

    if st.button("Submit"):
        st.success(f"Hello {name}, age {age}, identified as {gender}. Data saved successfully!")


elif selected_option == "Visualization":
    st.subheader("Random Data Visualization")

    data = pd.DataFrame({
        'X-axis': np.arange(1, 101),
        'Y-axis': np.random.randint(1, 100, size=100)
    })

    
    fig, ax = plt.subplots()
    ax.plot(data['X-axis'], data['Y-axis'], color='blue', marker='o')
    ax.set_title("Sample Data Visualization")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")

    st.pyplot(fig)


st.sidebar.markdown("---")
st.sidebar.write("© 2025 Kunwarjot Singh")

