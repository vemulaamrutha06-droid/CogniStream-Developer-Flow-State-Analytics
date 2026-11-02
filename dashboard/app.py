
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="CogniStream Analytics",
    page_icon="🧠",
    layout="wide"
)

# Load dataset
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "cleaned_developer_activity.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH, parse_dates=["date"])

df = load_data()

# Dashboard title
st.title("🧠 CogniStream")
st.subheader("Developer Flow-State & Cognitive Load Analytics")
st.caption("Understand developer focus, cognitive load and productivity.")

st.divider()

# Sidebar filters
st.sidebar.header("Dashboard Filters")

developers = st.sidebar.multiselect(
    "Select Developers",
    options=sorted(df["developer_id"].unique()),
    default=sorted(df["developer_id"].unique())
)

tasks = st.sidebar.multiselect(
    "Select Task Types",
    options=sorted(df["task_type"].unique()),
    default=sorted(df["task_type"].unique())
)

filtered_df = df[
    df["developer_id"].isin(developers)
    & df["task_type"].isin(tasks)
]

if filtered_df.empty:
    st.warning("No records match the selected filters.")
    st.stop()

# KPI cards
st.subheader("📊 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Records", f"{len(filtered_df):,}")
col2.metric("Average Focus", f"{filtered_df['focus_score'].mean():.1f}/100")
col3.metric("Average Cognitive Load", f"{filtered_df['cognitive_load'].mean():.1f}/100")
col4.metric("Average Productivity", f"{filtered_df['productivity_score'].mean():.1f}/100")

st.divider()

# Charts - Row 1
st.subheader("📈 Developer Analytics")

col1, col2 = st.columns(2)

with col1:
    fig = px.histogram(
        filtered_df,
        x="focus_score",
        nbins=20,
        title="Focus Score Distribution",
        color_discrete_sequence=["#3498db"]
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.histogram(
        filtered_df,
        x="cognitive_load",
        nbins=20,
        title="Cognitive Load Distribution",
        color_discrete_sequence=["#e67e22"]
    )
    st.plotly_chart(fig, use_container_width=True)

# Charts - Row 2
col1, col2 = st.columns(2)

with col1:
    task_data = filtered_df.groupby("task_type", as_index=False)[
        ["focus_score", "cognitive_load", "productivity_score"]
    ].mean()

    fig = px.bar(
        task_data,
        x="task_type",
        y=["focus_score", "cognitive_load", "productivity_score"],
        barmode="group",
        title="Performance by Task Type"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.scatter(
        filtered_df,
        x="focus_score",
        y="productivity_score",
        color="task_type",
        hover_data=["developer_id", "cognitive_load"],
        title="Focus vs Productivity"
    )
    st.plotly_chart(fig, use_container_width=True)

# Correlation heatmap
st.subheader("🔍 Correlation Analysis")

numeric_df = filtered_df.select_dtypes(include="number")
corr = numeric_df.corr()

fig = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale="RdBu_r",
    title="Developer Metrics Correlation Heatmap",
    aspect="auto"
)
st.plotly_chart(fig, use_container_width=True)

# Developer summary
st.subheader("👨‍💻 Developer Performance Summary")

summary = filtered_df.groupby("developer_id", as_index=False).agg(
    avg_focus=("focus_score", "mean"),
    avg_cognitive_load=("cognitive_load", "mean"),
    avg_productivity=("productivity_score", "mean"),
    total_commits=("commits", "sum"),
    total_bugs=("bugs_reported", "sum")
)

st.dataframe(
    summary.round(2),
    use_container_width=True,
    hide_index=True
)

# Raw records
with st.expander("View Dataset Records"):
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)

# Download cleaned data
csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Dataset",
    data=csv,
    file_name="cognistream_filtered_data.csv",
    mime="text/csv"
)

st.divider()
st.caption("CogniStream | Developer Flow-State & Cognitive Load Analytics")
