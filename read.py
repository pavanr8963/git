import pandas as pd
import streamlit as st
from database import *

def read_for_Tenant():
    result = view_all_Tenant_data()
    df = pd.DataFrame(result, columns=['Tenant_ID', 'Name', 'Email', 'Phone_number', 'No_of_people'])
    with st.expander("View all Tenants"):
        st.dataframe(df)

def read_for_Payment():
    result = view_all_Payment_data()
    df = pd.DataFrame(result, columns=['Payment_ID', 'Amount', 'Date', 'Method', 'Tenant_ID'])
    with st.expander("View all Payments"):
        st.dataframe(df)

def read_for_Maintenance():
    result = view_all_Maintenance_data()
    df = pd.DataFrame(result, columns=['Request_ID', 'House_ID', 'RequestDate', 'Status', 'Description'])
    with st.expander("View all Maintenance Requests"):
        st.dataframe(df)

def read_for_Lease():
    result = view_all_Lease_data()
    df = pd.DataFrame(result, columns=['Lease_ID', 'Tenant_ID', 'House_ID', 'StartDate', 'EndDate', 'Rent'])
    with st.expander("View all Leases"):
        st.dataframe(df)

def read_for_Property():
    result = view_all_Property_data()
    df = pd.DataFrame(result, columns=['PropertyID', 'Name', 'Location'])
    with st.expander("View all Properties"):
        st.dataframe(df)