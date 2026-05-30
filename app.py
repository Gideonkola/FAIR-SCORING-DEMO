import streamlit as st

st.set_page_config(page_title="FAIR Scoring Tool", layout="wide")

st.title("📊 FAIR Data Scoring Demo")

# ---- LAYOUT: 2 COLUMNS ----
col1, col2 = st.columns(2)

# ---- LEFT COLUMN (INPUTS) ----
with col1:
    st.header("Findable (F)")
    F1 = st.checkbox("F1: The KP is retrievable through its handle, metadata considered: Handle ")
    F2 = st.checkbox("F2:  The KP is described by rich metadata, metadata considered: Title, Author(s), Description/abstract, Date")
    F3 = st.checkbox("F3: At least one author is linked through their ORCID, metadata considered: ORCID")

    st.header("Accessible (A)")
    A1 = st.checkbox("A1: Metadata is retrievable through the handle, Metadata considered: Handle")

    st.header("Interoperable (I)")
    I1 = st.checkbox("I1: Metadata contains AGROVOC Keywords, Keywords automatically matched with the AGROVOC Thesaurus ")
    I2 = st.checkbox("I2: Metadata includes qualified references to other (meta)data, Reference to other KPs ")

    st.header("Reusable (R)")
    R1 = st.checkbox("R1: Accessibility")
    R2 = st.checkbox("R2: License")

# ---- SCORING FUNCTION ----
def score_section(values):
    return (sum(values) / len(values)) * 100 if len(values) > 0 else 0

# ---- CALCULATE ----
findable_score = score_section([F1, F2, F3])
accessible_score = score_section([A1])
interoperable_score = score_section([I1, I2])
reusable_score = 100 if (R1 and R2) else 0

total_score = (
    findable_score +
    accessible_score +
    interoperable_score +
    reusable_score
) / 4

# ---- RIGHT COLUMN (RESULTS) ----
with col2:
    st.subheader("Results")

    st.metric("Findable", f"{findable_score:.1f}%")
    st.metric("Accessible", f"{accessible_score:.1f}%")
    st.metric("Interoperable", f"{interoperable_score:.1f}%")
    st.metric("Reusable", f"{reusable_score:.1f}%")

    st.divider()

    st.metric("Total FAIR Score", f"{total_score:.2f}%")

    # ---- GRADE ----
    if total_score >= 90:
        grade = "Excellent"
    elif total_score >= 75:
        grade = "Good"
    elif total_score >= 60:
        grade = "Moderate"
    else:
        grade = "Fair"

    st.success(f"🏆 Rating: {grade}")