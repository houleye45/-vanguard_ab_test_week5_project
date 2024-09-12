# Vanguard's Company Project

👥 The Team:
- Houleye Anne
- Maïlys Jaffret
  

# 🔍 Project Overview

This project, conducted by Vanguard's Customer Experience team, aims to evaluate whether a new digital user interface (UI) enhances the user experience. The experiment involved two groups:
- Test Group: Exposed to the new UI.
- Control Group: Continued using the existing interface.
  
  
# 🎯 Objective
The main research question is: Does the new UI design result in a higher completion rate among users?


# 🏗️ Project Structure

This project revolves around several datasets related to client profiles, digital interactions, and participation in an A/B test. Here’s an overview of the datasets used and created during the experiment:

### 1. 📂 Datasets Used
- DF1: Clients Profile : contains customer information, such as demographics and basic profile data.
- DF2: Digital Footprints : data on clients online interactions. This dataset was formed by concatenating two sources of interaction data.
- DF3: Experiment Roster : information about the clients who participated in the A/B test, including their group assignment (Test or Control).
  
### 2. 🛠️ Datasets Created
- df_client_info : created by merging DF1 (client profile data) with the experiment information.
- client_last_start : filtered from DF2, retaining only steps occurring after the last "start" interaction for each client.
- df_total_info : a comprehensive dataset combining all relevant information.

### 3. 🔄 Final Datasets Based on the 'Variation' Column
- df_test : clients in the Test group who interacted with the new UI.
- df_control : clients in the Control group who interacted with the original UI.
- df_no_participation : clients who did not participate in the A/B test and were excluded from the analysis.
  


# 🛠️ Tools and Technologies Used

- Python: Core language for data cleaning, analysis, and visualization.
- Pandas & NumPy: Libraries for data manipulation and numerical analysis.
- Matplotlib & Seaborn: Libraries used for data visualization.
- Statsmodels & SciPy: Libraries for statistical analysis and hypothesis testing.
- Jupyter Notebook & Google Colab: Interactive environments for executing code and exploring data.
- Tableau: Used for creating visual dashboards.
  

# 📊 Findings and Conclusions

### 1. Key Findings
Based on KPI Analysis:
- Completion Rate Improvement: The Test group showed a significant improvement in completion rates.
- Higher Error Rate: The Test group also experienced a higher error rate than the Control group.


Based on Hypothesis Testing:
- Completion Rate Difference: The difference in completion rates between the Test and Control groups was statistically significant (p-value = 0.0).
- Cost-Effectiveness: The Test group’s completion rate was at least 5% higher than the Control group, meeting the cost-effectiveness threshold (p-value = 0.0).
- Error Rate: The Test group had a significantly higher error rate compared to the Control group (p-value = 0.0).
  
### 2. 📌 Conclusion
A balanced user experience should focus on both efficiency and accuracy. While the new UI led to higher completion rates, it also introduced a concerning increase in errors. This suggests the current design prioritizes speed over accuracy, potentially compromising user satisfaction.

🛠️ Recommendation: Vanguard should reassess the UI design to ensure it meets user needs without increasing errors. How can Vanguard optimize the design to maintain efficiency without compromising accuracy?

# 📦 Deliverables

- 📝 A Jupyter Notebook with the code, analysis, and visualizations.
- 🐍 Python files (.py) for key functions.
- 📊 Tableau file for dashboard visualizations.
- 📑 A slide deck for project presentation.
- 📄 This README for thorough project documentation.




