import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the synthetic clinical data
clinical_df = pd.read_csv('synthetic_clinical_data.csv')

# Modify the inclusion criteria and re-run the analysis
new_filter = clinical_df['Age'] > 50
filtered_df = clinical_df[new_filter]

sns.boxplot(x='COVID_Positive', y='Troponin_I', data=filtered_df)
plt.title('Troponin I Levels in Patients Older Than 50')
plt.show()
