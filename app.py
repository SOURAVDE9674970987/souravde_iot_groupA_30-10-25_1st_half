import streamlit as st
import pandas as pd
from datetime import datetime

available_slots = ['09:00 AM', '10:00 AM', '11:00 AM', '01:00 PM', '02:00 PM', '03:00 PM']

appointments = []

st.title("Patient Online Booking System")


with st.form(key='booking_form'):
    st.subheader("Please enter your details to book an appointment")
    
    patient_name = st.text_input("Full Name")
    patient_email = st.text_input("Email")
    patient_phone = st.text_input("Phone Number")
    

    appointment_date = st.date_input("Choose an Appointment Date", min_value=datetime.today())

    time_slot = st.selectbox("Choose Available Time Slot", available_slots)
   
    submit_button = st.form_submit_button(label="Book Appointment")

    if submit_button:

        appointment = {
            'Name': patient_name,
            'Email': patient_email,
            'Phone': patient_phone,
            'Date': appointment_date,
            'Time': time_slot
        }
        appointments.append(appointment)

        st.success(f"Appointment booked successfully for {patient_name} on {appointment_date} at {time_slot}!")

        st.subheader("Upcoming Appointments")
        appointments_df = pd.DataFrame(appointments)
        st.dataframe(appointments_df)

