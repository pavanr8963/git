import streamlit as st
from database import *

def create_for_Tenant():
    with st.container():
        Tenant_ID = st.text_input("Tenant_ID:")
        Name = st.text_input("Name:")
        Email = st.text_input("Email:")
        Phone_number = st.text_input("Phone_number:")
        No_of_people = st.text_input("No_of_people:")
    if st.button("Add Tenant Details"):
        add_Tenant_data(Tenant_ID, Name, Email, Phone_number, No_of_people)
        st.success(f"Successfully added Tenant details: {Tenant_ID}")

def create_for_Payment():
    with st.container():
        Payment_ID = st.text_input("Payment_ID:")
        Amount = st.text_input("Amount:")
        Date = st.date_input("Date:")
        Method = st.text_input("Method:")
        Tenant_ID = st.text_input("Tenant_ID:")
    if st.button("Add Payment Details"):
        add_Payment_data(Payment_ID, Amount, Date, Method, Tenant_ID)
        st.success(f"Successfully added Payment details: {Payment_ID}")

def create_for_Maintenance():
    with st.container():
        Request_ID = st.text_input("Request_ID:")
        PropertyID = st.text_input("PropertyID:")
        RequestDate = st.date_input("RequestDate:")
        Status = st.text_input("Status:")
        Description = st.text_input("Description:")
    if st.button("Add Maintenance Details"):
        add_Maintenance_data(Request_ID, PropertyID, RequestDate, Status, Description)
        st.success(f"Successfully added Maintenance details: {Request_ID}")

def create_for_Lease():
    with st.container():
        Lease_ID = st.text_input("Lease_ID:")
        Tenant_ID = st.text_input("Tenant_ID:")
        PropertyID = st.text_input("PropertyID")
        Start_Date = st.date_input("Start_Date:")
        End_Date = st.date_input("End_Date:")
        Rent = st.text_input("Rent:")
    if st.button("Add Lease Details"):
        add_Lease_data(Lease_ID, Tenant_ID, PropertyID, Start_Date, End_Date, Rent)
        st.success(f"Successfully added Lease details: {Lease_ID}")

def create_for_Property():
    with st.container():
        PropertyID = st.text_input("PropertyID:")
        Name = st.text_input("Name:")
        Location = st.text_input("Location:")
    if st.button("Add Property Details"):
        add_Property_data(PropertyID, Name, Location)
        st.success(f"Successfully added Property details: {PropertyID}")