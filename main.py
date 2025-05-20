import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_gamma_correction(image, gamma):
    invGamma = 1.0 / gamma
    table = np.array([(i / 255.0) ** invGamma * 255 for i in np.arange(256)]).astype("uint8")
    return cv2.LUT(image, table)

image = cv2.imread("fruits.jpg")

gamma_corrected_1 = apply_gamma_correction(image, gamma=0.3)
gamma_corrected_2 = apply_gamma_correction(image, gamma=1)
gamma_corrected_3 = apply_gamma_correction(image, gamma=3)

plt.figure(figsize=(10, 5))
plt.subplot(1, 4, 1)
plt.title("Original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1, 4, 2)
plt.title("Gamma Correction (0.3)")
plt.imshow(cv2.cvtColor(gamma_corrected_1, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1, 4, 3)
plt.title("Gamma Correction (1)")
plt.imshow(cv2.cvtColor(gamma_corrected_2, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1, 4, 4)
plt.title("Gamma Correction (3)")
plt.imshow(cv2.cvtColor(gamma_corrected_3, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.tight_layout()
plt.show()