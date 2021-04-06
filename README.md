# Instructions

## Setting Up the Database
1. Make sure to download and install PostgreSQL (link: https://www.postgresql.org/)
2. Create a database called "students" 
3. Edit simple_crud/settings.py
4. Go to the "DATABASES" dictionary 
5. Make sure to install psycogpg2 Python library ("pip install psycopg2")
6. Modify the "NAME", "PASSWORD", and "PORT" according to the configurations of your PostgreSQL
7. Type and run "py manage.py migrate" to properly set-up the necessary tables for the database 

## Running the Server 

Type and run "py manage.py runserver" to run the server and access the web project on the browser. The URL will be provided in the command prompt.

