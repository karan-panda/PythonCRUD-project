# PythonCRUD-project
This CRUD web app, built using Python, JS, and HTML/CSS, allows users to easily perform CRUD operations on a database. Featuring a user-friendly interface, Flask framework, mySQL, and data validation, it's a great foundation for building CRUD-based web apps.

# Python CRUD Project using Flask and MySQL
This is a Python CRUD (Create, Read, Update, Delete) project that utilizes Flask, a Python web framework, and MySQL database. It provides a basic REST API for managing student records and their marks for a particular course.

# Installation
### 1. Clone the repository to your local machine:

```bash
git clone https://github.com/karan-panda/PythonCRUD-project.git
```
### 2. Install the required packages:
 ```bash
 pip install -r requirements
 ```
 ### 3. Create a MySQL database named group1 and import the group1.sql file provided in the project directory.
 
# Usage
### 1. Start the Flask server:
```python
python crud.py
```

### 2. Access the endpoints using a web browser or any API development tool like Postman to test the crud.py python API. The following endpoints are available:
- `GET /users` - Fetches all student records from the database.
- `GET /user?rollno=<rollno>` - Fetches a specific student record by the given roll number.
- `DELETE /users?rollno=<rollno>` - Deletes a student record by the given roll number.
- `POST /users` - Updates an existing student record in the database.
- `PUT /users` - Inserts a new student record in the database.
- `GET /insertmarks` - Inserts a new record for a particular student with their marks.

NOTE: You can also use the index.html (front-end) instead of using Postman to do CRUD operations.

# Acknowledgments
This group project was created as part of Python ESD for Innovative Exams by group 1 from TCET Mumbai IT Branch.

Special Thanks to:
1. :cow: Nilesh Pal `Roll no. 01`
2. :disguised_face: Aditya Palande `Roll no. 02`
3. :panda_face: Karan Panda `Roll no.  03` (me)
4. :fox_face: Anand Pandey `Roll no. 04`
5. :koala: Nishant Pandey `Roll no. 05`

for collaborating and supporting me throughtout the Project.
