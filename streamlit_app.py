import streamlit as st
import pandas as pd
import random

# -------------------------------------------------
# BASIC PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="PenTrust – Healthcare Content Clarity Analyzer",
    layout="wide",
)

PRIMARY = "#F9D342"   # yellow
SECONDARY = "#F59E0B" # warm orange
ACCENT = "#2563EB"    # blue

# -------------------------------------------------
# GLOBAL STYLES (LIGHT UI)
# -------------------------------------------------
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: #F3F4F6;
        font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }}

    /* sidebar */
    [data-testid="stSidebar"] > div:first-child {{
        background-color: {PRIMARY};
        padding: 20px 18px 28px 18px;
        border-right: 1px solid rgba(15,23,42,0.08);
    }}

    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p {{
        color: #111827 !important;
    }}

    .brand-title {{
        font-size: 22px;
        font-weight: 800;
        margin-bottom: 4px;
    }}

    .brand-sub {{
        font-size: 12px;
        color: #4B5563;
        margin-bottom: 18px;
    }}

    .nav-pill {{
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 10px 12px;
        border-radius: 999px;
        margin-bottom: 8px;
        font-size: 14px;
        font-weight: 600;
        cursor: pointer;
        border: 1px solid rgba(15,23,42,0.08);
        background-color: #FEFCE8;
    }}

    .nav-pill.inactive {{
        background-color: rgba(255,255,255,0.6);
    }}

    .nav-pill span.icon {{
        font-size: 16px;
    }}

    /* main card */
    .main-block {{
        background-color: #F9FAFB;
        border-radius: 20px;
        padding: 20px 22px 26px 22px;
        box-shadow: 0 20px 45px rgba(15,23,42,0.07);
    }}

    .section-title {{
        font-size: 18px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 4px;
    }}
    .section-sub {{
        font-size: 13px;
        color: #6B7280;
        margin-bottom: 12px;
    }}

    .metric-card {{
        background-color: #FFFFFF;
        border-radius: 16px;
        padding: 14px 16px;
        border: 1px solid rgba(15,23,42,0.06);
        box-shadow: 0 10px 25px rgba(15,23,42,0.05);
        margin-bottom: 10px;
    }}
    .metric-label {{
        font-size: 13px;
        color: #6B7280;
        margin-bottom: 2px;
    }}
    .metric-value {{
        font-size: 24px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 0;
    }}
    .metric-delta {{
        font-size: 12px;
        color: #16A34A;
    }}

    .chip-bad {{
        display:inline-flex;
        align-items:center;
        gap:6px;
        padding:4px 10px;
        border-radius:999px;
        background-color:#FEF2F2;
        color:#B91C1C;
        font-size:12px;
        margin-right:6px;
        margin-bottom:4px;
    }}
    .chip-ok {{
        display:inline-flex;
        align-items:center;
        gap:6px;
        padding:4px 10px;
        border-radius:999px;
        background-color:#ECFEFF;
        color:#0E7490;
        font-size:12px;
        margin-right:6px;
        margin-bottom:4px;
    }}

    .content-box {{
        background-color:#FFFFFF;
        border-radius: 14px;
        padding: 12px 14px;
        border:1px solid rgba(15,23,42,0.06);
        font-size:13px;
        color:#111827;
        line-height:1.5;
        margin-bottom: 10px;
    }}
    .content-box.bad {{ border-left: 4px solid {SECONDARY}; }}
    .content-box.good {{ border-left: 4px solid #16A34A; }}

    .issue-item {{
        font-size: 13px;
        color: #B45309;
        margin-bottom: 4px;
    }}
    .suggest-item {{
        font-size: 13px;
        color: #166534;
        margin-bottom: 4px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------------------------------
# SIDEBAR NAV
# -------------------------------------------------
with st.sidebar:
    st.markdown(
        """
        <div class="brand-title">🩺 PenTrust</div>
        <div class="brand-sub">Healthcare Content Clarity Analyzer</div>
        """,
        unsafe_allow_html=True,
    )
    view = st.radio(
        "View",
        ["Dashboard", "Deep analysis"],
        label_visibility="collapsed",
    )

# -------------------------------------------------
# STATE
# -------------------------------------------------
if "pages" not in st.session_state:
    st.session_state["pages"] = []

# -------------------------------------------------
# FAKE ANALYSIS ENGINE (you can swap with real model later)
# -------------------------------------------------
def fake_analyze(label: str):
    # base scores
    clarity = random.randint(55, 88)
    wcag = random.randint(40, 95)
    next_steps = random.randint(50, 90)

    # classify statuses
    wcag_status = "At risk" if wcag < 70 else "Partially compliant" if wcag < 90 else "Solid"
    clarity_risk = "High" if clarity < 65 else "Medium" if clarity < 80 else "Low"

    issues = []
    if clarity < 75:
        issues.append("Critical instructions are buried in dense paragraphs.")
    if next_steps < 75:
        issues.append("Next steps are not clearly spelled out after key actions.")
    if wcag < 80:
        issues.append("WCAG signals: missing alt text / low contrast in key areas.")
    if not issues:
        issues.append("Minor phrasing improvements only; overall content is clear.")

    suggestions = {
        "Clarity": [
            "Break long paragraphs into short, scannable bullet lists.",
            "Front-load the most important action in the first sentence.",
        ],
        "Steps & next actions": [
            "Add a short checklist of 'What happens next' after form submissions.",
            "Use numbered steps instead of long narrative paragraphs.",
        ],
        "Accessibility & WCAG": [
            "Add meaningful alt text for icons and illustrations used as buttons.",
            "Check contrast for primary buttons against background using WCAG AA.",
        ],
        "Trust & safety tone": [
            "Replace fear-based warnings with calm, specific guidance.",
            "Clarify who to contact when something goes wrong (phone, portal message).",
        ],
    }

    bad_example = (
        "To access your lab results, the patient must ensure that all required "
        "authentication details are accurately entered prior to continuing. "
        "Failure to complete the verification sequence may result in a delay."
    )
    good_example = (
        "To view your lab results:\n"
        "1. Log in and open **Lab results**.\n"
        "2. Confirm your date of birth.\n"
        "3. Tap **View results**.\n\n"
        "If something doesn’t work, call us or send a secure message from the portal."
    )

    return {
        "label": label,
        "clarity": clarity,
        "wcag": wcag,
        "next_steps": next_steps,
        "wcag_status": wcag_status,
        "clarity_risk": clarity_risk,
        "issues": issues,
        "suggestions": suggestions,
        "bad_example": bad_example,
        "good_example": good_example,
    }

# -------------------------------------------------
# INPUT AREA (top of both views)
# -------------------------------------------------
st.markdown('<div class="main-block">', unsafe_allow_html=True)

top_cols = st.columns([2, 1])
with top_cols[0]:
    st.markdown(
        "<div class='section-title'>Content audit</div>"
        "<div class='section-sub'>Paste a few URLs or page labels from a healthcare portal, app, or message flow.</div>",
        unsafe_allow_html=True,
    )
with top_cols[1]:
    st.markdown(
        "<div style='text-align:right;font-size:12px;color:#6B7280;margin-top:6px;'>Today</div>",
        unsafe_allow_html=True,
    )

input_col, summary_col = st.columns([2, 1])

with input_col:
    urls_text = st.text_area(
        "Pages to review",
        placeholder=(
            "Example:\n"
            "https://hospital-portal.com/patient-login\n"
            "https://hospital-portal.com/medication-refill\n"
            "Discharge summary SMS copy"
        ),
        height=120,
    )
    run_btn = st.button("Run analysis")

with summary_col:
    if st.session_state["pages"]:
        avg_clarity = int(
            sum(p["clarity"] for p in st.session_state["pages"]) / len(st.session_state["pages"])
        )
        risky_pages = sum(1 for p in st.session_state["pages"] if p["clarity_risk"] != "Low")
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">Pages in current audit</div>
                <div class="metric-value">{len(st.session_state["pages"])}</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Avg. clarity score</div>
                <div class="metric-value">{avg_clarity}</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Pages with clarity / WCAG risk</div>
                <div class="metric-value">{risky_pages}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-label">No audit yet</div>
                <div class="metric-value">--</div>
                <div class="metric-delta">Paste pages and click “Run analysis”.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Run analysis
if run_btn and urls_text.strip():
    pages = []
    for line in urls_text.split("\n"):
        label = line.strip()
        if not label:
            continue
        pages.append(fake_analyze(label))
    st.session_state["pages"] = pages

pages = st.session_state["pages"]

st.markdown("<hr style='border-color:#E5E7EB;margin:16px 0;'/>", unsafe_allow_html=True)

# -------------------------------------------------
# DASHBOARD VIEW
# -------------------------------------------------
if view == "Dashboard":
    if not pages:
        st.markdown(
            "<div class='section-sub'>No results yet. Paste at least one URL or page label above and click <b>Run analysis</b>.</div>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            "<div class='section-title'>Dashboard</div>"
            "<div class='section-sub'>High-level view of clarity, next-step guidance, and WCAG signals across pages.</div>",
            unsafe_allow_html=True,
        )

        # Summary table
        df = pd.DataFrame(
            [
                {
                    "Page / message": p["label"],
                    "Clarity score": p["clarity"],
                    "Next-step clarity": p["next_steps"],
                    "WCAG score": p["wcag"],
                    "WCAG status": p["wcag_status"],
                    "Clarity risk": p["clarity_risk"],
                }
                for p in pages
            ]
        )

        chart_col, table_col = st.columns([1.1, 1.4])

        with chart_col:
            st.caption("Clarity score by page")
            chart_df = df[["Page / message", "Clarity score"]].set_index("Page / message")
            st.bar_chart(chart_df, height=260)

            st.caption("Where problems cluster")
            bad_wcag = sum(df["WCAG score"] < 80)
            bad_next = sum(df["Next-step clarity"] < 75)
            bad_clarity = sum(df["Clarity score"] < 75)

            st.markdown(
                f"""
                <div>
                    <span class="chip-bad">⚠️ Low clarity pages: {bad_clarity}</span>
                    <span class="chip-bad">⚠️ Weak next-step guidance: {bad_next}</span>
                    <span class="chip-bad">⚠️ WCAG at risk: {bad_wcag}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with table_col:
            st.caption("Pages in this audit")
            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True,
            )

# -------------------------------------------------
# DEEP ANALYSIS VIEW
# -------------------------------------------------
elif view == "Deep analysis":
    if not pages:
        st.markdown(
            "<div class='section-sub'>Run an analysis first, then come back here to inspect individual pages.</div>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            "<div class='section-title'>Deep analysis</div>"
            "<div class='section-sub'>Zoom into one page to see concrete problems and suggested fixes.</div>",
            unsafe_allow_html=True,
        )

        labels = [p["label"] for p in pages]
        selected_label = st.selectbox("Select a page or message", labels)
        page = next(p for p in pages if p["label"] == selected_label)

        top_cols2 = st.columns([1.2, 1])
        with top_cols2[0]:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">Overall clarity</div>
                    <div class="metric-value">{page['clarity']}</div>
                    <div class="metric-delta">Clarity risk: {page['clarity_risk']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with top_cols2[1]:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">WCAG signal</div>
                    <div class="metric-value">{page['wcag']}</div>
                    <div class="metric-delta">Status: {page['wcag_status']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("<br/>", unsafe_allow_html=True)

        cols = st.columns(2)

        # Left: problematic copy + issues
        with cols[0]:
            st.markdown("#### ⚠️ Customer’s problematic input")
            st.markdown(
                f"<div class='content-box bad'>{page['bad_example']}</div>",
                unsafe_allow_html=True,
            )
            st.markdown("**Key problems detected**")
            for issue in page["issues"]:
                st.markdown(f"<div class='issue-item'>⚠️ {issue}</div>", unsafe_allow_html=True)

        # Right: optimized copy + suggestions
        with cols[1]:
            st.markdown("#### ✅ Suggested optimized version")
            st.markdown(
                f"<div class='content-box good'>{page['good_example'].replace(chr(10), '<br/>')}</div>",
                unsafe_allow_html=True,
            )

        st.markdown("<br/>", unsafe_allow_html=True)

        # Category-based deep analysis (clarity, steps, WCAG, trust)
        st.markdown("#### Deep breakdown by category")

        for category, tips in page["suggestions"].items():
            st.markdown(f"**{category} – what PenTrust suggests**")
            for t in tips:
                st.markdown(f"<div class='suggest-item'>• {t}</div>", unsafe_allow_html=True)
            st.markdown("", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
