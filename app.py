

import streamlit as st

st.set_page_config(page_title="FAIR Scoring Tool", layout="centered")

st.title("📊 FAIR Data Scoring Demo")
st.write("This tool demonstrates how FAIR scoring works based on the rubric.")

# ---- INPUTS ----
st.header("Findable (F)")
F1 = st.checkbox("F1: The KP is retrievable through its handle, metadata considered: Handle ")
F2 = st.checkbox("F2:  The KP is described by rich metadata, metadata considered: Title, Author(s), Description/abstract, Date")
F3 = st.checkbox("F3: At least one author is linked through their ORCID, metadata considered: ORCID")


st.header("Accessible (A)")
A1 = st.checkbox("A1: Metadata is retrievable through the handle, Metadata considered: Handle")

st.header("Interoperable (I)")
I1 = st.checkbox("I1: Metadata contains AGROVOC Keyworsd, Keywords automatically matched with the AGROVOC Thesaurus ")
I2 = st.checkbox("I2: Metadata includes qualified references to other (meta)data, Reference to other KPs ")

st.header("Reusable (R)")
R1 = st.checkbox("R1: Accessibility")
R2 = st.checkbox("R2: License")

# ---- SCORING FUNCTION ----
def score_section(values):
    total_items = len(values)
    score = sum(values)
    return (score / total_items) * 100 if total_items > 0 else 0

# ---- CALCULATE SCORES ----
# ---- CALCULATE SCORES ----
findable_score = score_section([F1, F2, F3])
accessible_score = score_section([A1])
interoperable_score = score_section([I1, I2])

# ---- REUSABLE SCORE (custom rule) ----
if R1 and R2:
    reusable_score = 100
else:
    reusable_score = 0

# ---- TOTAL ----
total_score = (
    findable_score
    + accessible_score
    + interoperable_score
    + reusable_score
)

# ✅ FIXED: define total score properly
total_score = (
    findable_score
    + accessible_score
    + interoperable_score
    + reusable_score
)

# ---- OUTPUT ----
st.divider()

st.subheader("Results")
st.write(f"Findable Score: {findable_score:.1f}%")
st.write(f"Accessible Score: {accessible_score:.1f}%")
st.write(f"Interoperable Score: {interoperable_score:.1f}%")
st.write(f"Reusable Score: {reusable_score:.1f}%")

st.success(f"✅ Total FAIR Score: {total_score:.1f}")

# ---- SIMPLE INTERPRETATION ----
if total_score >= 300:
    st.info("Excellent FAIR compliance")
elif total_score >= 200:
    st.info("Good FAIR compliance")
elif total_score >= 100:
    st.info("Moderate FAIR compliance")
else:
    st.warning("Low FAIR compliance")
