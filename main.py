import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from skimage.filters import median
from skimage.morphology import ball
from image_utils import load_image, edge_detection

# שלבי עבודה
original_img = load_image("my_picture.jpg")
clean_img = median(original_img, ball(3))
edge_mag = edge_detection(clean_img)

# הצגת היסטוגרמה לבחירת סף
plt.hist(edge_mag.ravel(), bins=256)
plt.show()

# יצירת תמונה בינארית (שנה את ה-100 לפי הצורך)
threshold = 100 
binary_image = edge_mag > threshold

# שמירה והצגה
plt.imshow(binary_image, cmap='gray')
plt.show()

final_output = Image.fromarray((binary_image * 255).astype(np.uint8))
final_output.save("edge_result.png")
