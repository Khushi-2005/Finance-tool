import matplotlib.pyplot as plt
import streamlit as st

def fetch_stats(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['Name'] == selected_user]
    # Fetch the number of transactions
    num_trans = df.shape[0]
    deb = df[df['Type'] == 'DEBIT']['Amount'].sum()
    cre = df[df['Type'] == 'CREDIT']['Amount'].sum()
    
    debit_data = df[df['Type'] == 'DEBIT']
    top_debit_persons = debit_data.groupby('Name')['Amount'].sum().nlargest(5).reset_index()
    top_debit_persons.columns = ['Name', 'Debit Amount']
    
    credit_data = df[df['Type'] == 'CREDIT']
    top_credit_persons = credit_data.groupby('Name')['Amount'].sum().nlargest(5).reset_index()
    top_credit_persons.columns = ['Name', 'Credit Amount']
    
    return num_trans, deb, cre, top_debit_persons, top_credit_persons

def total_amount_spent_by_month(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['Name'] == selected_user]
    monthly_data = df.groupby('Month')['Amount'].sum()
    
    # Plotting the bar chart
    plt.figure(figsize=(14, 6))  # Fixed the figsize tuple
    colors = plt.cm.tab20c.colors[:len(monthly_data)]
    bars = plt.bar(monthly_data.index, monthly_data.values, color=colors, edgecolor='black')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xlabel('Month', fontsize=12, fontweight='bold')
    plt.ylabel('Total Amount', fontsize=12, fontweight='bold')
    plt.title('Total Amount Spent by Month', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45)
    plt.yticks(fontsize=10) 
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 5, round(yval, 2), ha='center', va='bottom')
    st.pyplot(plt)
    plt.close()  # Closing the figure to avoid memory issues

def Percentage_of_Transaction_Types(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['Name'] == selected_user]
    plt.figure(figsize=(16, 2))
    transaction_types = df['Type'].value_counts()
    colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3']
    plt.pie(transaction_types, labels=transaction_types.index, autopct='%1.1f%%', startangle=10,
            colors=colors, shadow=True)
    plt.title('Percentage of Transaction Types', fontweight='bold', fontsize=20)
    st.pyplot(plt)
    plt.close()  # Closing the figure to avoid memory issues

def Dailyamountspend(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['Name'] == selected_user]
    daily_data = df.groupby('Date')['Amount'].sum()
    plt.figure(figsize=(14, 6))
    plt.plot(daily_data.index, daily_data.values, marker='o', linestyle='-', color='b')
    plt.xlabel('Date', fontsize=12, fontweight='bold')
    plt.ylabel('Total Amount', fontsize=12, fontweight='bold')
    plt.title('Daily Total Amount Spent', fontsize=14, fontweight='bold')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45, fontsize=10)
    plt.yticks(fontsize=10)
    st.pyplot(plt)
    plt.close()  # Closing the figure to avoid memory issues

def Dayofweek(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['Name'] == selected_user]
    day_of_week_data = df.groupby('Day_of_Week')['Amount'].sum()

    # Plotting the bar chart with customizations
    plt.figure(figsize=(14, 6))
    plt.bar(day_of_week_data.index, day_of_week_data.values, color='skyblue', edgecolor='black')
    plt.xlabel('Day of Week', fontsize=12, fontweight='bold')
    plt.ylabel('Total Amount', fontsize=12, fontweight='bold')
    plt.title('Total Amount Spent by Day of Week', fontsize=14, fontweight='bold')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.yticks(fontsize=10)
    st.pyplot(plt)
    plt.close()  # Closing the figure to avoid memory issues
