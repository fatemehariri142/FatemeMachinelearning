import seaborn as sns
import matplotlib.pyplot as plt

# Load the synthetic clinical data
clinical_df = pd.read_csv('synthetic_clinical_data.csv')

# Statistical analysis example
sns.boxplot(x='COVID_Positive', y='Troponin_I', data=clinical_df)
plt.title('Troponin I Levels in COVID-19 Positive and Negative Patients')
plt.show()
