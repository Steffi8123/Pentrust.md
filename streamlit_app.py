import streamlit as st
import pandas as pd

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Web Clarity, Empathy & Accessibility Check",
    page_icon="♿",
    layout="wide",
)

# ---------- GLOBAL STYLES ----------
st.markdown(
    """
<style>
:root {
  --purple-900: #1E1035;
  --purple-700: #3D2B7A;
  --purple-500: #6D4DE6;
  --purple-soft: #F4EEFF;
  --amber-400:  #FBBF24;
  --green-500:  #16A34A;
  --red-500:    #DC2626;
}

/* Base layout */
body, .stApp {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "SF Pro Text",
               "Segoe UI", sans-serif;
  background: radial-gradient(circle at top left, #F4EEFF 0, #F7F7FB 45%, #FFFFFF 100%);
}

/* Tighten main container a bit */
.block-container {
  padding-top: 1.2rem;
  padding-bottom: 2.2rem;
}

/* Buttons */
.stButton>button {
  background: var(--purple-500);
  color: #FFFFFF;
  border-radius: 999px;
  padding: 0.5rem 1.6rem;
  border: none;
  font-weight: 600;
  letter-spacing: 0.02em;
}
.stButton>button:hover {
  background: var(--purple-700);
}

/* Section title */
.section-title {
  font-size: 1.1rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--purple-700);
  margin-bottom: 0.3rem;
}
.section-kicker {
  font-size: 0.8rem;
  color: #6B7280;
  text-transform: uppercase;
  letter-spacing: 0.16em;
}

/* Hero card */
.hero-card {
  background: linear-gradient(135deg, var(--purple-900) 0%, #4C1D95 40%, #7C3AED 100%);
  color: white;
  border-radius: 18px;
  padding: 22px 24px;
  box-shadow: 0 14px 40px rgba(15,23,42,0.35);
}
.hero-title {
  font-size: 1.6rem;
  font-weight: 650;
  margin-bottom: 0.25rem;
}
.hero-subtitle {
  font-size: 0.98rem;
  color: #E5E7EB;
}

/* Generic cards */
.card {
  background: #FFFFFF;
  border-radius: 16px;
  padding: 18px 20px;
  box-shadow: 0 10px 30px rgba(15, 23, 42, 0.06);
  margin-bottom: 1rem;
}
.card-soft {
  background: var(--purple-soft);
  border-radius: 16px;
  padding: 16px 18px;
  margin-bottom: 1rem;
}
.card-border {
  border-left: 5px solid var(--purple-500);
}

/* KPI tiles */
.kpi-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 0.9rem;
}
.kpi {
  background: #FFFFFF;
  border-radius: 14px;
  padding: 0.7rem 0.9rem;
  box-shadow: 0 6px 18px rgba(15,23,42,0.05);
}
.kpi-label {
  font-size: 0.78rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: #6B7280;
}
.kpi-value {
  font-size: 1.3rem;
  font-weight: 650;
  margin-top: 0.15rem;
}
.kpi-meta {
  font-size: 0.8rem;
  color: #6B7280;
}

/* Pills */
.pill {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.17rem 0.7rem;
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 500;
}
.pill-demo {
  background: rgba(55,65,81,0.18);
  color: #111827;
}
.pill-pass {
  background: rgba(22,163,74,0.12);
  color: var(--green-500);
}
.pill-risk {
  background: rgba(220,38,38,0.08);
  color: var(--red-500);
}

/* Divider label */
.divider-label {
  display: flex;
  align-items: center;
  gap: 0.7rem;
  margin: 1.2rem 0 0.5rem 0;
}
.divider-label hr {
  flex: 1;
  border: none;
  border-top: 1px solid #E5E7EB;
}

/* Recommendation bullets */
.reco-list li {
  margin-bottom: 0.15rem;
}

/* Make select + textarea labels cleaner */
label {
  font-weight: 500 !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# ---------- TITLE / HERO ----------
hero_left, hero_right = st.columns([2.7, 1.3])

with hero_left:
    st.markdown(
        """
        <div class="hero-card">
          <div class="section-kicker">Madison · Healthcare-inspired UX</div>
          <div class="hero-title">Web Clarity, Empathy & Accessibility Check</div>
          <p class="hero-subtitle">
            A concept dashboard that treats your marketing pages like a patient:
            checking whether the language is clear, supportive, and friendly to assistive tech.
          </p>
          <div style="margin-top: 0.6rem; font-size:0.8rem; color:#E5E7EB;">
            Paste 1–5 URLs and see a Madison-style snapshot. This version uses demo scores for the assignment.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with hero_right:
    st.markdown(
        """
        <div class="card-soft">
          <b>How this relates to steffimanhalli.com</b><br><br>
          • Inspired by the AudioEye scan you ran<br>
          • Focus on WCAG-style flags + empathy<br>
          • Designed to sit inside your portfolio as an
            explorable <i>“assessment layer”</i> on top of your site
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("")

# ---------- INPUT PANEL ----------
input_col, info_col = st.columns([2, 1])

with input_col:
    st.markdown('<div class="section-title">Input URLs to review</div>', unsafe_allow_html=True)
    urls_text = st.text_area(
        "Paste one URL per line",
        placeholder="https://steffimanhalli.com/\nhttps://example.com/page-1",
        height=140,
    )
    run_button = st.button("Run demo analysis")

with info_col:
    st.markdown('<div class="section-title">What this demo simulates</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="card">
        • A quick, non-clinical read on:<br>
        &nbsp;&nbsp;– Plain-language clarity<br>
        &nbsp;&nbsp;– Tone & empathy<br>
        &nbsp;&nbsp;– Simple accessibility health check<br><br>
        • The real version would:<br>
        &nbsp;&nbsp;– Call a Madison/n8n workflow<br>
        &nbsp;&nbsp;– Use LLM prompts tuned for health comms<br>
        &nbsp;&nbsp;– Log results into a Google Sheet for trends
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.info(
        "For Assignment 9, the scores below are mocked so the interface can be evaluated "
        "without exposing any private API keys."
    )

# ---------- DUMMY ANALYSIS ----------
def analyze_url_dummy(url: str) -> dict:
    """
    Demo-only analysis so the UI can be graded.
    This is where you’d plug in your actual Madison pipeline later.
    """
    return {
        "url": url,
        "empathy_score": "Medium",
        "clarity_score": "High",
        "wcag_status": "Not compliant (demo)",
        "visual_schema": "Content-heavy layout",
        "summary": (
            "Demo summary: content is generally clear but may be hard for some users "
            "with low literacy or visual stress. Headings and spacing can do more work."
        ),
        "rewrite_suggestion": (
            "Shorten dense paragraphs, replace jargon with everyday words, and add "
            "lead-in headings like “In simple terms” or “What you should do next”."
        ),
        "low_literacy_note": (
            "Several long sentences; consider aiming for ~8–10 words per line and "
            "simpler phrasing."
        ),
        "tone_safety_note": (
            "Tone is informational and neutral. You could add a short validating phrase "
            "to sound more human (“It’s okay if this feels confusing at first…”)."
        ),
        "hierarchy_note": (
            "Main call-to-action is visible, but secondary content could be grouped into "
            "scannable sections with subheadings and bullets."
        ),
        "visual_stress_note": (
            "Minimal whitespace around body text. Slightly larger line-height and "
            "extra spacing between sections would help."
        ),
        "recommendations": [
            "Introduce a clear first heading that states the page’s purpose in plain language.",
            "Break large text blocks into smaller paragraphs and bullet lists.",
            "Ensure links describe their destination (avoid “click here”).",
            "Add descriptive titles or aria-labels for icons and meaningful SVGs.",
        ],
    }

# ---------- RUN ANALYSIS ----------
results = []
df = None

if run_button:
    urls = [u.strip() for u in urls_text.splitlines() if u.strip()]
    if not urls:
        st.warning("Please paste at least one URL to analyze.")
    else:
        for url in urls:
            results.append(analyze_url_dummy(url))

        df_rows = []
        for item in results:
            df_rows.append(
                {
                    "URL": item["url"],
                    "Empathy": item["empathy_score"],
                    "Clarity": item["clarity_score"],
                    "WCAG status": item["wcag_status"],
                    "Layout": item["visual_schema"],
                }
            )
        df = pd.DataFrame(df_rows)

# ---------- RESULTS LAYER ----------
if results and df is not None:
    st.markdown("<div class='divider-label'><span class='section-title'>Snapshot</span><hr></div>",
                unsafe_allow_html=True)

    total_urls = len(df)
    high_clarity = (df["Clarity"] == "High").sum()
    good_empathy = df["Empathy"].isin(["Medium", "High"]).sum()
    # Any page that contains "Not compliant" is treated as at-risk in this demo
    at_risk = df["WCAG status"].str.contains("Not compliant", case=False).sum()

    st.markdown(
        f"""
        <div class="card card-border">
          <span class="pill pill-demo">Demo data • Madison concept</span><br><br>
          <div style="display:flex; justify-content:space-between; align-items:flex-end; gap:1rem; flex-wrap:wrap;">
            <div>
              <div style="font-size:1.05rem; font-weight:600; color:var(--purple-700);">
                Accessibility & empathy snapshot for {total_urls} page(s)
              </div>
              <div style="font-size:0.85rem; color:#4B5563; margin-top:0.2rem;">
                Treat this as a design conversation starter, not a legal compliance report.
              </div>
            </div>
            <div>
              <span class="pill pill-risk">{at_risk} page(s) flagged as “Not compliant (demo)”</span>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # KPI row
    st.markdown(
        """
        <div class="kpi-grid">
          <div class="kpi">
            <div class="kpi-label">URLs analyzed</div>
            <div class="kpi-value">{total}</div>
            <div class="kpi-meta">Per run</div>
          </div>
          <div class="kpi">
            <div class="kpi-label">High clarity pages</div>
            <div class="kpi-value">{clarity}/{total}</div>
            <div class="kpi-meta">“High” label in demo scoring</div>
          </div>
          <div class="kpi">
            <div class="kpi-label">Supportive tone (Med/High)</div>
            <div class="kpi-value">{empathy}/{total}</div>
            <div class="kpi-meta">Pages unlikely to feel harsh</div>
          </div>
          <div class="kpi">
            <div class="kpi-label">WCAG risk (demo)</div>
            <div class="kpi-value">{risk}</div>
            <div class="kpi-meta">Pages marked “Not compliant (demo)”</div>
          </div>
        </div>
        """.format(
            total=total_urls,
            clarity=high_clarity,
            empathy=good_empathy,
            risk=at_risk,
        ),
        unsafe_allow_html=True,
    )

    # Table + bar chart
    st.markdown("<div class='divider-label'><span class='section-title'>Table & trend view</span><hr></div>",
                unsafe_allow_html=True)

    with st.expander("View page-by-page table"):
        st.dataframe(df, use_container_width=True)

    score_map = {"Low": 1, "Medium": 2, "High": 3}
    chart_df = df.copy()
    chart_df["Clarity score"] = chart_df["Clarity"].map(score_map)
    chart_df["Empathy score"] = chart_df["Empathy"].map(score_map)
    chart_df = chart_df.set_index("URL")[["Clarity score", "Empathy score"]]

    st.bar_chart(chart_df, use_container_width=True)

    # ---------- DEEP DIVE ----------
    st.markdown("<div class='divider-label'><span class='section-title'>Deep dive</span><hr></div>",
                unsafe_allow_html=True)

    selected_url = st.selectbox(
        "Choose a page to see detailed notes",
        df["URL"].tolist(),
    )
    selected_item = next(item for item in results if item["url"] == selected_url)

    colA, colB = st.columns([1.2, 1])

    with colA:
        st.markdown(
            f"""
            <div class="card">
              <div style="font-size:0.8rem; text-transform:uppercase; letter-spacing:0.14em; color:#6B7280;">
                Page overview
              </div>
              <div style="font-size:0.95rem; font-weight:600; color:var(--purple-700); margin-top:0.15rem;">
                {selected_item["url"]}
              </div>
              <div style="margin-top:0.6rem; font-size:0.9rem;">
                <b>Empathy:</b> {selected_item["empathy_score"]}<br>
                <b>Clarity:</b> {selected_item["clarity_score"]}<br>
                <b>WCAG status (demo):</b> {selected_item["wcag_status"]}<br>
                <b>Layout pattern:</b> {selected_item["visual_schema"]}
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class="card-soft">
              <b>Quick narrative summary</b><br><br>
              {selected_item["summary"]}
            </div>
            """,
            unsafe_allow_html=True,
        )

    with colB:
        st.markdown(
            f"""
            <div class="card">
              <div class="section-title" style="margin-bottom:0.4rem;">AI rewrite direction</div>
              <div style="font-size:0.9rem;">
                {selected_item["rewrite_suggestion"]}
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        f"""
        <div class="card">
          <div class="section-title" style="margin-bottom:0.6rem;">Healthcare-inspired UX lenses</div>
          <ul class="reco-list" style="font-size:0.9rem;">
            <li><b>Low-literacy friendliness:</b> {selected_item["low_literacy_note"]}</li>
            <li><b>Tone safety:</b> {selected_item["tone_safety_note"]}</li>
            <li><b>Information hierarchy:</b> {selected_item["hierarchy_note"]}</li>
            <li><b>Visual stress:</b> {selected_item["visual_stress_note"]}</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("#### Recommended next moves")
    for r in selected_item.get("recommendations", []):
        st.markdown(f"- {r}")

# ---------- FOOTER ----------
st.markdown("---")
st.markdown(
    "Back to portfolio → [steffimanhalli.com](https://steffimanhalli.com)  ·  "
    "This demo was built for INFO 7375 · Madison / Branding & AI."
)
