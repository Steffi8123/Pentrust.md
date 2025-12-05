import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="PenTrust – Healthcare Content Clarity Analyzer",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Custom CSS (colors & layout)
# -----------------------------
PRIMARY = "#F9D342"   # main yellow
SECONDARY = "#F59E0B" # deeper yellow / orange
ACCENT = "#2563EB"    # blue

st.markdown(
    f"""
    <style>
    /* Global font */
    html, body, [class*="css"]  {{
        font-family: system-ui, -apple-system, BlinkMacSystemFont, "Inter", sans-serif;
    }}

    /* Sidebar styling */
    [data-testid="stSidebar"] {{
        background-color: {PRIMARY};
        padding-top: 24px;
        padding-left: 16px;
        padding-right: 16px;
    }}

    .sidebar-title {{
        font-size: 22px;
        font-weight: 700;
        color: #082F49;
        margin-bottom: 24px;
        display: flex;
        align-items: center;
        gap: 8px;
    }}

    .nav-item {{
        padding: 10px 14px;
        border-radius: 999px;
        margin-bottom: 6px;
        display: flex;
        align-items: center;
        font-size: 15px;
        font-weight: 500;
        color: #1F2937;
        opacity: 0.9;
    }}
    .nav-item span {{
        margin-right: 8px;
    }}
    .nav-item-active {{
        background-color: #FFFFFF;
        box-shadow: 0 6px 16px rgba(15,23,42,0.12);
    }}

    /* Metric cards */
    .metric-card {{
        border-radius: 24px;
        padding: 18px 20px;
        box-shadow: 0 10px 25px rgba(15,23,42,0.08);
    }}
    .metric-label {{
        font-size: 14px;
        color: #64748B;
        margin-bottom: 4px;
    }}
    .metric-value {{
        font-size: 30px;
        font-weight: 700;
        color: #020617;
        margin-bottom: 2px;
    }}
    .metric-trend {{
        font-size: 13px;
        color: #16A34A;
    }}

    /* Right panel */
    .panel {{
        background-color: #FFFFFF;
        border-radius: 24px;
        padding: 18px 20px;
        box-shadow: 0 10px 25px rgba(15,23,42,0.05);
    }}
    .panel h3 {{
        margin-top: 0;
        margin-bottom: 8px;
        font-size: 18px;
    }}
    .pill {{
        display: inline-block;
        padding: 4px 10px;
        border-radius: 999px;
        font-size: 12px;
        background-color: #E5F3FF;
        color: #1D4ED8;
        margin-bottom: 4px;
    }}
    .notif-item {{
        font-size: 14px;
        margin-bottom: 10px;
    }}
    .notif-time {{
        font-size: 12px;
        color: #94A3B8;
    }}

    /* Section titles */
    .section-title {{
        font-size: 18px;
        font-weight: 600;
        margin-top: 24px;
        margin-bottom: 8px;
    }}

    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Session state for data
# -----------------------------
if "data" not in st.session_state:
    st.session_state["data"] = pd.DataFrame()

# -----------------------------
# Sidebar – logo, nav, input
# -----------------------------
with st.sidebar:
    st.markdown(
        '<div class="sidebar-title">🩺 <span>PenTrust</span></div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '''
        <div class="nav-item nav-item-active"><span>📊</span>Dashboard</div>
        <div class="nav-item"><span>📄</span>Analysis</div>
        <div class="nav-item"><span>📝</span>Reports</div>
        <div class="nav-item"><span>🛡️</span>Compliance</div>
        <div class="nav-item"><span>👥</span>Team</div>
        ''',
        unsafe_allow_html=True,
    )

    st.markdown("---")

    urls_text = st.text_area(
        "Paste page URLs or labels (one per line)",
        placeholder="https://example-hospital.com/patient-portal\nhttps://example-healthplan.com/claims\n...",
        height=150,
    )

    run = st.button("Run analysis")

# -----------------------------
# Fake analysis when button clicked
# -----------------------------
if run and urls_text.strip():
    raw_urls = [u.strip() for u in urls_text.splitlines() if u.strip()]
    rows = []
    now = datetime.now().strftime("%b %d, %H:%M")

    rng = np.random.default_rng(42)  # fixed seed for stable demo

    for i, url in enumerate(raw_urls, start=1):
        clarity = rng.integers(68, 96)
        trust = rng.integers(60, 94)
        risk_flags = rng.integers(0, 4)
        reading = rng.choice(["Easy", "Moderate", "Complex"], p=[0.4, 0.45, 0.15])

        rows.append(
            {
                "Page": f"Page {i}",
                "URL": url,
                "Clarity Score": clarity,
                "Trust Score": trust,
                "Risk Flags": risk_flags,
                "Reading Level": reading,
                "Last Scan": now,
            }
        )

    st.session_state["data"] = pd.DataFrame(rows)

df = st.session_state["data"]

# -----------------------------
# Main layout
# -----------------------------
st.markdown("## ")  # small top spacer

left_col, right_col = st.columns([3, 1.3])

with left_col:
    # Header row
    header_col1, header_col2 = st.columns([4, 1])
    with header_col1:
        st.markdown("## Dashboard")
    with header_col2:
        st.markdown(
            f"<div style='text-align:right; color:#64748B; margin-top:10px;'>Today</div>",
            unsafe_allow_html=True,
        )

    # If we have data, compute aggregates
    if not df.empty:
        total_pages = len(df)
        avg_clarity = int(df["Clarity Score"].mean())
        avg_trust = int(df["Trust Score"].mean())
        high_risk = int((df["Risk Flags"] >= 2).sum())

        # Top metrics row
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(
                f"""
                <div class="metric-card" style="background-color:{PRIMARY};">
                    <div class="metric-label">Pages analyzed today</div>
                    <div class="metric-value">{total_pages}</div>
                    <div class="metric-trend">+11.0% ↗</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with c2:
            st.markdown(
                f"""
                <div class="metric-card" style="background-color:#DBEAFE;">
                    <div class="metric-label">Average clarity score</div>
                    <div class="metric-value">{avg_clarity}</div>
                    <div class="metric-trend">Target ≥ 85</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Second metrics row
        c3, c4 = st.columns(2)
        with c3:
            st.markdown(
                f"""
                <div class="metric-card" style="background-color:#FEF3C7;">
                    <div class="metric-label">Average trust score</div>
                    <div class="metric-value">{avg_trust}</div>
                    <div class="metric-trend">Improved after last rewrite</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with c4:
            st.markdown(
                f"""
                <div class="metric-card" style="background-color:#E0F2FE;">
                    <div class="metric-label">Pages with high-risk flags</div>
                    <div class="metric-value">{high_risk}</div>
                    <div class="metric-trend" style="color:#DC2626;">Needs review</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Focus select
        st.markdown('<div class="section-title">Clarity score trend</div>', unsafe_allow_html=True)

        focus_options = ["All pages"] + df["Page"].tolist()
        focus = st.selectbox("Focus view", focus_options, index=0, label_visibility="collapsed")

        if focus == "All pages":
            focus_df = df.copy()
        else:
            focus_df = df[df["Page"] == focus]

        # Simple bar chart using focus_df
        chart_data = pd.DataFrame(
            {
                "Page": focus_df["Page"],
                "Clarity Score": focus_df["Clarity Score"],
            }
        ).set_index("Page")
        st.bar_chart(chart_data)

        # Detail table
        st.markdown('<div class="section-title">Page details</div>', unsafe_allow_html=True)
        st.dataframe(
            focus_df[["Page", "URL", "Clarity Score", "Trust Score", "Risk Flags", "Reading Level", "Last Scan"]],
            use_container_width=True,
            hide_index=True,
        )

    else:
        st.info(
            "Paste a few healthcare URLs or page labels in the sidebar and click **Run analysis** "
            "to populate the PenTrust dashboard."
        )

# -----------------------------
# Right notifications / activity column
# -----------------------------
with right_col:
    st.markdown(
        f"""
        <div class="panel">
            <h3>Notifications</h3>
            <div class="notif-item">
                ⚠️ Tone alert detected<br/>
                <span class="notif-time">Patient discharge email · just now</span>
            </div>
            <div class="notif-item">
                👥 New workspace added<br/>
                <span class="notif-time">Cardiology service line · 4 min ago</span>
            </div>
            <div class="notif-item">
                ✅ Batch analysis complete<br/>
                <span class="notif-time">Insurance FAQ set · 12 min ago</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="panel">
            <h3>Activities</h3>
            <div class="notif-item">
                📄 UX team reviewed 3 high-risk pages<br/>
                <span class="notif-time">Just now</span>
            </div>
            <div class="notif-item">
                ✏️ Content designer updated consent form copy<br/>
                <span class="notif-time">18 min ago</span>
            </div>
            <div class="notif-item">
                🛡️ Compliance approved revised SMS template<br/>
                <span class="notif-time">43 min ago</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
