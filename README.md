# Pentrust.md
# PenTrust — Healthcare Content Clarity Analyzer

PenTrust is a **presentation-friendly, AI-assisted concept tool** for healthcare UX and content teams. It simulates how a content audit product could surface **clarity, next-step, trust, and accessibility-aware writing risks** across patient-facing pages.

This version is designed for **class demos and portfolio storytelling**. It does not crawl or medically validate live content; instead, it generates realistic, structured signals based on sample logic so you can demonstrate **problem → insight → fix** clearly.

---

## What PenTrust helps you show

PenTrust is built to support a simple narrative:

1. **You paste multiple pages/labels**
2. **Dashboard surfaces 2–3 high-impact risks**
3. **Deep Analysis explains**
   - what the issue means
   - why it matters in healthcare
   - how to rewrite it
4. **A detailed audit table** provides a clean artifact for screenshots and grading

---

## Core UX signals (demo logic)

PenTrust simulates scoring and warnings in four areas:

- **Clarity**
  - Dense instructions
  - Overloaded paragraphs
  - Ambiguity in critical moments
- **Next-step**
  - Missing “what happens next?”
  - Weak or competing CTAs
  - Lack of action-oriented microcopy
- **Trust**
  - Vague claims
  - Missing reassurance language
  - Lack of transparent instructions
- **Accessibility-aware writing**
  - High reading level
  - Jargon-heavy copy
  - Inconsistent headings/structure

> Note: This tool is **not a WCAG scanner**. The “accessibility-aware” score focuses on **language-level accessibility** (readability, clarity, structure).

---

## Features

### Dashboard (problems, fast)
- Snapshot cards aligned to PenTrust’s core signals  
  Examples:
  - **Clarity risk signals found**
  - **Next-step gaps flagged**
  - **Trust friction signals**
  - **Readability/structure warnings**
- **Clarity score trend** (demo chart)
- **Key problems detected on this page** (brief)

### Deep Analysis (solutions, detailed)
For the selected page:
- Plain-language explanation of each issue
- Suggested fixes
- Before/After rewrite examples
- Copy patterns healthcare teams can reuse

### Detailed audit table
A single table summarizing:
- Clarity score  
- Next-step score  
- Trust score  
- Accessibility-aware score  
- Top risk signals  
- Risk level

---

## Why “Next-step gaps flagged” matters

This is a **specific UX writing risk** where users are left unsure what to do after an action.

Examples of next-step gaps:
- Confirmation screens that say *“Request received.”* but do not tell users what happens next
- Successful form submissions with **no primary CTA**
- Instructions missing a simple step-by-step sequence
- Multiple actions shown with no recommendation

In healthcare, this can lead to:
- repeat calls
- abandoned appointments
- missed documentation steps
- lower confidence in the system

---

## Tech stack

- **Python**
- **Streamlit**
- Optional:
  - pandas
  - numpy

---

## Project structure (suggested)

