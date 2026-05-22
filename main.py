import streamlit as st
import pandas as pd
import sqlite3

# define connection and cursor

connection = sqlite3.connect("user_db.db") 

cursor = connection.cursor()

#create to_do table

cursor.execute(""" CREATE TABLE IF NOT EXISTS
users(user_id INTEGER PRIMARY KEY, user_name TEXT, user_email TEXT, user_phone_number TEXT)""")
connection.commit()

st.title("Add user:")

# form

with st.form("user_form", clear_on_submit=False):

    st.subheader("Name:")
    user_name=st.text_input(label="",label_visibility="collapsed", key="user_name", placeholder="Name")
    st.subheader("Email:")
    user_email=st.text_input(label="", label_visibility="collapsed", key="user_email", placeholder="example@email.com")
    st.subheader("Phone number:")
    user_phone_number=st.text_input(label="", label_visibility="collapsed", key="user_phone_number", placeholder="###-###-####")

    submit=st.form_submit_button("Add")

    if submit:
        valid=1
        

        if user_name == "" or user_email == "" or user_phone_number == "":
            st.badge("Please fill every row", icon=":material/error:", color="orange")
            valid=0
        else:
            try: 
                int(user_phone_number)
            except:
                st.badge("Enter a valid phone number", icon=":material/error:", color="orange")
                valid=0
            if "@" not in user_email or "." not in user_email:
                st.badge("Enter a valid email", icon=":material/error:", color="orange")
                valid=0
        
        if valid:
            cursor.execute("INSERT INTO users(user_name, user_email, user_phone_number) VALUES(?, ?, ?)", (user_name, user_email, user_phone_number))
            connection.commit()


# delete all
if st.button("Delete all"):
    cursor.execute("DELETE FROM users")
    connection.commit()

# view
df= pd.read_sql_query("SELECT * FROM users", connection)

edited_df=st.data_editor(df, hide_index=True, num_rows="delete")