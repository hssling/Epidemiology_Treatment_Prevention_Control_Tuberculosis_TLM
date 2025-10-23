# TB Teaching Module: Epidemiology, Treatment, and Control of Tuberculosis

## Overview

This comprehensive teaching module has been created specifically for MBBS students to understand the epidemiology, treatment, and control of tuberculosis with strong focus on the Indian context. All materials are based on latest WHO and CDC guidelines (2023 data).

## Project Structure

```
TB_Module/
├── chapters/
│   ├── README.md                             # Chapters navigation guide
│   ├── chapter1_introduction_and_epidemiology.md
│   ├── chapter2_transmission_and_pathogenesis.md
│   ├── chapter3_risk_factors.md
│   ├── chapter4_clinical_manifestations.md
│   ├── chapter5_diagnosis.md
│   ├── chapter6_treatment.md
│   ├── chapter7_prevention_and_control.md
│   ├── chapter8_tb_in_special_populations.md
│   ├── chapter9_national_tb_elimination_program.md
│   └── chapter10_future_directions_and_research.md
├── presentations/
│   └── TB_Module_Presentation.pptx          # Interactive PowerPoint presentation (14 slides)
├── handouts/
│   └── student_handout.md                   # Updated master handbook with module overview
├── visualizations/
│   ├── charts/                              # Generated PNG charts (6 charts)
│   │   ├── tb_incidence_india_trend.png
│   │   ├── tb_cases_by_state_india.png
│   │   ├── india_global_tb_comparison.png
│   │   ├── tb_types_pie_india.png
│   │   ├── tb_risk_factors_india.png
│   │   └── tb_treatment_outcomes_india.png
│   ├── data/
│   │   └── tb_india_statistics.csv          # Raw data for charts
│   └── generate_charts.py                   # Python script to recreate charts
├── quizzes/
│   └── tb_quiz.json                         # MCQ quiz (25 questions, Indian context)
├── videos/
│   ├── video_script_episode1.txt            # Introduction video script
│   └── video_script_episode2.txt            # Diagnosis video script
├── dashboard/
│   └── app.py                               # Interactive Streamlit dashboard
├── scripts/
│   └── generate_presentation.py             # Python script to recreate PPTX
├── docs/
│   └── README.md                            # This documentation file
└── requirements.txt                         # Python dependencies
```

## Module Objectives

By the end of this module, students will be able to:

1. **Epidemiology**: Describe global and Indian TB burden, understand trends and distribution
2. **Pathogenesis**: Explain transmission, infection progression, and risk factors
3. **Clinical Presentation**: Identify signs, symptoms, and clinical forms of TB
4. **Diagnosis**: Outline diagnostic approaches and interpret test results
5. **Treatment**: Discuss drug regimens for DS-TB and DR-TB, manage complications
6. **Control & Prevention**: Understand national programs, preventive measures, and strategies

## Key Topics Covered

### Chapter 1: Introduction to Tuberculosis
- Global burden (10M cases, 1.5M deaths)
- India's contribution (27% of global cases)
- Historical context and economic impact

### Chapter 2: Epidemiology
- Disease distribution by region
- Age, gender, and socioeconomic patterns
- Seasonal variations and hotspots
- Comparison with COVID-19 impact

### Chapter 3: Transmission and Pathogenesis
- Droplet nuclei mechanism
- Primary infection and latency
- Risk of progression to disease
- Bacterial factors and host immunity

### Chapter 4: Risk Factors (Indian Context)
- HIV/AIDS co-infection (18% of cases)
- Diabetes mellitus
- Malnutrition and poverty
- Tobacco and alcohol use
- Occupational and social determinants

### Chapter 5: Clinical Manifestations
- Pulmonary TB symptoms and signs
- Extrapulmonary TB forms
- Complications and special presentations
- Pediatric and HIV-associated TB

### Chapter 6: Diagnosis
- Clinical algorithms and suspicion
- Laboratory tests (smear, CBNAAT, culture)
- Imaging (X-ray, CT, PET)
- Interpretation and follow-up

### Chapter 7: Treatment
- Principles of antitubercular therapy
- Drug-susceptible TB regimen (2HRZE/4HR)
- Multidrug-resistant TB (18-24 months)
- Extensively drug-resistant TB
- Side effects and monitoring

### Chapter 8: Special Situations
- TB-HIV co-infection
- Pregnancy and lactation
- Childhood TB
- Diabetes and TB
- COVID-19 and TB interaction

### Chapter 9: Prevention and Control
- BCG vaccination
- Latent TB preventive treatment
- Infection control in healthcare
- Contact tracing and screening
- National TB elimination program

### Chapter 10: India's TB Control Efforts
- Revised National TB Control Programme (RNTCP)
- Nikshay portal and digital surveillance
- Private sector engagement
- Nutritional support (Nikshay Poshan)
- Way forward to elimination

## Learning Materials

### 1. Interactive Presentation
- **File**: `presentations/TB_Module_Presentation.pptx`
- 14 slides covering all major topics
- Suitable for classroom teaching
- Created using Python-pptx library

### 2. Student Handouts
- **File**: `handouts/student_handout.md`
- Comprehensive study material
- Convert to PDF using Markdown processors
- Includes notes sections for annotations
- Detailed Indian statistics and programs

### 3. Visualizations
- **Charts**: 6 high-resolution PNG files
- **Data**: CSV file with all statistics
- **Script**: Python file to regenerate charts
- Topics: Trends, state-wise distribution, risk factors, outcomes

**Charts Include:**
- TB incidence trend in India (2015-2023)
- Top 10 states by TB cases
- India vs global TB burden comparison
- Risk factors percentages
- Case types distribution
- Treatment outcomes

### 4. Assessment Quiz
- **File**: `quizzes/tb_quiz.json`
- 25 multiple-choice questions
- Indian context throughout
- Passing score: 70%
- Time limit: 30 minutes
- JSON format for easy integration

### 5. Video Scripts
- **Episode 1**: Introduction and epidemiology
- **Episode 2**: Diagnosis and clinical presentation
- Suitable for video content creation
- Narrator cues and scene descriptions

### 6. Interactive Dashboard
- **File**: `dashboard/app.py`
- **Run**: `streamlit run dashboard/app.py`
- Web-based application with tabs:
  - Epidemiological trends with charts
  - State-wise case distribution
  - Risk factors analysis
  - Treatment outcomes
  - Learning resources
- Responsive design, mobile-friendly

## Technical Requirements

### System Dependencies
- Python 3.8+
- pip package manager
- Web browser for Streamlit dashboard

### Python Libraries
Install all dependencies:
```bash
pip install -r requirements.txt
```

### Key Libraries Used
- **python-pptx**: PowerPoint file generation
- **matplotlib/seaborn**: Data visualization charts
- **streamlit**: Interactive web dashboard
- **pandas**: Data manipulation

## How to Use the Module

### For Faculty
1. Start with the PowerPoint presentation for overview
2. Use handouts as base for classroom discussion
3. Demonstrate the interactive dashboard
4. Assign quiz for assessment

### For Students
1. Read the student handouts thoroughly
2. Explore visualizations and data trends
3. Run the dashboard for interactive learning
4. Take the assessment quiz

### Content Updates
- All scripts and data use 2023 WHO and Indian TB report statistics
- Update epidemiological data annually
- Modify content based on new guidelines

## Sources and References

### Primary Sources
1. **WHO Global Tuberculosis Report 2023**: Main epidemiological data
2. **India TB Report 2023**: National program statistics
3. **CDC Tuberculosis Guidelines**: Technical updates
4. **RNTCP Technical Guidelines**: Treatment protocols

### Technical References
1. Park K. *Textbook of Preventive and Social Medicine* (2023)
2. Prasad R. *Textbook of Medicine* (2023)
3. Harrison's *Principles of Internal Medicine* (2023)

### Online Resources
- WHO: https://www.who.int/health-topics/tuberculosis
- CDC: https://www.cdc.gov/tuberculosis/
- Nikshay Portal: https://nikshay.gov.in/
- RNTCP: https://tbcindia.gov.in/

## Module Metrics

### File Statistics
- **Total Files**: 15
- **Code Files**: 4 (Python scripts)
- **Data Files**: 1 (CSV data)
- **Content Files**: 10 (PPTX, MD, JSON, TXT)
- **Total Size**: ~5 MB

### Content Volume
- **Presentation Slides**: 14
- **Handout Pages**: 12
- **Quiz Questions**: 25
- **Video Scripts**: 2 episodes
- **Charts**: 6 PNG files
- **Dashboard Tabs**: 5

### Educational Coverage
- **Clinical Learning**: Diagnosis and treatment protocols
- **Epidemiological Understanding**: Global and local patterns
- **Public Health Concepts**: Control programs and prevention
- **Data Analysis Skills**: Visual interpretation of statistics
- **Indian Context**: Specific toremoving local challenges and programs

## Future Enhancements

### Possible Additions
- Video content creation from scripts
- Mobile app version of dashboard
- Case-based learning scenarios
- Online quiz platform integration
- Regional state-wise customizable content

### Content Updates
- Annual epidemiological data refresh
- Guideline updates based on new research
- Addition of new vaccine information
- DR-TB treatment advancements
- COVID-TB co-infection studies

---

## Developer Notes

### Scripts Usage
- **Presentations**: Run `python scripts/generate_presentation.py`
- **Charts**: Run `cd visualizations; python generate_charts.py`
- **Dashboard**: Run `streamlit run dashboard/app.py`

### Content Integrity
- All factual information verified against official sources
- Indian statistics updated to 2023 data
- Treatment regimens follow WHO and RNTCP guidelines
- Educational content aligned with MBBS curriculum

### Version Control
- Ready for Git repository initialization
- Modular structure for easy updates
- Documentation included for maintainability

### CI/CD Setup for Streamlit Dashboard

To automatically test and deploy the Streamlit dashboard using GitHub Actions:

1. Create `.github/workflows/` directory in the repository root
2. Add a file `deploy_streamlit.yml` with the following content:

```yaml
name: Deploy Streamlit Dashboard

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run syntax check
      run: python -m py_compile dashboard/app.py

    - name: Run streamlit check
      run: streamlit hello --help

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Deploy to Streamlit Cloud
      env:
        ST_EMAIL: ${{ secrets.STREAMLIT_EMAIL }}
        ST_PASSWORD: ${{ secrets.STREAMLIT_PASSWORD }}
      run: |
        echo "Manual deployment required. Run: streamlit deploy"
```

3. **Manual Deployment Steps:**
   - Sign up at [share.streamlit.io](https://share.streamlit.io)
   - Add your Streamlit credentials as GitHub secrets: `STREAMLIT_EMAIL` and `STREAMLIT_PASSWORD`
   - Or deploy manually: `pip install streamlit` then `streamlit run dashboard/app.py`

4. **Local Testing:**
   - Run `streamlit run dashboard/app.py` in terminal
   - Access dashboard at `http://localhost:8501`

---

## Creator

**Dr. Siddalingaiah H S**  
Email: hssling@yahoo.com  
Phone: 8941087719  

---

*This module was created to provide high-quality, accurate, and comprehensive education on tuberculosis specifically tailored for MBBS students with Indian healthcare context. All materials can be freely used and modified for educational purposes.*
