import pandas as pd
import streamlit as st
from database import *



def delete_for_Tenant():
    result = view_all_Tenant_data()
    df = pd.DataFrame(result, columns=['Tenant_ID', 'Name', 'Email', 'Phone_number', 'No_of_people'])
    with st.expander("View all Tenants"):
        st.dataframe(df)
    list_of_Tenants = [i[0] for i in view_only_Tenant_ID()]
    selected_Tenant = st.selectbox("Tenant to delete", list_of_Tenants)
    st.warning(f"Do you want to delete ::{selected_Tenant}")
    try:
        delete_data_Tenant(selected_Tenant)
        st.success("Tenant has been deleted successfully")
    except ValueError as e:
        st.error(e)
    result2 = view_all_Tenant_data()
    df2 = pd.DataFrame(result2, columns=['Tenant_ID', 'Name', 'Email', 'Phone_number', 'No_of_people'])
    with st.expander("Updated data"):
        st.dataframe(df2)

    selected_Tenant_name = st.selectbox("Tenant Name to delete", [i[1] for i in result])
    st.warning(f"Do you want to delete ::{selected_Tenant_name}")
    try:
        delete_data_Tenant_by_name(selected_Tenant_name)
        st.success("Tenant has been deleted successfully")
    except ValueError as e:
        st.error(e)

def delete_for_Payment():
    result = view_all_Payment_data()
    df = pd.DataFrame(result, columns=['Payment_ID', 'Amount', 'Date', 'Method', 'Tenant_ID'])
    with st.expander("View all Payments"):
        st.dataframe(df)
    list_of_Payments = [i[0] for i in view_only_Payment_ID()]
    selected_Payment = st.selectbox("Payment to delete", list_of_Payments)
    st.warning(f"Do you want to delete ::{selected_Payment}")
    if st.button("Delete Payment"):
        delete_data_Payment(selected_Payment)
        st.success("Payment has been deleted successfully")
    result2 = view_all_Payment_data()
    df2 = pd.DataFrame(result2, columns=['Payment_ID', 'Amount', 'Date', 'Method', 'Tenant_ID'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_for_Maintenance():
    result = view_all_Maintenance_data()
    df = pd.DataFrame(result, columns=['Request_ID', 'House_ID', 'RequestDate', 'Status', 'Description'])
    with st.expander("View all Maintenance Requests"):
        st.dataframe(df)
    list_of_Requests = [i[0] for i in view_only_Maintenance_ID()]
    selected_Request = st.selectbox("Request to delete", list_of_Requests)
    st.warning(f"Do you want to delete ::{selected_Request}")
    if st.button("Delete Maintenance"):
        delete_data_Maintenance(selected_Request)
        st.success("Maintenance request has been deleted successfully")
    result2 = view_all_Maintenance_data()
    df2 = pd.DataFrame(result2, columns=['Request_ID', 'House_ID', 'RequestDate', 'Status', 'Description'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_for_Lease():
    result = view_all_Lease_data()
    df = pd.DataFrame(result, columns=['Lease_ID', 'Tenant_ID', 'House_ID', 'StartDate', 'EndDate', 'Rent'])
    with st.expander("View all Leases"):
        st.dataframe(df)
    list_of_Leases = [i[0] for i in view_only_Lease_ID()]
    selected_Lease = st.selectbox("Lease to delete", list_of_Leases)
    st.warning(f"Do you want to delete ::{selected_Lease}")
    if st.button("Delete Lease"):
        delete_data_Lease(selected_Lease)
        st.success("Lease has been deleted successfully")
    result2 = view_all_Lease_data()
    df2 = pd.DataFrame(result2, columns=['Lease_ID', 'Tenant_ID', 'House_ID', 'StartDate', 'EndDate', 'Rent'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_for_Property():
    result = view_all_Property_data()
    df = pd.DataFrame(result, columns=['PropertyID', 'Name', 'Location'])
    with st.expander("View all Properties"):
        st.dataframe(df)
    list_of_Properties = [i[0] for i in view_only_Property_ID()]
    selected_Property = st.selectbox("Property to delete", list_of_Properties)
    st.warning(f"Do you want to delete ::{selected_Property}")
    if st.button("Delete Property"):
        delete_data_Property(selected_Property)
        st.success("Property has been deleted successfully")
    result2 = view_all_Property_data()
    df2 = pd.DataFrame(result2, columns=['PropertyID', 'Name', 'Location'])
    with st.expander("Updated data"):
        st.dataframe(df2)