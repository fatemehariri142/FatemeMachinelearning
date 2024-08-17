import pandas as pd

# Load the synthetic clinical data
clinical_df = pd.read_csv('synthetic_clinical_data.csv')

# Preprocessing synthetic clinical data
clinical_df['Troponin_I_Positive'] = clinical_df['Troponin_I'] > 0.04
clinical_df['Troponin_T_Positive'] = clinical_df['Troponin_T'] > 0.04

print(clinical_df.head())
