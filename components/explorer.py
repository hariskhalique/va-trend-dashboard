# 📁 streamlit_app/components/explorer.py

import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from streamlit_app.data.mock_data import mock_product_details


def render_explorer_tab():
    st.subheader("Product Explorer")

    product_names = list(mock_product_details.keys())
    selected_product = st.selectbox("Select a product to explore", product_names)

    product = mock_product_details[selected_product]

    # Display forecast summary
    st.markdown(f"### Forecast: {product['forecast']}")

    col1, col2 = st.columns(2)

    # Sentiment chart
    with col1:
        st.markdown("**Sentiment Score (Last 5 Days)**")
        fig, ax = plt.subplots(figsize=(6, 3))
        ax.plot(product["sentiment_history"], marker="o", linestyle="--", color="#28a745")
        ax.set_ylabel("Sentiment Score")
        ax.set_xlabel("Days")
        ax.set_title(f"Sentiment Trend for {selected_product}")
        ax.yaxis.set_major_locator(MaxNLocator(nbins=5))
        ax.grid(True, linestyle="--", alpha=0.5)
        st.pyplot(fig)

    # Mention chart
    with col2:
        st.markdown("**Mentions (Last 5 Days)**")
        fig, ax = plt.subplots(figsize=(6, 3))
        bars = ax.bar(range(5), product["mention_history"], color="#17a2b8")
        ax.set_ylabel("Mentions")
        ax.set_xlabel("Days")
        ax.set_title(f"Mention Volume for {selected_product}")
        ax.yaxis.set_major_locator(MaxNLocator(nbins=5))
        ax.grid(True, linestyle="--", axis="y", alpha=0.5)

        # Add value labels
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=8)

        st.pyplot(fig)

    # Hashtags
    st.markdown("---")
    st.markdown("**Top Hashtags:**")
    st.write(", ".join(product["top_hashtags"]))
