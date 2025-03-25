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

