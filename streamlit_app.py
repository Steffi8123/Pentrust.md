import streamlit as st
import pandas as pd
import random
import textwrap

# -----------------------------
# Brand Colors (your palette)
# -----------------------------
PRIMARY = "#F9D342"     # warm yellow
SECONDARY = "#F59E0B"   # amber
ACCENT = "#2563EB"      # blue

BG = "#FFFFFF"
BG_SOFT = "#F8FAFC"
TEXT = "#0F172A"
MUTED = "#6B7280"
BORDER = "#E5E7EB"

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="PenTrust – Healthcare Content Clarity Analyzer",
    page_icon="✏️",
    layout="wide",
)

# -----------------------------
# Global styles
# -----------------------------
st.markdown(
    f"""
    <style>
    /* App background */
    .stApp {{
        background: {BG};
        color: {TEXT};
    }}

    /* Remove default top padding a bit tighter */
    .block-container {{
        padding-top: 1.4rem;
        padding-bottom: 2.5rem;
    }}

    /* Sidebar */
    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {PRIMARY} 0%, #FDE68A 100%);
        border-right: 1px solid rgba(0,0,0,0.06);
    }}

    /* Sidebar title area */
    .sidebar-brand {{
        font-size: 22px;
        font-weight: 800;
        color: #111827;
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 8px 4px 2px 4px;
    }}
    .sidebar-sub {{
        font-size: 12px;
        color: #1F2937;
        opacity: 0.9;
        margin-top: -2px;
        padding-left: 4px;
    }}

    /* Headlines */
    .section-title {{
        font-size: 34px;
        font-weight: 800;
        letter-spacing: -0.03em;
        margin-bottom: 2px;
        color: {TEXT};
    }}
    .section-sub {{
        font-size: 15px;
        color: {MUTED};
        margin-bottom: 18px;
    }}

    /* Input label */
    div[data-testid="stTextArea"] label {{
        font-weight: 700 !important;
        color: {TEXT} !important;
    }}

    /* Text area outline + placeholder */
    div[data-testid="stTextArea"] textarea {{
        border: 1.5px solid {BORDER} !important;
        border-radius: 12px !important;
        background: #FFFFFF !important;
        padding: 12px 12px !important;
        font-size: 14px !important;
        color: #111827 !important;
        box-shadow: 0 6px 14px rgba(15,23,42,0.04) !important;
    }}
    div[data-testid="stTextArea"] textarea:focus {{
        border: 2px solid {ACCENT} !important;
        box-shadow: 0 0 0 3px rgba(37,99,235,0.15) !important;
        outline: none !important;
    }}
    div[data-testid="stTextArea"] textarea::placeholder {{
        color: #9CA3AF !important;
    }}

    /* Primary button */
    .stButton > button {{
        background: {ACCENT};
        color: white;
        font-weight: 700;
        border-radius: 12px;
        border: none;
        padding: 0.65rem 1.1rem;
        box-shadow: 0 8px 18px rgba(37,99,235,0.18);
        transition: 0.15s ease;
    }}
    .stButton > button:hover {{
        transform: translateY(-1px);
        filter: brightness(0.98);
    }}

    /* Metric cards */
    .metric-card {{
        border-radius: 18px;
        padding: 18px 20px;
        background: white;
        border: 1px solid {BORDER};
        box-shadow: 0 10px 22px rgba(15,23,42,0.06);
        margin-bottom: 14px;
    }}
    .metric-label {{
        font-size: 14px;
        color: {MUTED};
        font-weight: 600;
    }}
    .metric-value {{
        font-size: 40px;
        font-weight: 800;
        letter-spacing: -0.03em;
        margin-top: 2px;
        color: {TEXT};
    }}
    .metric-delta {{
        font-size: 12px;
        color: {MUTED};
        margin-top: 2px;
    }}

    /* Soft cards */
    .soft-yellow {{
        background: linear-gradient(165deg, {PRIMARY} 0%, #FDE68A 100%);
        border: 1px solid rgba(0,0,0,0.04);
    }}
    .soft-blue {{
        background: linear-gradient(165deg, #DBEAFE 0%, #E0F2FE 100%);
        border: 1px solid rgba(0,0,0,0.04);
    }}
    .soft-cream {{
        background: #FFF7ED;
    }}

    /* Right rail panels */
    .rail-box {{
        border-radius: 14px;
        padding: 12px 14px;
        background: white;
        border: 1px solid {BORDER};
        margin-bottom: 10px;
    }}
    .rail-bad {{
        border-left: 4px solid {SECONDARY};
    }}
    .rail-good {{
        border-left: 4px solid #22C55E;
    }}

    /* Analysis cards */
    .analysis-card {{
        border-radius: 16px;
        padding: 18px 18px 12px 18px;
        background: white;
        border: 1px solid {BORDER};
        box-shadow: 0 8px 18px rgba(15,23,42,0.05);
        margin-bottom: 14px;
    }}
    .analysis-title {{
        font-size: 18px;
        font-weight: 800;
        margin-bottom: 6px;
    }}
    .analysis-meta {{
        font-size: 12px;
        color: {MUTED};
        margin-bottom: 10px;
    }}

    /* Problem -> Fix blocks */
    .pf-row {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 12px;
        margin-top: 8px;
    }}
    .pf-box {{
        border-radius: 12px;
        padding: 12px 12px 10px 12px;
        background: {BG_SOFT};
        border: 1px solid {BORDER};
    }}
    .pf-label {{
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 0.02em;
        color: {MUTED};
        margin-bottom: 6px;
        text-transform: uppercase;
    }}
    .pf-text {{
        font-size: 13.5px;
        color: {TEXT};
    }}

    /* Small pill */
    .pill {{
        display: inline-block;
        padding: 4px 8px;
        border-radius: 999px;
        font-size: 10.5px;
        font-weight: 800;
        background: #EEF2FF;
        color: #1D4ED8;
        margin-left: 6px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Data + fake analysis engine
# -----------------------------
def parse_urls(raw: str):
    lines = [l.strip() for l in raw.split("\n") if l.strip()]
    # allow URLs or page labels
    return lines

def fake_analyze(label: str):
    # Scores are directional / demo-ready
    clarity = random.randint(58, 92)
    next_steps = random.randint(55, 90)
    wcag = random.randint(60, 92)

    # Candidate problem bank aligned to your tool framing
    possible_issues = [
        "Next steps are unclear after key actions.",
        "Instructions are too dense for quick scanning.",
        "Tone feels high-stakes without clear reassurance.",
        "WCAG risk signals: missing alt text / contrast concerns.",
        "Terminology shifts across the flow (inconsistent labels).",
    ]

    issues = []
    if clarity < 75:
        issues.append("Instructions are too dense for quick scanning.")
    if next_steps < 75:
        issues.append("Next steps are unclear after key actions.")
    if wcag < 80:
        issues.append("WCAG risk signals: missing alt text / contrast concerns.")

    for i in possible_issues:
        if len(issues) >= 2:
            break
        if i not in issues:
            issues.append(i)

    issues = issues[:2]

    # Map each issue to a clear fix + example
    fix_map = {
        "Next steps are unclear after key actions.": {
            "fix": "Add explicit next-step microcopy and a single primary CTA. Use short, action-first language.",
            "before": "Your request was received. We’ll review it.",
            "after": "Request received. **Next:** Upload your insurance card to continue.",
        },
        "Instructions are too dense for quick scanning.": {
            "fix": "Break long paragraphs into 2–3 bullet steps. Surface the 1-line summary first.",
            "before": "To complete your appointment, please review the following detailed instructions...",
            "after": "**Book in 3 steps:** Choose date → Select provider → Confirm details.",
        },
        "Tone feels high-stakes without clear reassurance.": {
            "fix": "Reduce alarm-heavy phrases. Add brief reassurance and plain-language context.",
            "before": "Failure to act may result in serious complications.",
            "after": "Acting early helps reduce risk. If you’re unsure, we’ll guide you step by step.",
        },
        "WCAG risk signals: missing alt text / contrast concerns.": {
            "fix": "Audit headings, alt text, and contrast. Ensure error messages are text + not color-only.",
            "before": "Error shown only in red text.",
            "after": "Error with icon + text: “We couldn’t verify this field. Please re-enter your ID.”",
        },
        "Terminology shifts across the flow (inconsistent labels).": {
            "fix": "Standardize labels and match user mental models. Use one term per concept.",
            "before": "‘Visit’, ‘Session’, and ‘Appointment’ used interchangeably.",
            "after": "Use **‘Appointment’** consistently across steps and confirmations.",
        },
    }

    # Build detailed entries for deep analysis
    issue_details = []
    for i in issues:
        meta = fix_map.get(i, {
            "fix": "Simplify wording and add a clear next action.",
            "before": "Original copy example.",
            "after": "Improved copy example.",
        })
        issue_details.append({
            "issue": i,
            "fix": meta["fix"],
            "before": meta["before"],
            "after": meta["after"],
        })

    return {
        "label": label,
        "clarity": clarity,
        "next_steps": next_steps,
        "wcag": wcag,
        "issues": issues,
        "issue_details": issue_details,
    }

# -----------------------------
# Session state
# -----------------------------
if "pages" not in st.session_state:
    st.session_state.pages = []
if "selected_page" not in st.session_state:
    st.session_state.selected_page = None

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-brand">✏️ PenTrust</div>
        <div class="sidebar-sub">Healthcare content clarity analyzer</div>
        """,
        unsafe_allow_html=True,
    )

    view = st.radio(
        "Navigation",
        ["Dashboard", "Deep analysis"],
        label_visibility="collapsed",
    )

# -----------------------------
# Top input area (global)
# -----------------------------
st.markdown(
    "<div class='section-title'>PenTrust – Healthcare Content Clarity Analyzer</div>"
    "<div class='section-sub'>Paste URLs or page labels to simulate how an AI-assisted content audit can surface clarity, next-step, and accessibility risks.</div>",
    unsafe_allow_html=True,
)

urls_text = st.text_area(
    "Pages to review",
    placeholder="Paste links here…",
    height=120,
)

col_a, col_b, col_c = st.columns([0.18, 0.62, 0.20])
with col_a:
    run_btn = st.button("Run analysis")

with col_c:
    if st.session_state.pages:
        st.markdown(
            f"<span class='pill'>Last run: {len(st.session_state.pages)} pages</span>",
            unsafe_allow_html=True,
        )

if run_btn:
    inputs = parse_urls(urls_text)
    if not inputs:
        st.warning("Paste at least one URL or page label.")
    else:
        st.session_state.pages = [fake_analyze(i) for i in inputs]
        st.session_state.selected_page = st.session_state.pages[0]["label"]
        st.success("Analysis generated.")

pages = st.session_state.pages

# -----------------------------
# Helpers
# -----------------------------
def build_df(pages_list):
    return pd.DataFrame(
        [
            {
                "Page / message": p["label"],
                "Clarity score": p["clarity"],
                "Next-step clarity": p["next_steps"],
                "WCAG signal": p["wcag"],
                "Top issues (2)": " • ".join(p["issues"]),
            }
            for p in pages_list
        ]
    )

# -----------------------------
# DASHBOARD VIEW (Problems)
# -----------------------------
if view == "Dashboard":
    if not pages:
        st.info("No results yet. Add pages above and click **Run analysis**.")
    else:
        df = build_df(pages)

        # Aggregate
        avg_clarity = int(df["Clarity score"].mean())
        avg_next = int(df["Next-step clarity"].mean())
        avg_wcag = int(df["WCAG signal"].mean())
        low_clarity_pages = int((df["Clarity score"] < 75).sum())

        left, center, right = st.columns([1.1, 1.1, 0.9])

        # LEFT rail cards (match your layout)
        with left:
            st.markdown(
                f"""
                <div class="metric-card soft-yellow">
                    <div class="metric-label">Avg clarity score</div>
                    <div class="metric-value">{avg_clarity}</div>
                    <div class="metric-delta">Pages below 75: {low_clarity_pages}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                f"""
                <div class="metric-card soft-blue">
                    <div class="metric-label">Avg next-step clarity</div>
                    <div class="metric-value">{avg_next}</div>
                    <div class="metric-delta">Signals missing handoffs</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                f"""
                <div class="metric-card soft-cream">
                    <div class="metric-label">Avg WCAG signal</div>
                    <div class="metric-value">{avg_wcag}</div>
                    <div class="metric-delta">Directional indicator for review</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # CENTER cards + clarity chart
        with center:
            needs_review = max(1, len(pages) // 2)
            flagged_sections = random.randint(3, 12)

            st.markdown(
                f"""
                <div class="metric-card soft-blue">
                    <div class="metric-label">Pages needing review</div>
                    <div class="metric-value">{needs_review}</div>
                    <div class="metric-delta">Based on issue signals</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                f"""
                <div class="metric-card soft-blue">
                    <div class="metric-label">Flagged content sections</div>
                    <div class="metric-value">{flagged_sections}</div>
                    <div class="metric-delta">Clarity + guidance + accessibility</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.caption("Clarity score trend")
            chart_df = df[["Page / message", "Clarity score"]].set_index("Page / message")
            st.bar_chart(chart_df, height=220)

        # RIGHT Notifications + Activities
        with right:
            st.markdown("### Notifications")
            st.markdown(
                """
                <div class="rail-box rail-bad">⚠️ Clarity risk detected on at least one page</div>
                <div class="rail-box rail-bad">⚠️ Next-step guidance may be missing</div>
                <div class="rail-box rail-bad">⚠️ Accessibility signals need review</div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown("### Activities")
            st.markdown(
                """
                <div class="rail-box rail-good">✅ Analysis completed</div>
                <div class="rail-box">📝 Detailed fixes available in Deep analysis</div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("<br/>", unsafe_allow_html=True)

        # BIG TABLE
        st.markdown("#### Page-level summary")
        st.dataframe(df, use_container_width=True, hide_index=True)

# -----------------------------
# DEEP ANALYSIS VIEW (Solutions)
# -----------------------------
if view == "Deep analysis":
    if not pages:
        st.info("Run an analysis first to unlock deep analysis.")
    else:
        labels = [p["label"] for p in pages]
        selected = st.selectbox(
            "Select a page to review deeply",
            labels,
            index=0 if st.session_state.selected_page is None else labels.index(st.session_state.selected_page),
        )
        st.session_state.selected_page = selected

        page = next(p for p in pages if p["label"] == selected)

        st.markdown(
            f"""
            <div class="analysis-card">
                <div class="analysis-title">{page["label"]}</div>
                <div class="analysis-meta">
                    Clarity: <b>{page["clarity"]}</b> &nbsp;|&nbsp;
                    Next-step clarity: <b>{page["next_steps"]}</b> &nbsp;|&nbsp;
                    WCAG signal: <b>{page["wcag"]}</b>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("### Key issues and fixes")

        for idx, d in enumerate(page["issue_details"], start=1):
            issue = d["issue"]
            fix = d["fix"]
            before = d["before"]
            after = d["after"]

            st.markdown(
                f"""
                <div class="analysis-card">
                    <div class="analysis-title">{idx}. {issue}</div>
                    <div class="analysis-meta">This section shows a compact “problem → fix → example” narrative for presentation use.</div>

                    <div class="pf-row">
                        <div class="pf-box">
                            <div class="pf-label">⚠️ Problem signal</div>
                            <div class="pf-text">{issue}</div>
                        </div>
                        <div class="pf-box">
                            <div class="pf-label">✅ Suggested fix</div>
                            <div class="pf-text">{fix}</div>
                        </div>
                    </div>

                    <div class="pf-row">
                        <div class="pf-box">
                            <div class="pf-label">Before (sample copy)</div>
                            <div class="pf-text">{before}</div>
                        </div>
                        <div class="pf-box">
                            <div class="pf-label">After (clearer version)</div>
                            <div class="pf-text">{after}</div>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("### Expanded recommendations (presentation-friendly)")

        bullets = []
        if page["clarity"] < 80:
            bullets.append("Shorten intake instructions into 2–3 scannable steps.")
        if page["next_steps"] < 80:
            bullets.append("Add one explicit next action after every confirmation state.")
        if page["wcag"] < 85:
            bullets.append("Re-check contrast and ensure errors include icon + text description.")
        if not bullets:
            bullets = [
                "Refine headings for faster scanning in critical flows.",
                "Standardize terminology across interface and help content.",
            ]

        st.markdown(
            "- " + "\n- ".join(bullets)
        )

        # Optional: mini deep table per selected page
        st.markdown("<br/>", unsafe_allow_html=True)
        st.markdown("#### Issue breakdown (for notes or appendix)")
        issue_df = pd.DataFrame(
            [
                {
                    "Issue": x["issue"],
                    "Suggested fix": x["fix"],
                    "Before example": x["before"],
                    "After example": x["after"],
                }
                for x in page["issue_details"]
            ]
        )
        st.dataframe(issue_df, use_container_width=True, hide_index=True)
