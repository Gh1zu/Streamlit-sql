import streamlit as st
import pandas as pd

#create data frame
if "df" not in st.session_state:
    st.session_state.df=pd.DataFrame(columns=["ID","Name", "Email", "Phone number"])

if "index" not in st.session_state:
    st.session_state.index=0
st.title("Add user:")
# form

with st.form("user_form", clear_on_submit=False):

    st.subheader("Name:")
    user_name=st.text_input(label="",label_visibility="collapsed", key="user_name", placeholder="Name")
    st.subheader("Email:")
    user_email=st.text_input(label="", label_visibility="collapsed", key="user_email", placeholder="example@email.com")
    st.subheader("Phone number:")
    user_phone_number=st.text_input(label="", label_visibility="collapsed", key="user_phone_number", placeholder="###-###-###")

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
            if len(user_phone_number)<9:
                st.badge("Enter a valid phone number", icon=":material/error:", color="orange")
                valid=0
            if "@" not in user_email or "." not in user_email or len(user_email)<5:
                st.badge("Enter a valid email", icon=":material/error:", color="orange")
                valid=0
        
        if valid:
            st.session_state.index+=1
            form_data = {
                "ID": st.session_state.index,
                "Name": user_name,
                "Email": user_email,
                "Phone number": user_phone_number
            }
            st.session_state.df.loc[len(st.session_state.df)]=form_data
            
# delete all
if st.button("Delete all"):
    st.session_state.df=st.session_state.df.iloc[0:0]

# view

edited_df=st.data_editor(st.session_state.df, hide_index=True, num_rows="delete", key="editor")
st.session_state.df=edited_df