import pandas as pd
import numpy as np

# Set the number of synthetic patients
num_patients = 100

# Generate synthetic clinical data
np.random.seed(42)
data = {
    'Patient_ID': range(1, num_patients + 1),
    'Age': np.random.randint(20, 80, size=num_patients),
    'Sex': np.random.choice(['Male', 'Female'], size=num_patients),
    'COVID_Positive': np.random.choice(['Yes', 'No'], size=num_patients, p=[0.7, 0.3]),
    'Troponin_I': np.random.uniform(0.01, 0.5, size=num_patients),
    'Troponin_T': np.random.uniform(0.01, 0.5, size=num_patients),
    'ECG_Abnormal': np.random.choice(['Yes', 'No'], size=num_patients, p=[0.6, 0.4]),
    'Symptoms': np.random.choice(['Chest Pain', 'Dyspnea', 'Both', 'None'], size=num_patients, p=[0.4, 0.4, 0.1, 0.1])
}

clinical_df = pd.DataFrame(data)

# Save to CSV
clinical_df.to_csv('synthetic_clinical_data.csv', index=False)

print(clinical_df.head())
