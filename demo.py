import streamlit as st
import pandas as pd

# Page title
st.title("Civil Engineering Research Dashboard")

# Read Excel file
df = pd.read_excel("faculty_research.xlsx")

# Show complete table
st.subheader("Faculty Research Progress")

st.dataframe(df)

# Basic statistics
st.subheader("Department Statistics")

total_papers = len(df)

published = len(df[df["Status"] == "Published"])

under_review = len(df[df["Status"] == "Under Review"])

draft = len(df[df["Status"] == "Draft"])

st.write("Total Research Entries:", total_papers)
st.write("Published Papers:", published)
st.write("Under Review Papers:", under_review)
st.write("Draft Papers:", draft)