"""
Streamlit UI for the multi-agent research pipeline defined in pipeline.py.

Run with:
    streamlit run app.py

Place this file in the SAME folder as pipeline.py, agents.py, and tools.py.
"""

import io
import contextlib
import streamlit as st

from pipeline import run_research_pipeline


# ---------------------------------------------------------------------------
# Page setup
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    page_icon="🔎",
    layout="wide",
)

st.title("🔎 Multi-Agent Research Assistant")
st.caption(
    "Enter a topic and watch the Search → Reader → Writer → Critic agent "
    "pipeline research it end-to-end."
)

# ---------------------------------------------------------------------------
# Session state (so results survive Streamlit re-runs)
# ---------------------------------------------------------------------------
if "result" not in st.session_state:
    st.session_state.result = None
if "logs" not in st.session_state:
    st.session_state.logs = ""

# ---------------------------------------------------------------------------
# Input form
# ---------------------------------------------------------------------------
with st.form("research_form"):
    topic = st.text_input(
        "Research topic",
        placeholder="e.g. Impact of quantum computing on cryptography",
    )
    submitted = st.form_submit_button("Run Research Pipeline", use_container_width=True)

# ---------------------------------------------------------------------------
# Run pipeline
# ---------------------------------------------------------------------------
if submitted:
    if not topic.strip():
        st.warning("Please enter a topic before running the pipeline.")
    else:
        status_box = st.status(
            "Running multi-agent pipeline... this can take a minute or two.",
            expanded=True,
        )

        # pipeline.py uses print() statements for progress; capture them
        # so we can show them inside the UI instead of only the terminal.
        captured_output = io.StringIO()

        try:
            with status_box:
                st.write("Step 1 — Search agent gathering sources...")
                st.write("Step 2 — Reader agent scraping top result...")
                st.write("Step 3 — Writer agent drafting the report...")
                st.write("Step 4 — Critic agent reviewing the report...")

                with contextlib.redirect_stdout(captured_output):
                    result = run_research_pipeline(topic)

            status_box.update(label="Pipeline complete ✅", state="complete", expanded=False)
            st.session_state.result = result
            st.session_state.logs = captured_output.getvalue()

        except Exception as e:
            status_box.update(label="Pipeline failed ❌", state="error", expanded=True)
            st.error(f"Something went wrong while running the pipeline:\n\n{e}")
            st.session_state.result = None
            st.session_state.logs = captured_output.getvalue()

# ---------------------------------------------------------------------------
# Display results
# ---------------------------------------------------------------------------
if st.session_state.result:
    result = st.session_state.result

    st.divider()
    st.subheader("📄 Final Report")
    st.markdown(result.get("report", "_No report generated._"))

    st.divider()
    st.subheader("🧪 Critic Feedback")
    st.markdown(result.get("feedback", "_No feedback generated._"))

    st.divider()
    with st.expander("🔍 Step 1 — Raw Search Results"):
        st.write(result.get("search_results", ""))

    with st.expander("📚 Step 2 — Scraped Content"):
        st.write(result.get("scraped_content", ""))

    if st.session_state.logs:
        with st.expander("🖥️ Full Terminal Log"):
            st.code(st.session_state.logs, language="text")

    # Download the final report as a markdown file
    st.download_button(
        label="⬇️ Download Report (.md)",
        data=result.get("report", ""),
        file_name="research_report.md",
        mime="text/markdown",
        use_container_width=True,
    )
else:
    st.info("Enter a topic above and click **Run Research Pipeline** to get started.")