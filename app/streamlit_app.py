import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Advanced Poll Analytics Dashboard",
    layout="wide"
)

df = pd.read_csv("data/poll_data.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

st.sidebar.title("Control Panel")

region_filter = st.sidebar.multiselect(
    "Region",
    df["region"].unique(),
    default=df["region"].unique()
)

age_filter = st.sidebar.multiselect(
    "Age Group",
    df["age_group"].unique(),
    default=df["age_group"].unique()
)

mode = st.sidebar.radio(
    "View Mode",
    ["Overview", "Deep Analysis"]
)

filtered_df = df[
    (df["region"].isin(region_filter)) &
    (df["age_group"].isin(age_filter))
]

st.title("Advanced Poll Analytics System")

st.markdown("Real-time simulation of survey intelligence system")

st.markdown("---")

vote_counts = filtered_df["option_selected"].value_counts()
top_option = vote_counts.idxmax()
total = len(filtered_df)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Responses", total)
col2.metric("Top Option", top_option)
col3.metric("Options Count", filtered_df["option_selected"].nunique())
col4.metric("Regions", filtered_df["region"].nunique())

st.markdown("---")

lead_margin = vote_counts.max() - vote_counts.min()
dominance_score = (vote_counts.max() / total) * 100

st.subheader("Analytics Summary")


if mode == "Deep Analysis":

    st.markdown("---")
    st.subheader("Deep Analytical Insights")

    total = len(filtered_df)
    vote_counts = filtered_df["option_selected"].value_counts()

    # 1. Winner Strength
    dominance = (vote_counts.max() / total) * 100

    # 2. Spread (stability)
    spread = vote_counts.std()

    # 3. Region influence
    region_strength = filtered_df.groupby("region")["option_selected"].count().max()

    # 4. Age influence
    age_strength = filtered_df.groupby("age_group")["option_selected"].count().max()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Winner Dominance %", round(dominance, 2))

    with col2:
        st.metric("Result Spread", round(spread, 2))

    with col3:
        st.metric("Max Region Influence", region_strength)

    st.markdown("### Business Interpretation")

    if dominance > 70:
        st.success("Strong market leader detected. Safe decision recommended.")
    elif dominance > 50:
        st.warning("Moderate dominance. Market still competitive.")
    else:
        st.error("Highly fragmented results. Avoid single-option decisions.")

    if spread < 5:
        st.info("Stable voting pattern observed across users.")
    else:
        st.info("High variation detected — segmented audience behavior.")

    st.write("Recommendation:")
    st.write("- Focus on top performing segment")
    st.write("- Run targeted campaigns for weak regions")
    st.write("- Collect more data for stable prediction")


col1, col2 = st.columns(2)

with col1:
    st.write("Lead Margin:", lead_margin)
    st.write("Dominance Score:", round(dominance_score, 2), "%")

with col2:
    if dominance_score > 60:
        st.success("Strong dominance detected in poll results")
    else:
        st.warning("Competitive distribution detected")

st.markdown("---")

region_data = filtered_df.groupby(["region", "option_selected"]).size().reset_index(name="count")
age_data = filtered_df.groupby(["age_group", "option_selected"]).size().reset_index(name="count")


st.subheader("Poll Visualization Dashboard")

col1, col2 = st.columns(2)

with col1:
    fig1 = px.bar(
        x=vote_counts.index,
        y=vote_counts.values,
        title="Vote Distribution",
        height=350
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.pie(
        values=vote_counts.values,
        names=vote_counts.index,
        title="Vote Share",
        height=350
    )
    st.plotly_chart(fig2, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    fig3 = px.bar(
        region_data,
        x="region",
        y="count",
        color="option_selected",
        barmode="stack",
        title="Region Behavior",
        height=350
    )
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    fig4 = px.bar(
        age_data,
        x="age_group",
        y="count",
        color="option_selected",
        barmode="group",
        title="Age Behavior",
        height=350
    )
    st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

st.subheader("Executive Insights")

st.write("Most Preferred Option:", top_option)

if dominance_score > 70:
    st.success("Clear market leader identified. Strong decision confidence.")
elif dominance_score > 50:
    st.info("Moderate preference detected. Further segmentation recommended.")
else:
    st.warning("No dominant option. Market is fragmented.")

st.write("Business Recommendation:")
st.write("- Focus marketing on top option segment")
st.write("- Analyze underperforming segments for improvement")
st.write("- Use demographic targeting for better conversion")
