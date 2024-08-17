import nibabel as nib
import numpy as np
import os

# Number of synthetic patients
num_patients = 100  # Make sure this matches the number of patients in your clinical data

# Function to generate synthetic MRI images
def generate_synthetic_mri(shape=(64, 64, 30)):
    return nib.Nifti1Image(np.random.rand(*shape), np.eye(4))

# Create a directory to store the MRI data
os.makedirs('synthetic_mri_data', exist_ok=True)

# Generate synthetic MRI images for each patient
mri_data = {}
for pid in range(1, num_patients + 1):
    mri_data[pid] = generate_synthetic_mri()
    nib.save(mri_data[pid], f'synthetic_mri_data/synthetic_mri_{pid}.nii')

print("Synthetic MRI data generated and saved.")
