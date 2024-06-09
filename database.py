import mysql.connector 
mydb = mysql.connector.connect(
   host="localhost",
   user="root", 
   password="root", 
   database="Rental_Management_System"
)

c = mydb.cursor()

def create_table():

   c.execute('''
   CREATE TABLE IF NOT EXISTS Tenant(
       Tenant_ID varchar(10) NOT NULL,
       Name varchar(50) NOT NULL,
       Email varchar(50) NOT NULL,
       Phone_number char(10) NOT NULL,
       No_of_people int(3) NOT NULL,
       PRIMARY KEY(Tenant_ID)
   ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
   ''')

  
   c.execute('''
   CREATE TABLE IF NOT EXISTS `Maintenance`(
   `Request_ID` varchar(10) NOT NULL,
   `PropertyID` varchar(10) NOT NULL,
   `RequestDate` date NOT NULL,
   `Status` varchar(20) NOT NULL,
   `Description` varchar(255) NOT NULL,
   PRIMARY KEY(`Request_ID`),
   FOREIGN KEY(`PropertyID`) REFERENCES `Property`(`PropertyID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
   ''')
   
   c.execute('''
   CREATE TABLE IF NOT EXISTS `Property`(
   `PropertyID` varchar(10) NOT NULL,
   `Name` varchar(50) NOT NULL,
   `Location` varchar(100) NOT NULL,
   PRIMARY KEY(`PropertyID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
   ''')
   c.execute('''
   CREATE TABLE IF NOT EXISTS `Payment`(
   `Payment_ID` varchar(10) NOT NULL,
   `Amount` float NOT NULL,
   `Date` date NOT NULL,
   `Method` varchar(20) NOT NULL,
   `Tenant_ID` varchar(10) NOT NULL,
   PRIMARY KEY(`Payment_ID`),
   FOREIGN KEY(`Tenant_ID`) REFERENCES `Tenant`(`Tenant_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
   ''')
   
   mydb.commit()

def add_Tenant_data(Tenant_ID, Name, Email, Phone_number, No_of_people):
    c.execute('SELECT COUNT(*) FROM Tenant WHERE Tenant_ID=%s', (Tenant_ID,))
    if c.fetchone()[0] == 0:
        c.execute('INSERT INTO Tenant (Tenant_ID, Name, Email, Phone_number, No_of_people) VALUES (%s, %s, %s, %s, %s)', (Tenant_ID, Name, Email, Phone_number, No_of_people))
        mydb.commit()
    else:
        raise ValueError("Tenant already exists")

def view_all_Tenant_data():
    c.execute('SELECT * FROM Tenant')
    data = c.fetchall()
    return data

def view_only_Tenant_ID():
    c.execute("SELECT Tenant_ID FROM Tenant")
    data = c.fetchall()
    return data

def get_all_info_Tenant(selected_Tenant):
    c.execute('SELECT * FROM Tenant WHERE Tenant_ID="{}"'.format(selected_Tenant))
    data = c.fetchall()
    return data

def edit_Tenant_data(new_Name, new_Email, new_Phone_number, new_No_of_people, Tenant_ID):
    c.execute("UPDATE Tenant SET Name=%s, Email=%s, Phone_number=%s, No_of_people=%s WHERE Tenant_ID=%s", (new_Name, new_Email, new_Phone_number, new_No_of_people, Tenant_ID))
    mydb.commit()
    data = view_all_Tenant_data()
    return data

def delete_data_Tenant(selected_Tenant):
    c.execute('SELECT COUNT(*) FROM Tenant WHERE Tenant_ID=%s', (selected_Tenant,))
    if c.fetchone()[0] > 0:
        c.execute('DELETE FROM Tenant WHERE Tenant_ID="{}"'.format(selected_Tenant))
        mydb.commit()
    else:
        raise ValueError("Tenant does not exist")

def delete_data_Tenant_by_name(name):
    c.execute('SELECT COUNT(*) FROM Tenant WHERE Name=%s', (name,))
    if c.fetchone()[0] > 0:
        c.execute('DELETE FROM Tenant WHERE Name=%s', (name,))
        mydb.commit()
    else:
        raise ValueError("Tenant name does not exist")

def add_Payment_data(Payment_ID, Amount, Date, Method, Tenant_ID):
    c.execute('SELECT COUNT(*) FROM Payment WHERE Payment_ID=%s', (Payment_ID,))
    if c.fetchone()[0] == 0:
        c.execute('INSERT INTO Payment (Payment_ID, Amount, Date, Method, Tenant_ID) VALUES (%s, %s, %s, %s, %s)', (Payment_ID, Amount, Date, Method, Tenant_ID))
        mydb.commit()
    else:
        raise ValueError("Payment already exists")

def view_all_Payment_data():
    c.execute('SELECT * FROM Payment')
    data = c.fetchall()
    return data

def view_only_Payment_ID():
    c.execute('SELECT Payment_ID FROM Payment')
    data = c.fetchall()
    return data

def get_all_info_Payment(selected_Payment):
    c.execute('SELECT * FROM Payment WHERE Payment_ID="{}"'.format(selected_Payment))
    data = c.fetchall()
    return data

def edit_Payment_data(new_Amount, new_Date, new_Method, new_Tenant_ID, Payment_ID):
    c.execute("UPDATE Payment SET Amount=%s, Date=%s, Method=%s, Tenant_ID=%s WHERE Payment_ID=%s", (new_Amount, new_Date, new_Method, new_Tenant_ID, Payment_ID))
    mydb.commit()
    data = view_all_Payment_data()
    return data

def delete_data_Payment(selected_Payment):
    c.execute('SELECT COUNT(*) FROM Payment WHERE Payment_ID=%s', (selected_Payment,))
    if c.fetchone()[0] > 0:
        c.execute('DELETE FROM Payment WHERE Payment_ID=%s', (selected_Payment,))
        mydb.commit()
    else:
        raise ValueError("Payment does not exist")

def add_Maintenance_data(Request_ID, PropertyID, RequestDate, Status, Description):
    c.execute('SELECT COUNT(*) FROM Maintenance WHERE Request_ID=%s', (Request_ID,))
    if c.fetchone()[0] == 0:
        c.execute('INSERT INTO Maintenance (Request_ID, PropertyID, RequestDate, Status, Description) VALUES (%s, %s, %s, %s, %s)', (Request_ID, PropertyID, RequestDate, Status, Description))
        mydb.commit()
    else:
        raise ValueError("Maintenance request already exists")

def view_all_Maintenance_data():
    c.execute('SELECT * FROM Maintenance')
    data = c.fetchall()
    return data

def view_only_Maintenance_ID():
    c.execute("SELECT Request_ID FROM Maintenance")
    data = c.fetchall()
    return data

def get_all_info_Maintenance(selected_Request):
    c.execute('SELECT * FROM Maintenance WHERE Request_ID="{}"'.format(selected_Request))
    data = c.fetchall()
    return data

def edit_Maintenance_data(new_PropertyID, new_RequestDate, new_Status, new_Description, Request_ID):
    c.execute("UPDATE Maintenance SET PropertyID=%s, RequestDate=%s, Status=%s, Description=%s WHERE Request_ID=%s", (new_PropertyID, new_RequestDate, new_Status, new_Description, Request_ID))
    mydb.commit()
    data = view_all_Maintenance_data()
    return data

def delete_data_Maintenance(selected_Request):
    c.execute('SELECT COUNT(*) FROM Maintenance WHERE Request_ID=%s', (selected_Request,))
    if c.fetchone()[0] > 0:
        c.execute('DELETE FROM Maintenance WHERE Request_ID=%s', (selected_Request,))
        mydb.commit()
    else:
        raise ValueError("Maintenance request does not exist")

def add_Lease_data(Lease_ID, Tenant_ID, Property_ID, Start_Date, End_Date, Rent):
    c.execute('SELECT COUNT(*) FROM Lease WHERE Lease_ID=%s', (Lease_ID,))
    if c.fetchone()[0] == 0:
        c.execute('INSERT INTO Lease (Lease_ID, Tenant_ID, Property_ID, Start_Date, End_Date, Rent) VALUES (%s, %s, %s, %s, %s, %s)', (Lease_ID, Tenant_ID, Property_ID, Start_Date, End_Date, Rent))
        mydb.commit()
    else:
        raise ValueError("Lease already exists")

def view_all_Lease_data():
    c.execute('SELECT * FROM Lease')
    data = c.fetchall()
    return data

def view_only_Lease_ID():
    c.execute("SELECT Lease_ID FROM Lease")
    data = c.fetchall()
    return data

def get_all_info_Lease(selected_Lease):
    c.execute('SELECT * FROM Lease WHERE Lease_ID="{}"'.format(selected_Lease))
    data = c.fetchall()
    return data

def edit_Lease_data(new_Tenant_ID, new_Property_ID, new_Start_Date, new_End_Date, new_Rent, Lease_ID):
    c.execute("UPDATE Lease SET Tenant_ID=%s, Property_ID=%s, Start_Date=%s, End_Date=%s, Rent=%s WHERE Lease_ID=%s", (new_Tenant_ID, new_Property_ID, new_Start_Date, new_End_Date, new_Rent, Lease_ID))
    mydb.commit()
    data = view_all_Lease_data()
    return data

def delete_data_Lease(selected_Lease):
    c.execute('SELECT COUNT(*) FROM Lease WHERE Lease_ID=%s', (selected_Lease,))
    if c.fetchone()[0] > 0:
        c.execute('DELETE FROM Lease WHERE Lease_ID=%s', (selected_Lease,))
        mydb.commit()
    else:
        raise ValueError("Lease does not exist")

def add_Property_data(PropertyID, Name, Location):
    c.execute('SELECT COUNT(*) FROM Property WHERE PropertyID=%s', (PropertyID,))
    if c.fetchone()[0] == 0:
        c.execute('INSERT INTO Property (PropertyID, Name, Location) VALUES (%s, %s, %s)', (PropertyID, Name, Location))
        mydb.commit()
    else:
        raise ValueError("Property already exists")

def view_all_Property_data():
    c.execute('SELECT * FROM Property')
    data = c.fetchall()
    return data

def view_only_Property_ID():
    c.execute("SELECT PropertyID FROM Property")
    data = c.fetchall()
    return data

def get_all_info_Property(selected_Property):
    c.execute('SELECT * FROM Property WHERE PropertyID="{}"'.format(selected_Property))
    data = c.fetchall()
    return data

def edit_Property_data(new_Name, new_Location, PropertyID):
    c.execute("UPDATE Property SET Name=%s, Location=%s WHERE PropertyID=%s", (new_Name, new_Location, PropertyID))
    mydb.commit()
    data = view_all_Property_data()
    return data

def delete_data_Property(selected_Property):
    c.execute('SELECT COUNT(*) FROM Property WHERE PropertyID=%s', (selected_Property,))
    if c.fetchone()[0] > 0:
        c.execute('DELETE FROM Property WHERE PropertyID=%s', (selected_Property,))
        mydb.commit()
    else:
        raise ValueError("Property does not exist")
