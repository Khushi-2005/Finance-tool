
       
import streamlit as st
import preprocessor  # Assuming this is a custom module in your project
import helper  # Assuming this is a custom module in your project
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

st.set_page_config(layout='wide')
st.sidebar.title("Phonepe Transaction Analysis")
st.title("TOP STATISTICS")

file = st.sidebar.file_uploader('Upload CSV', type=['csv'])

if file is not None:
    data = pd.read_csv(file)

    # Preprocess the data using the preprocessor module
    df = preprocessor.preprocess(data)
    st.dataframe(df)

    # Create a list of unique user names for selection
    user_list = df['Name'].unique().tolist()
    user_list.sort()
    user_list.insert(0, "Overall")
    selected_user = st.sidebar.selectbox("Show analysis with respect to Name", user_list)

    if st.sidebar.button("Show Analysis"):
        # Fetch statistics using the helper module
        num_trans, deb, cre, top_debit_persons, top_credit_persons = helper.fetch_stats(selected_user, df)
        st.title("Top Statistics")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("No. of Transactions")
            st.subheader(num_trans)
        with col2:
            st.header("Total Debit")
            st.subheader(deb)
        with col3:
            st.header("Total Credit")
            st.subheader(cre)

        # Create columns for top debit and credit persons
        col4, col5 = st.columns(2)
        with col4:
            top_debit_persons.columns = ['Name', 'Debit Amount']
            st.write("Top 5 Debit:")
            st.write(top_debit_persons)

        with col5:
            top_credit_persons.columns = ['Name', 'Credit Amount']  # Ensure correct column name
            st.write("Top 5 Credit:")
            st.write(top_credit_persons)

        # Visualizations
        st.title("Total Amount Spent by Month")
        helper.total_amount_spent_by_month(selected_user, df)

        st.title("Percentage of Transaction Types")
        helper.Percentage_of_Transaction_Types(selected_user, df)

        st.title("Daily Amount Spent")
        helper.Dailyamountspend(selected_user, df)

        st.title("Day of Week")
        helper.Dayofweek(selected_user, df)

