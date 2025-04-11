import streamlit as st
import pandas as pd

from data.mock_data import mock_trending_products


def render_trending_tab():
    st.subheader("Trending Products")

    df = pd.DataFrame(mock_trending_products)

    # Sorting option
    sort_by = st.selectbox("Sort by", ["trend_score", "mention_count", "avg_sentiment"])
    df = df.sort_values(by=sort_by, ascending=False)

    # Filter by platform
    platforms = df["platform"].unique().tolist()
    selected_platforms = st.multiselect("Filter by Platform", platforms, default=platforms)
    df = df[df["platform"].isin(selected_platforms)]

    # Show top N
    top_n = st.slider("Show top N products", 5, 30, 10)
    df = df.head(top_n)

    # Render table
    st.dataframe(
        df[["product_name", "platform", "mention_count", "avg_sentiment", "forecast", "trend_score"]].reset_index(
            drop=True), use_container_width=True)

    # Optional: Highlight top product
    top_product = df.iloc[0]
    st.markdown("---")
    st.markdown(f"### Top Trending: **{top_product['product_name']}**")
    st.markdown(f"**Platform:** {top_product['platform']}  ")
    st.markdown(f"**Mentions:** {top_product['mention_count']}  ")
    st.markdown(f"**Avg Sentiment:** {top_product['avg_sentiment']}  ")
    st.markdown(f"**Trend Score:** {top_product['trend_score']}  ")
    st.markdown(f"**Forecast:** {top_product['forecast']}  ")
