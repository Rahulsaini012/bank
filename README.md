# Bank Management System

This project is a simple **Bank Management System** built with **Flask**, **HTML**, **CSS**, and **PyMySQL**. It allows users to create accounts, log in, credit or debit amounts, and delete accounts.

## **Features**
- Create a new account
- Login for existing users
- View account details
- Credit or debit amounts
- Delete accounts securely

---

## **Installation Guide**

### **1. Clone the Repository:**
```bash
git clone https://github.com/yourusername/bank-management-system.git
cd bank-management-system
```

### **2. Set Up Virtual Environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install Requirements:**
```bash
pip install -r requirements.txt
```

### **4. Configure the Database:**
- Install MySQL Server.
- Create a database named `bank_management`.
- Create a table named `customers` with the following fields:
  ```sql
  CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_number VARCHAR(20) UNIQUE NOT NULL,
    username VARCHAR(100) NOT NULL,
    contact_no VARCHAR(15) NOT NULL,
    amount FLOAT NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL
  );
  ```

### **5. Update the Database Configuration:**
- Edit `app.py` with your MySQL credentials:
  ```python
  connection = pymysql.connect(
      host="localhost",
      user="root",
      password="YOUR_DATABASE_PASSWORD",
      database="bank_management"
  )
  ```

### **6. Run the Application:**
```bash
python app.py
```

### **7. Access the Web App:**
- Open your web browser and go to:  
  `http://127.0.0.1:5000`

---

## **Deployment Guide**

### Deploy on **Render.com** or **Railway.app**
1. Create a new project.
2. Connect your GitHub repository.
3. Add environment variables for database credentials.
4. Deploy the application!

---

## **Technologies Used**
- **Backend:** Flask, PyMySQL
- **Frontend:** HTML, CSS
- **Database:** MySQL

---

## **License**
This project is licensed