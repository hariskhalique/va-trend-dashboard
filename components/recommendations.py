import streamlit as st
import matplotlib.pyplot as plt

from streamlit_app.data.mock_data import mock_recommendations, mock_product_details


def render_recommendations_tab():
    st.subheader("Weekly Product Recommendations")

    st.markdown("These product suggestions are based on current sentiment trends, forecast signals, and social buzz analysis:")

    filter_option = st.radio("Filter by trend type", ["All", "Rising", "Dipping"], horizontal=True)

    for product_name in mock_recommendations:
        details = mock_product_details.get(product_name)
        if not details:
            continue

        # Determine trend direction
        is_rising = details["sentiment_history"][-1] > details["sentiment_history"][0]
        trend_label = "Rising" if is_rising else "Dipping"
        trend_color = "#28a745" if is_rising else "#dc3545"

        # Filter logic
        if filter_option == "Rising" and not is_rising:
            continue
        if filter_option == "Dipping" and is_rising:
            continue

        with st.container():
            st.markdown(f"### {trend_label} — **{product_name}**")
            st.markdown(f"**Forecast:** {details['forecast']}")
            st.markdown(f"**Top Hashtags:** {', '.join(details['top_hashtags'])}")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**Sentiment Trend**")
                fig, ax = plt.subplots(figsize=(4, 2))
                ax.plot(details["sentiment_history"], marker="o", linestyle="--", color=trend_color)
                ax.set_ylabel("Sentiment")
                ax.set_xticks(range(5))
                ax.set_xticklabels(["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"])
                ax.grid(True, linestyle="--", alpha=0.4)
                st.pyplot(fig)

            with col2:
                st.markdown("**Mentions Volume**")
                fig, ax = plt.subplots(figsize=(4, 2))
                bars = ax.bar(range(5), details["mention_history"], color="#17a2b8")
                ax.set_ylabel("Mentions")
                ax.set_xticks(range(5))
                ax.set_xticklabels(["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"])
                ax.grid(True, linestyle="--", axis="y", alpha=0.3)
                for bar in bars:
                    height = bar.get_height()
                    ax.annotate(f'{height}',
                                xy=(bar.get_x() + bar.get_width() / 2, height),
                                xytext=(0, 3),
                                textcoords="offset points",
                                ha='center', va='bottom', fontsize=8)
                st.pyplot(fig)

    st.info("Use this panel to prioritize rising opportunities or monitor dipping trends for tactical decisions.")
