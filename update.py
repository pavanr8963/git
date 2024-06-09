import pandas as pd
import streamlit as st
from database import *



def update_for_House():
    result = view_all_House_data()
    df = pd.DataFrame(result, columns=['House_ID', 'Facilities', 'Address', 'Type'])
    with st.expander("Current House details"):
        st.dataframe(df)
    list_of_Houses = [i[0] for i in view_only_House_ID()]
    selected_House = st.selectbox("House to Edit", list_of_Houses)
    selected_result = get_all_info_House(selected_House)
    if selected_result:
        House_ID = selected_result[0][0]
        Facilities = selected_result[0][1]
        Address = selected_result[0][2]
        Type = selected_result[0][3]
        with st.container():
            new_Facilities = st.text_input("Facilities:", Facilities)
            new_Address = st.text_input("Address:", Address)
            new_Type = st.text_input("Type:", Type)
        if st.button("Update House"):
            edit_House_data(new_Facilities, new_Address, new_Type, House_ID)
            st.success("Successfully updated")
    result2 = view_all_House_data()
    df2 = pd.DataFrame(result2, columns=['House_ID', 'Facilities', 'Address', 'Type'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_for_Tenant():
    result = view_all_Tenant_data()
    df = pd.DataFrame(result, columns=['Tenant_ID', 'Name', 'Email', 'Phone_number', 'No_of_people'])
    with st.expander("Current Tenant details"):
        st.dataframe(df)
    list_of_Tenants = [i[0] for i in view_only_Tenant_ID()]
    selected_Tenant = st.selectbox("Tenant to Edit", list_of_Tenants)
    selected_result = get_all_info_Tenant(selected_Tenant)
    if selected_result:
        Tenant_ID = selected_result[0][0]
        Name = selected_result[0][1]
        Email = selected_result[0][2]
        Phone_number = selected_result[0][3]
        No_of_people = selected_result[0][4]
        with st.container():
            new_Name = st.text_input("Name:", Name)
            new_Email = st.text_input("Email:", Email)
            new_Phone_number = st.text_input("Phone_number:", Phone_number)
            new_No_of_people = st.text_input("No_of_people:", No_of_people)
        if st.button("Update Tenant"):
            edit_Tenant_data(new_Name, new_Email, new_Phone_number, new_No_of_people, Tenant_ID)
            st.success("Successfully updated")
    result2 = view_all_Tenant_data()
    df2 = pd.DataFrame(result2, columns=['Tenant_ID', 'Name', 'Email', 'Phone_number', 'No_of_people'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_for_Payment():
    result = view_all_Payment_data()
    df = pd.DataFrame(result, columns=['Payment_ID', 'Amount', 'Date', 'Method', 'Tenant_ID'])
    with st.expander("Current Payment details"):
        st.dataframe(df)
    list_of_Payments = [i[0] for i in view_only_Payment_ID()]
    selected_Payment = st.selectbox("Payment to Edit", list_of_Payments)
    selected_result = get_all_info_Payment(selected_Payment)
    if selected_result:
        Payment_ID = selected_result[0][0]
        Amount = selected_result[0][1]
        Date = selected_result[0][2]
        Method = selected_result[0][3]
        Tenant_ID = selected_result[0][4]
        with st.container():
            new_Amount = st.text_input("Amount:", Amount)
            new_Date = st.date_input("Date:", Date)
            new_Method = st.text_input("Method:", Method)
            new_Tenant_ID = st.text_input("Tenant_ID:", Tenant_ID)
        if st.button("Update Payment"):
            edit_Payment_data(new_Amount, new_Date, new_Method, new_Tenant_ID, Payment_ID)
            st.success("Successfully updated")
    result2 = view_all_Payment_data()
    df2 = pd.DataFrame(result2, columns=['Payment_ID', 'Amount', 'Date', 'Method', 'Tenant_ID'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_for_Maintenance():
    result = view_all_Maintenance_data()
    df = pd.DataFrame(result, columns=['Request_ID', 'PropertyID', 'RequestDate', 'Status', 'Description'])
    with st.expander("Current Maintenance details"):
        st.dataframe(df)
    list_of_Requests = [i[0] for i in view_only_Maintenance_ID()]
    selected_Request = st.selectbox("Request to Edit", list_of_Requests)
    selected_result = get_all_info_Maintenance(selected_Request)
    if selected_result:
        Request_ID = selected_result[0][0]
        PropertyID = selected_result[0][1]
        RequestDate = selected_result[0][2]
        Status = selected_result[0][3]
        Description = selected_result[0][4]
        with st.container():
            new_PropertyID = st.text_input("PropertyID:", PropertyID)
            new_RequestDate = st.date_input("RequestDate:", RequestDate)
            new_Status = st.text_input("Status:", Status)
            new_Description = st.text_input("Description:", Description)
        if st.button("Update Maintenance"):
            edit_Maintenance_data(new_PropertyID, new_RequestDate, new_Status, new_Description, Request_ID)
            st.success("Successfully updated")
    result2 = view_all_Maintenance_data()
    df2 = pd.DataFrame(result2, columns=['Request_ID', 'PropertyID', 'RequestDate', 'Status', 'Description'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_for_Lease():
    result = view_all_Lease_data()
    df = pd.DataFrame(result, columns=['Lease_ID', 'Tenant_ID', 'Property_ID', 'Start_Date', 'End_Date', 'Rent'])
    with st.expander("Current Lease details"):
        st.dataframe(df)
    list_of_Leases = [i[0] for i in view_only_Lease_ID()]
    selected_Lease = st.selectbox("Lease to Edit", list_of_Leases)
    selected_result = get_all_info_Lease(selected_Lease)
    if selected_result:
        Lease_ID = selected_result[0][0]
        Tenant_ID = selected_result[0][1]
        Property_ID = selected_result[0][2]
        Start_Date = selected_result[0][3]
        End_Date = selected_result[0][4]
        Rent = selected_result[0][5]
        with st.container():
            new_Tenant_ID = st.text_input("Tenant_ID:", Tenant_ID)
            new_Property_ID = st.text_input("Property_ID:", Property_ID)
            new_Start_Date = st.date_input("Start_Date:", Start_Date)
            new_End_Date = st.date_input("End_Date:", End_Date)
            new_Rent = st.text_input("Rent:", Rent)
        if st.button("Update Lease"):
            edit_Lease_data(new_Tenant_ID, new_Property_ID, new_Start_Date, new_End_Date, new_Rent, Lease_ID)
            st.success("Successfully updated")
    result2 = view_all_Lease_data()
    df2 = pd.DataFrame(result2, columns=['Lease_ID', 'Tenant_ID', 'Property_ID', 'Start_Date', 'End_Date', 'Rent'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_for_Property():
    result = view_all_Property_data()
    df = pd.DataFrame(result, columns=['PropertyID', 'Name', 'Location'])
    with st.expander("Current Property details"):
        st.dataframe(df)
    list_of_Properties = [i[0] for i in view_only_Property_ID()]
    selected_Property = st.selectbox("Property to Edit", list_of_Properties)
    selected_result = get_all_info_Property(selected_Property)
    if selected_result:
        PropertyID = selected_result[0][0]
        Name = selected_result[0][1]
        Location = selected_result[0][2]
        with st.container():
            new_Name = st.text_input("Name:", Name)
            new_Location = st.text_input("Location:", Location)
        if st.button("Update Property"):
            edit_Property_data(new_Name, new_Location, PropertyID)
            st.success("Successfully updated")
    result2 = view_all_Property_data()
    df2 = pd.DataFrame(result2, columns=['PropertyID', 'Name', 'Location'])
    with st.expander("Updated data"):
        st.dataframe(df2)