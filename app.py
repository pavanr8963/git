import streamlit as st
from create import create_for_Tenant, create_for_Payment, create_for_Maintenance, create_for_Lease, create_for_Property
from read import read_for_Tenant, read_for_Payment, read_for_Maintenance, read_for_Lease, read_for_Property
from update import update_for_Tenant, update_for_Payment, update_for_Maintenance, update_for_Lease, update_for_Property
from delete import delete_for_Tenant, delete_for_Payment, delete_for_Maintenance, delete_for_Lease, delete_for_Property
from database import create_table

def main():
    st.title("Rental Management System")
    app_menu()

def app_menu():
    create_table()  # Ensure tables are created
    menu = ["Tenant", "Payment", "Maintenance", "Property", "Lease"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Tenant":
        menu = ["Add", "View", "Update", "Remove"]
        choice2 = st.sidebar.selectbox("CRUD Operations", menu)
        if choice2 == "Add":
            st.subheader("Enter Tenant Details:")
            create_for_Tenant()
        elif choice2 == "View":
            st.subheader("View the Tenant details:")
            read_for_Tenant()
        elif choice2 == "Update":
            st.subheader("Updated Tenant tasks")
            update_for_Tenant()
        elif choice2 == "Remove":
            st.subheader("Delete Tenant tasks")
            delete_for_Tenant()

    elif choice == "Payment":
        menu = ["Add", "View", "Update", "Remove"]
        choice2 = st.sidebar.selectbox("CRUD Operations", menu)
        if choice2 == "Add":
            st.subheader("Enter Payment Details:")
            create_for_Payment()
        elif choice2 == "View":
            st.subheader("View the Payment details:")
            read_for_Payment()
        elif choice2 == "Update":
            st.subheader("Update Payment details")
            update_for_Payment()
        elif choice2 == "Remove":
            st.subheader("Delete Payment details")
            delete_for_Payment()

    elif choice == "Maintenance":
        menu = ["Add", "View", "Update", "Remove"]
        choice2 = st.sidebar.selectbox("CRUD Operations", menu)
        if choice2 == "Add":
            st.subheader("Enter Maintenance Details:")
            create_for_Maintenance()
        elif choice2 == "View":
            st.subheader("View the Maintenance details:")
            read_for_Maintenance()
        elif choice2 == "Update":
            st.subheader("Update Maintenance details")
            update_for_Maintenance()
        elif choice2 == "Remove":
            st.subheader("Delete Maintenance details")
            delete_for_Maintenance()

    elif choice == "Lease":
        menu = ["Add", "View", "Update", "Remove"]
        choice2 = st.sidebar.selectbox("CRUD Operations", menu)
        if choice2 == "Add":
            st.subheader("Enter Lease Details:")
            create_for_Lease()
        elif choice2 == "View":
            st.subheader("View the Lease details:")
            read_for_Lease()
        elif choice2 == "Update":
            st.subheader("Update Lease details")
            update_for_Lease()
        elif choice2 == "Remove":
            st.subheader("Delete Lease details")
            delete_for_Lease()

    elif choice == "Property":
        menu = ["Add", "View", "Update", "Remove"]
        choice2 = st.sidebar.selectbox("CRUD Operations", menu)
        if choice2 == "Add":
            st.subheader("Enter Property Details:")
            create_for_Property()
        elif choice2 == "View":
            st.subheader("View the Property details:")
            read_for_Property()
        elif choice2 == "Update":
            st.subheader("Update Property details")
            update_for_Property()
        elif choice2 == "Remove":
            st.subheader("Delete Property details")
            delete_for_Property()

    else:
        st.subheader("About tasks")

if __name__ == '__main__':
    main()
