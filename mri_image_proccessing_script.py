import nibabel as nib
import matplotlib.pyplot as plt

# Load and visualize a synthetic MRI image
img = nib.load('synthetic_mri_data/synthetic_mri_1.nii')
img_data = img.get_fdata()

plt.imshow(img_data[:, :, 15], cmap='gray')
plt.title('Synthetic MRI Slice')
plt.show()
