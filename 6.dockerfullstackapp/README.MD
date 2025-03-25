Full Stack App Using Docker 🐳🌐
In this project, we will deploy a Full Stack Application using Docker. The application consists of a Streamlit frontend and a PostgreSQL database backend, both running in separate Docker containers. These containers will communicate via a custom Docker network, ensuring seamless interaction between the frontend and the database.

By the end of this tutorial, you will have a fully functional full-stack application running inside Docker containers, ready for development or production use. 🚀

Project Overview 📖
This project demonstrates how to containerize a full-stack application using Docker. The application includes:

PostgreSQL Database: A containerized database to store and manage data.
Streamlit Frontend: A containerized web application to interact with the database and display data.
The two containers are connected via a custom Docker network, enabling secure and efficient communication.

Prerequisites 📋
Before we begin, ensure you have the following installed on your system:

Docker: A platform for developing, shipping, and running applications in containers.
Docker Desktop: A tool to manage Docker containers on your local machine.
Step 1: Create a Docker Network 🌐
To enable communication between the database and the Streamlit app, we will create a custom Docker network in bridge mode.

Run the following command:

docker network create my_network
my_network: The name of the custom network. This network will act as a communication bridge between the containers.
Step 2: Set Up the Database Container 🗄️
We will use PostgreSQL as the database for this project. Run the following command to create a PostgreSQL container:

docker run -d \
  --name my_postgres \
  --network my_network \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=adminpassword \
  -e POSTGRES_DB=mydb \
  postgres
Explanation of the Command:

-d: Runs the container in detached mode.
--name my_postgres: Assigns a name to the container.
--network my_network: Connects the container to the custom network.
Environment Variables:
POSTGRES_USER: Sets the database username.
POSTGRES_PASSWORD: Sets the database password.
POSTGRES_DB: Creates a database named mydb.
postgres: The official PostgreSQL Docker image.
Step 3: Create the Streamlit App Container 🐍
Step 3.1: Create a Dockerfile for Streamlit

In your Streamlit project folder, create a Dockerfile with the following content:

# Use Python as the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "stream.py", "--server.port=8501", "--server.address=0.0.0.0"]
Step 3.2: Create requirements.txt

Ensure your requirements.txt file includes the following dependencies:

streamlit
psycopg2
Step 3.3: Build the Streamlit Image

Run the following command to build the Docker image:

docker build -t my_streamlit_app .
my_streamlit_app: The name of the Docker image.
Step 3.4: Run the Streamlit Container

Start the Streamlit container and connect it to the custom network:

docker run -d \
  --name streamlit_app \
  --network my_network \
  -p 8501:8501 \
  my_streamlit_app
-p 8501:8501: Maps port 8501 on your local machine to port 8501 in the container.
Step 4: Connect the Streamlit App to PostgreSQL 🔗
Step 4.1: Create stream.py

In your Streamlit project folder, create a file named stream.py with the following content:

import psycopg2
import streamlit as st
import pandas as pd

# Database connection
conn = psycopg2.connect(
    dbname="my_database",
    user="postgres",
    password="your_password",
    host="172.17.0.4",
    port=5432
)


# Query to fetch data
try:
    query = "SELECT * FROM public.users;"
    df = pd.read_sql(query, conn)

    if not df.empty:
        st.write("### User Data", df)
    else:
        st.warning("No data available in the database yet.")

except Exception as e:
    st.error(f"Error fetching data: {e}")

finally:
    conn.close()

Step 4.2: Test the Setup

Open your web browser and navigate to:

http://localhost:8501
Step 5: Insert Dummy Data 📊
Step 5.1: Connect to the PostgreSQL Container

Access the PostgreSQL database inside the container:

docker exec -it my_postgres psql -U admin -d mydb
Step 5.2: Create a Sample Table and Insert Data

Run the following SQL commands to create a table and insert dummy data:
Step 4.2: Test the Setup

Open your web browser and navigate to:

http://localhost:8501
Step 5: Insert Dummy Data 📊
Step 5.1: Connect to the PostgreSQL Container

Access the PostgreSQL database inside the container:

docker exec -it my_postgres psql -U admin -d mydb
Step 5.2: Create a Sample Table and Insert Data

Run the following SQL commands to create a table and insert dummy data: