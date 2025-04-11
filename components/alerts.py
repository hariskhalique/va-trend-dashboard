import streamlit as st
import pandas as pd

from data.mock_data import mock_alerts


def render_alerts_tab():
    st.subheader("Alerts & Emerging Trends")

    if not mock_alerts:
        st.info("No alerts to show at the moment.")
        return

    st.markdown("These are products showing unusual activity or sudden trend changes:")

    df = pd.DataFrame(mock_alerts)
    df = df.sort_values(by="timestamp", ascending=False)

    st.dataframe(df.reset_index(drop=True), use_container_width=True)

    st.warning("Use these alerts to act quickly on viral opportunities or prepare for unexpected demand surges.")
