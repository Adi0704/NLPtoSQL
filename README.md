# Conversational SQL Assistant

## 🚀 Overview
This project enables users to interact with a **MySQL database** using **natural language queries**. Instead of writing SQL, users can simply ask questions like:

- **"Give me names of all employees along with their performance."**
- **"Which department does Jane Smith work for?"**
- **"When was she hired?"**

The system processes these queries, dynamically generates the necessary **SQL statements**, retrieves data from MySQL, and returns human-readable responses—all while maintaining the **conversation context**.

## 🖼️ Demo
![Demo Screenshot](Text2SQL.drawio.png)

## 🔧 How It Works
1. **Natural Language to SQL:**
   - The user's query is converted into an SQL statement.
   - Example:
     ```sql
     SELECT employee.name, performance.rating 
     FROM employee 
     JOIN performance ON employee.id = performance.employee_id;
     ```

2. **Database Query Execution:**
   - The generated SQL query is executed on a **MySQL database**, retrieving relevant data.

3. **Conversational Memory:**
   - The system **remembers** previous interactions, allowing follow-up questions like:
     - *"Which department does Jane Smith work for?"*
     - *"When was she hired?"* (The assistant understands "she" refers to Jane Smith.)

4. **Human-Readable Responses:**
   - The raw SQL output is transformed into structured, easy-to-understand sentences.

## 📂 Project Structure
```
├── app.py                # Main application script
├── bot.py                # Conversational AI and SQL generation
├── sql.py                # Database connection and schema retrieval
├── htmlTemplates.py      # HTML templates for chat messages
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

## 📌 Key Features
✅ **Seamless interaction with MySQL databases** using simple questions  
✅ **Joins multiple tables** dynamically based on the query  
✅ **Maintains conversation context** for better user experience  
✅ **Automatically structures responses** for clarity  
✅ **User-friendly interface using Streamlit**  

## 🛠️ Getting Started
### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Set Up MySQL Database
- Ensure you have a MySQL database running.
- Update your connection details in `sql.py`:
  ```python
  from langchain_community.utilities import SQLDatabase
  db = SQLDatabase.from_uri("mysql+pymysql://user:password@host/db_name")
  ```

### 3️⃣ Start the Application
```bash
streamlit run app.py
```

## 📬 Contact Me
📧 Email: hombaladitya30@gmail.com  


👏 **Thanks for checking this out! If you found it useful, give it a star ⭐ on GitHub!**
