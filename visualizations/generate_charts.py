import matplotlib.pyplot as plt
import pandas as pd
import os

# Ensure output directory exists
os.makedirs('charts', exist_ok=True)
os.makedirs('data', exist_ok=True)

# Chart 1: TB Incidence Trend in India (2015-2023)
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
incidence_per_100k = [277, 275, 280, 285, 290, 268, 256, 241, 234]  # TB India report >= data

plt.figure(figsize=(10, 6))
plt.plot(years, incidence_per_100k, marker='o', linewidth=2, markersize=8, color='#1f77b4')
plt.title('TB Incidence Rate in India (2015-2023)', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Incidence per 100,000 Population', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(years)
plt.axvline(x=2020, color='#ff7f0e', linestyle='--', alpha=0.7, label='COVID-19 Impact')
plt.legend()

# Add data labels
for i, val in enumerate(incidence_per_100k):
    plt.text(years[i], val + 2, f'{val}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('charts/tb_incidence_india_trend.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved: tb_incidence_india_trend.png")

# Chart 2: Top 10 Indian States by TB Cases (2023)
states = ['Uttar Pradesh', 'Maharashtra', 'West Bengal', 'Bihar', 'Madhya Pradesh',
          'Rajasthan', 'Tamil Nadu', 'Gujarat', 'Karnataka', 'Andhra Pradesh']
cases = [325000, 270000, 225000, 215000, 180000, 160000, 140000, 135000, 120000, 115000]

plt.figure(figsize=(12, 8))
bars = plt.barh(states, cases, color='#ff7f0e', alpha=0.8)
plt.title('Estimated TB Cases by State in India (2023)', fontsize=16, pad=20)
plt.xlabel('Number of Cases (in thousands)', fontsize=12)
plt.ylabel('States', fontsize=12)
plt.grid(True, alpha=0.3, axis='x')

# Add value labels on bars
for bar, case in zip(bars, cases):
    plt.text(bar.get_width() + 5000, bar.get_y() + bar.get_height()/2,
             f'{case:,}', ha='left', va='center', fontsize=9)

plt.tight_layout()
plt.savefig('charts/tb_cases_by_state_india.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved: tb_cases_by_state_india.png")

# Chart 3: TB Burden Comparison - India vs Global
categories = ['India', 'Global']
incidence = [2.7, 1.0]  # Million cases
mortality = [0.45, 1.5]  # Million deaths

fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35
x = range(len(categories))

bars1 = ax.bar([i - bar_width/2 for i in x], incidence, bar_width,
               label='Annual Cases (Millions)', color='#2ca02c', alpha=0.8)
bars2 = ax.bar([i + bar_width/2 for i in x], mortality, bar_width,
               label='Annual Deaths (Millions)', color='#d62728', alpha=0.8)

ax.set_title('India\'s Contribution to Global TB Burden (2023)', fontsize=16, pad=20)
ax.set_xlabel('Context', fontsize=12)
ax.set_ylabel('Million People', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('charts/india_global_tb_comparison.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved: india_global_tb_comparison.png")

# Chart 4: Pie Chart - TB Cases by Type in India
types = ['Pulmonary\nConfirmed', 'Pulmonary\nClinically\nDiagnosed', 'Extrapulmonary']
cases = [1532684, 485414, 302902]  # TB India 2023 data

colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(cases, labels=types, colors=colors, autopct='%1.1f%%',
                                   startangle=90, wedgeprops={'edgecolor': 'white', 'linewidth': 2})

plt.title('TB Cases by Type in India (2023)', fontsize=16, pad=20)
plt.axis('equal')
plt.legend(wedges, types, title="Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.savefig('charts/tb_types_pie_india.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved: tb_types_pie_india.png")

# Chart 5: Risk Factors Proportion (Indian Context)
risk_factors = ['HIV/AIDS', 'Diabetes', 'Malnutrition', 'Smoking', 'Alcohol Use',
                'Overcrowding/Poverty', 'Other']
percentages = [18, 15, 20, 22, 10, 12, 3]  # Approximate percentages

colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#f9ca24', '#f0932b', '#eb4d4b', '#6c5ce7']
plt.figure(figsize=(12, 8))
bars = plt.bar(risk_factors, percentages, color=colors, alpha=0.8)
plt.title('TB Risk Factors in Indian Population (% of TB Cases)', fontsize=16, pad=20)
plt.xlabel('Risk Factors', fontsize=12)
plt.ylabel('Percentage of TB Cases (%)', fontsize=12)
plt.grid(True, alpha=0.3, axis='y')
plt.xticks(rotation=45, ha='right')

for bar, percentage in zip(bars, percentages):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             f'{percentage}%', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('charts/tb_risk_factors_india.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved: tb_risk_factors_india.png")

# Chart 6: Treatment Outcomes in India (2023)
outcomes = ['Successfully Treated', 'Died', 'Loss to Follow-up', 'LAMA', 'Others']
percentages = [84, 9, 4, 2, 1]

colors = ['#2ecc71', '#e74c3c', '#f39c12', '#9b59b6', '#95a5a6']
plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(percentages, labels=outcomes, colors=colors,
                                   autopct='%1.1f%%', startangle=90,
                                   wedgeprops={'edgecolor': 'white', 'linewidth': 2})

plt.title('TB Treatment Outcomes in India (2023)', fontsize=16, pad=20)
plt.axis('equal')

plt.tight_layout()
plt.savefig('charts/tb_treatment_outcomes_india.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved: tb_treatment_outcomes_india.png")

# Create data CSV file for reference
data = {
    'State': states,
    'Estimated_Cases_2023': cases,
    'Risk_Factor': risk_factors,
    'Risk_Percentage': percentages,
    'Treatment_Outcome': outcomes,
    'Outcome_Percentage': percentages
}

df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))
df.to_csv('data/tb_india_statistics.csv', index=False)
print("Saved: tb_india_statistics.csv")

print("\nAll visualizations generated successfully!")
print("Files saved in visualizations/charts/ and visualizations/data/")
