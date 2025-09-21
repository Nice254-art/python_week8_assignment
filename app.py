import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv")
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    df["year"] = df["publish_time"].dt.year
    return df

df = load_data()

# Title
st.title("CORD-19 Data Explorer (Sample)")
st.write("Explore COVID-19 research papers using the sample metadata dataset.")

# Sidebar filters
st.sidebar.header("Filters")
years = st.sidebar.multiselect("Select publication years", options=df["year"].dropna().unique(), default=df["year"].dropna().unique())
journals = st.sidebar.multiselect("Select journals", options=df["journal"].unique(), default=df["journal"].unique())

# Apply filters
filtered_df = df[df["year"].isin(years) & df["journal"].isin(journals)]

# Show data preview
st.subheader("Sample of Filtered Data")
st.write(filtered_df.head())

# Publications per year
st.subheader("Publications by Year")
year_counts = filtered_df["year"].value_counts().sort_index()
fig, ax = plt.subplots()
year_counts.plot(kind="bar", ax=ax, color="skyblue")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Publications")
st.pyplot(fig)

# Top journals
st.subheader("Top Journals")
journal_counts = filtered_df["journal"].value_counts().head(5)
fig, ax = plt.subplots()
sns.barplot(x=journal_counts.values, y=journal_counts.index, ax=ax, palette="viridis")
ax.set_xlabel("Number of Publications")
ax.set_ylabel("Journal")
st.pyplot(fig)

# Source distribution
st.subheader("Publications by Source")
source_counts = filtered_df["source_x"].value_counts()
fig, ax = plt.subplots()
source_counts.plot(kind="pie", autopct="%1.1f%%", ax=ax, startangle=90, cmap="Set3")
ax.set_ylabel("")
st.pyplot(fig)

st.success("Analysis complete! 🎉")
