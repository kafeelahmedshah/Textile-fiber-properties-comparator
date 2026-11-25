import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Textile Fiber Properties Comparator",
    page_icon="🧵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Educational reference values. Actual properties vary with grade, processing,
# test method, conditioning, and fiber construction.
FIBERS = {
    "Cotton": {
        "type": "Natural — Cellulosic",
        "origin": "Cotton plant seed hair",
        "moisture_regain": 8.5,
        "tenacity_low": 27,
        "tenacity_high": 44,
        "breathability": 5,
        "absorbency": "High",
        "heat_behavior": "Good heat resistance; scorches at high temperature",
        "main_advantages": "Comfortable, absorbent, soft, and easy to dye",
        "limitations": "Can crease and shrink; may dry slowly",
        "common_uses": "Shirts, T-shirts, towels, bedsheets, denim"
    },
    "Polyester": {
        "type": "Synthetic",
        "origin": "Petrochemical-based polymer",
        "moisture_regain": 0.4,
        "tenacity_low": 35,
        "tenacity_high": 75,
        "breathability": 2,
        "absorbency": "Very low",
        "heat_behavior": "Thermoplastic; softens and melts at high temperature",
        "main_advantages": "Strong, durable, wrinkle-resistant, quick-drying",
        "limitations": "Low moisture absorption; may retain oily stains",
        "common_uses": "Sportswear, shirts, curtains, industrial fabrics"
    },
    "Wool": {
        "type": "Natural — Protein",
        "origin": "Animal fleece, commonly sheep",
        "moisture_regain": 16.0,
        "tenacity_low": 10,
        "tenacity_high": 16,
        "breathability": 4,
        "absorbency": "High",
        "heat_behavior": "Good insulation; can be damaged by excessive heat",
        "main_advantages": "Warm, resilient, elastic, and moisture-absorbing",
        "limitations": "Can felt or shrink; requires careful washing",
        "common_uses": "Suits, sweaters, blankets, winter clothing"
    },
    "Silk": {
        "type": "Natural — Protein",
        "origin": "Silkworm filament",
        "moisture_regain": 11.0,
        "tenacity_low": 30,
        "tenacity_high": 50,
        "breathability": 4,
        "absorbency": "Good",
        "heat_behavior": "Sensitive to strong heat and prolonged sunlight",
        "main_advantages": "Smooth, lustrous, lightweight, and comfortable",
        "limitations": "Can be costly and sensitive to sunlight and harsh chemicals",
        "common_uses": "Scarves, dresses, ties, luxury garments"
    },
    "Nylon": {
        "type": "Synthetic — Polyamide",
        "origin": "Synthetic polyamide polymer",
        "moisture_regain": 4.5,
        "tenacity_low": 40,
        "tenacity_high": 80,
        "breathability": 3,
        "absorbency": "Low to moderate",
        "heat_behavior": "Thermoplastic; softens and melts at high temperature",
        "main_advantages": "High strength, abrasion resistance, and elasticity",
        "limitations": "Can build static; heat sensitivity depends on grade",
        "common_uses": "Hosiery, sportswear, ropes, parachutes, bags"
    }
}

st.markdown("""
<style>
.hero {
    padding: 1.4rem 1.6rem;
    border-radius: 16px;
    background: linear-gradient(115deg, #153b5b, #147d83);
    color: white;
    margin-bottom: 1.2rem;
}
.hero h1 { color: white; margin: 0; font-size: 2rem; }
.hero p { color: #e7f5f5; margin: .45rem 0 0 0; }
.note { padding: 12px 14px; border-radius: 10px; border: 1px solid rgba(128,128,128,.3); }
</style>
<div class="hero">
<h1>🧵 Textile Fiber Properties Comparator</h1>
<p>Compare cotton, polyester, wool, silk, and nylon using clear textile reference data and interactive charts.</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.title("🧵 Fiber Comparator")
page = st.sidebar.radio(
    "Navigation",
    ["Fiber Comparison", "Fiber Details", "About & Data Notes"]
)
st.sidebar.divider()
st.sidebar.markdown("**Project Details**")
st.sidebar.write("Roll No: 25TE009")
st.sidebar.write("Department: Textile Engineering")

if page == "Fiber Comparison":
    st.subheader("Select Fibers to Compare")
    selected = st.multiselect(
        "Choose two or more fibers",
        options=list(FIBERS.keys()),
        default=["Cotton", "Polyester", "Wool"],
        help="Select the fibers you want to compare."
    )

    if len(selected) < 2:
        st.info("Please select at least two fibers to display a comparison.")
    else:
        records = []
        for name in selected:
            f = FIBERS[name]
            records.append({
                "Fiber": name,
                "Fiber Type": f["type"],
                "Moisture Regain (%)": f["moisture_regain"],
                "Tenacity Range (cN/tex)": f'{f["tenacity_low"]}–{f["tenacity_high"]}',
                "Breathability (guide score / 5)": f["breathability"],
                "Absorbency": f["absorbency"]
            })

        df = pd.DataFrame(records)
        st.subheader("Side-by-Side Comparison")
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Moisture Regain (%)": st.column_config.NumberColumn(format="%.1f%%"),
                "Breathability (guide score / 5)": st.column_config.ProgressColumn(
                    min_value=0, max_value=5, format="%d / 5"
                )
            }
        )

        st.subheader("Interactive Property Charts")
        chart_tab1, chart_tab2, chart_tab3 = st.tabs(
            ["Moisture Regain", "Tenacity / Strength", "Breathability"]
        )

        moisture_df = pd.DataFrame({
            "Fiber": selected,
            "Moisture Regain (%)": [FIBERS[x]["moisture_regain"] for x in selected]
        }).set_index("Fiber")
        with chart_tab1:
            st.caption("Typical moisture regain reference values under standard conditioning; actual values vary.")
            st.bar_chart(moisture_df)

        strength_df = pd.DataFrame({
            "Minimum Tenacity (cN/tex)": [FIBERS[x]["tenacity_low"] for x in selected],
            "Maximum Tenacity (cN/tex)": [FIBERS[x]["tenacity_high"] for x in selected]
        }, index=selected)
        with chart_tab2:
            st.caption("Approximate textbook ranges. Tenacity is strength per unit linear density; test results depend on fiber grade and method.")
            st.bar_chart(strength_df)

        breath_df = pd.DataFrame({
            "Breathability guide score (out of 5)": [FIBERS[x]["breathability"] for x in selected]
        }, index=selected)
        with chart_tab3:
            st.caption("Qualitative educational guide score, not a standardized laboratory measurement.")
            st.bar_chart(breath_df)

        st.subheader("Quick Comparison Insights")
        highest_moisture = max(selected, key=lambda x: FIBERS[x]["moisture_regain"])
        lowest_moisture = min(selected, key=lambda x: FIBERS[x]["moisture_regain"])
        highest_strength = max(selected, key=lambda x: FIBERS[x]["tenacity_high"])
        st.markdown(f"- Highest moisture regain among selected fibers: **{highest_moisture}**.")
        st.markdown(f"- Lowest moisture regain among selected fibers: **{lowest_moisture}**.")
        st.markdown(f"- Highest upper-end tenacity value among selected fibers: **{highest_strength}**.")

        csv = df.to_csv(index=False).encode("utf-8-sig")
        st.download_button(
            "⬇️ Download Comparison Table (CSV)",
            data=csv,
            file_name="textile_fiber_comparison.csv",
            mime="text/csv",
            use_container_width=True
        )

elif page == "Fiber Details":
    st.subheader("Explore Individual Fiber Properties")
    fiber_name = st.selectbox("Select a fiber", list(FIBERS.keys()))
    f = FIBERS[fiber_name]

    st.markdown(f"### {fiber_name}")
    st.caption(f["type"])
    a, b, c = st.columns(3)
    a.metric("Moisture Regain", f'{f["moisture_regain"]:.1f}%')
    b.metric("Tenacity Range", f'{f["tenacity_low"]}–{f["tenacity_high"]} cN/tex')
    c.metric("Breathability Guide", f'{f["breathability"]}/5')

    st.markdown(f"**Origin:** {f['origin']}")
    st.markdown(f"**Absorbency:** {f['absorbency']}")
    st.markdown(f"**Heat behavior:** {f['heat_behavior']}")
    left, right = st.columns(2)
    with left:
        st.markdown("#### Main advantages")
        st.success(f["main_advantages"])
    with right:
        st.markdown("#### Limitations")
        st.warning(f["limitations"])
    st.markdown("#### Common applications")
    st.info(f["common_uses"])

    st.caption("Values are indicative educational references, not guaranteed specifications for every commercial fiber.")

else:
    st.subheader("About This Project")
    st.write("**Application:** Textile Fiber Properties Comparator")
    st.write("**Roll No:** 25TE009")
    st.write("**Department:** Textile Engineering")
    st.write("**Framework:** Python + Streamlit")
    st.markdown("""
    **Project objective**

    To help textile students compare common natural and synthetic fibers using standard educational properties, including moisture regain, strength (tenacity), and breathability.

    **Fibers included**
    - Cotton
    - Polyester
    - Wool
    - Silk
    - Nylon

    **Application features**
    - Multi-fiber selection
    - Side-by-side comparison table
    - Interactive charts for moisture regain, tenacity, and breathability
    - Individual fiber information
    - Advantages, limitations, and common applications
    - Downloadable comparison table
    """)
    st.markdown("#### Data notes")
    st.markdown("""
    - Moisture regain and tenacity figures are approximate educational reference values. They vary with fiber grade, conditioning, processing, and test method.
    - Breathability is affected by yarn, fabric construction, thickness, finishing, and test conditions. The 1–5 score in this app is a qualitative teaching aid, not a standardized measured value.
    - Use laboratory test data or a recognized textile reference when exact specifications are required.
    """)
    st.warning("Responsible AI / limitations note: This app uses a small fixed reference dataset and simplified comparisons. It does not perform laboratory testing, predict every fabric's performance, or replace standards-based testing.")

st.divider()
st.caption("Textile Fiber Properties Comparator | Roll No. 25TE009 | Textile Engineering")
