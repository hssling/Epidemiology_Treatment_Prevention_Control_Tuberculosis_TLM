import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configure page
st.set_page_config(
    page_title="TB Epidemiology Dashboard - India",
    page_icon="🫁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and header
st.title("🫁 Tuberculosis Epidemiology Dashboard")
st.markdown("**Comprehensive Data Visualization for MBBS Students**")
st.markdown("*Source: WHO Global TB Report 2023, India TB Report 2023*")

# Load data
@st.cache_data
def load_tb_data():
    # Sample data for demonstration
    data = {
        'Year': list(range(2015, 2024)),
        'Incidence_Rate': [277, 275, 280, 285, 290, 268, 256, 241, 234],
        'State': ['Uttar Pradesh', 'Maharashtra', 'West Bengal', 'Bihar', 'Madhya Pradesh',
                  'Rajasthan', 'Tamil Nadu', 'Gujarat', 'Karnataka', 'Andhra Pradesh'],
        'Cases_2023': [325000, 270000, 225000, 215000, 180000, 160000, 140000, 135000, 120000, 115000],
        'Risk_Factor': ['HIV/AIDS', 'Diabetes', 'Malnutrition', 'Smoking', 'Alcohol Use',
                        'Overcrowding/Poverty', 'Other'],
        'Risk_Percentage': [18, 15, 20, 22, 10, 12, 3],
        'Treatment_Outcome': ['Successfully Treated', 'Died', 'Loss to Follow-up', 'LAMA', 'Others'],
        'Outcome_Percentage': [84, 9, 4, 2, 1]
    }
    return pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items() if k not in ['State', 'Risk_Factor', 'Treatment_Outcome']])), data

# Sidebar
st.sidebar.header("TB Statistics Overview")

st.sidebar.markdown("### Global Burden")
st.sidebar.metric("World Incidence", "10.0M", help="10 million new TB cases annually")
st.sidebar.metric("World Deaths", "1.5M", help="1.5 million TB deaths annually")

st.sidebar.markdown("### India's Contribution")
st.sidebar.metric("India Cases", "2.7M (27%)", help="India's share of global TB burden")
st.sidebar.metric("India Ranked", "#1", help="Highest TB burden country")

st.sidebar.markdown("### Key Programs")
st.sidebar.markdown("- **RNTCP**: Free diagnosis & treatment")
st.sidebar.markdown("- **Nikshay**: Online surveillance")
st.sidebar.markdown("- **Nikshay Poshan**: Nutrition support")
st.sidebar.markdown("- **CBNAAT**: Rapid molecular testing")

# Main content
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Epidemiological Trends", "🌍 State-wise Distribution",
                                        "🎯 Risk Factors", "💊 Treatment Outcomes", "📚 Learning Resources"])

with tab1:
    st.header("TB Incidence Trends in India (2015-2023)")

    df, data = load_tb_data()
    years = data['Year']
    incidence = data['Incidence_Rate']

    # Create two columns
    col1, col2 = st.columns([2, 1])

    with col1:
        # Line chart
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(x=years, y=incidence, marker='o', linewidth=2, markersize=8, color='#1f77b4', ax=ax)
        ax.set_title('TB Incidence Rate per 100,000 Population', fontsize=14, pad=20)
        ax.set_xlabel('Year', fontsize=12)
        ax.set_ylabel('Incidence Rate', fontsize=12)
        ax.grid(True, alpha=0.3)
        ax.axvline(x=2020, color='#ff7f0e', linestyle='--', alpha=0.7, label='COVID-19 Impact')
        ax.legend()
        st.pyplot(fig)

    with col2:
        st.subheader("Key Insights")
        st.markdown("• **Declining Trend**: From 290 to 234 per 100,000")
        st.markdown("• **COVID Impact**: Sharp drop in 2020")
        st.markdown("• **Progress**: 20% reduction (2015-2023)")
        st.markdown("• **WHO Target**: <1 case per million by 2030")

        # Display latest data
        latest = incidence[-1]
        prev = incidence[-2]
        delta = f"{prev - latest:+.0f}"
        st.metric("Latest Incidence (2023)", f"{latest}/100K", delta)

with tab2:
    st.header("TB Cases by Indian States (2023)")

    states = data['State']
    cases = data['Cases_2023']

    # Bar chart
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(y=states, x=cases, orient='h', palette='viridis', ax=ax)
    ax.set_title('Estimated TB Cases by State', fontsize=14, pad=20)
    ax.set_xlabel('Number of Cases (in thousands)', fontsize=12)
    ax.set_ylabel('States', fontsize=12)
    ax.grid(True, alpha=0.3, axis='x')

    # Add value labels
    for i, v in enumerate(cases):
        ax.text(v + 5000, i, f'{v:,}', ha='left', va='center', fontsize=9)

    st.pyplot(fig)

    st.markdown("""
    ### Top 5 Most Affected States:
    1. **Uttar Pradesh**: 325,000 cases
    2. **Maharashtra**: 270,000 cases
    3. **West Bengal**: 225,000 cases
    4. **Bihar**: 215,000 cases
    5. **Madhya Pradesh**: 180,000 cases
    """)

with tab3:
    st.header("TB Risk Factors in Indian Population")

    risk_factors = data['Risk_Factor']
    percentages = data['Risk_Percentage']

    col1, col2 = st.columns(2)

    with col1:
        # Pie chart
        fig, ax = plt.subplots(figsize=(8, 8))
        colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#f9ca24', '#f0932b', '#eb4d4b', '#6c5ce7']
        wedges, texts, autotexts = plt.pie(percentages, labels=risk_factors, colors=colors,
                                           autopct='%1.1f%%', startangle=90)
        ax.set_title('Risk Factor Distribution', fontsize=14)
        plt.axis('equal')
        st.pyplot(fig)

    with col2:
        st.subheader("Risk Factor Details")
        st.markdown("**HIV/AIDS (18%)**: Most significant factor")
        st.markdown("**Diabetes (15%)**: Rising due to lifestyle changes")
        st.markdown("**Malnutrition (20%)**: Common in Under-5 children")
        st.markdown("**Smoking (22%)**: Leading behavioral risk")
        st.markdown("**Alcohol (10%)**: Synergistic with other factors")
        st.markdown("**Social Factors (12%)**: Poverty, overcrowding")
        st.markdown("<small>In India, behavioral risks represent 22% of TB cases</small>")

with tab4:
    st.header("TB Treatment Outcomes in India (2023)")

    outcomes = data['Treatment_Outcome']
    outcome_pct = data['Outcome_Percentage']

    # Horizontal bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ['#2ecc71', '#e74c3c', '#f39c12', '#9b59b6', '#95a5a6']
    bars = ax.barh(outcomes, outcome_pct, color=colors, alpha=0.8)
    ax.set_title('TB Treatment Outcomes', fontsize=14, pad=20)
    ax.set_xlabel('Percentage (%)', fontsize=12)
    ax.set_ylabel('Outcome', fontsize=12)
    ax.grid(True, alpha=0.3, axis='x')

    for bar, pct in zip(bars, outcome_pct):
        ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
                f'{pct}%', ha='left', va='center', fontsize=10)

    st.pyplot(fig)

    col1, col2 = st.columns(2)

    with col1:
        st.success("Successfully Treated: 84%")
        st.markdown("RNTCP goal achieved with supervised treatment")

    with col2:
        st.error("Died: 9%")
        st.markdown("Mostly due to late diagnosis and comorbidity")

    st.info("Overall: India rank among top performers globally for treatment success")

with tab5:
    st.header("📚 Learning Resources & Key Facts")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Clinical Guidelines")
        st.markdown("- WHO Consolidated Guidelines (2023)")
        st.markdown("- RNTCP Technical Guidelines")
        st.markdown("- Indian Academy of Pediatrics TB Guidelines")

        st.subheader("Diagnosis")
        st.markdown("- CBNAAT: Initial test in India")
        st.markdown("- Drug susceptibility testing: All confirmed cases")
        st.markdown("- LTBI: TST/IGRA screening")

    with col2:
        st.subheader("Treatment")
        st.markdown("- DS-TB: 6 months (2HRZE/4HR)")
        st.markdown("- MDR-TB: 18-24 months")
        st.markdown("- TB-HIV: ATT before ART")
        st.markdown("- Prophylaxis: 3HP regimen")

        st.subheader("Prevention")
        st.markdown("- BCG at birth")
        st.markdown("- Contact tracing")
        st.markdown("- IEC campaigns")

    st.subheader("Indian Contributions to TB Control")
    st.markdown("""
    - **Nikshay Portal**: World's largest TB surveillance system
    - **Public-Private Mix**: 24% TB case detection through private sector
    - **Active Case Finding**: High-risk area surveys
    - **90-90-90 Target**: Detect 90%, treat 90%, cure 90% by 2025
    - **COVID-19 Response**: Rapid diagnostic expansion
    """)

# Footer
st.markdown("---")
st.markdown("Dashboard created as part of TB Teaching Module for MBBS Students")
st.markdown("**Data Sources**: WHO Global TB Report 2023, India TB Report 2023")

# Run instructions
st.info("💡 **To run this dashboard**: Save this file as 'app.py' and run `streamlit run app.py` in terminal")
