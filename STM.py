#a= 10
#b = 20
#e = a+b
#print(e)

#import streamlit as st

#st.title("Vada pav")

import streamlit as st
import pandas as pd
import os

# Excel file path
excel_file = 'user_data.xlsx'

# Title
st.title("Data Entry Form")

# Input fields
name = st.text_input("Enter your Name")
mobile = st.text_input("Enter your Mobile Number")
Aadhar = st.text_input("Enter your Aadhar Number")
Pan = st.text_input("Enter your Pancard Number")
address = st.text_area("Enter your Address")

# Done Button
if st.button("Done"):
    if not name or not mobile or not address:
        st.warning("Please fill all fields.")
    else:
        # Create a DataFrame
        new_data = pd.DataFrame([[name, mobile, Aadhar, Pan, address]], columns=["Name", "Mobile Number", "Aadhar Number", "PanCard Number", "Address"])

        # Check if Excel exists
        if os.path.exists(excel_file):
            existing_data = pd.read_excel(excel_file)
            updated_data = pd.concat([existing_data, new_data], ignore_index=True)
        else:
            updated_data = new_data

        # Save to Excel
        updated_data.to_excel(excel_file, index=False)
        st.success("Data saved successfully!")
