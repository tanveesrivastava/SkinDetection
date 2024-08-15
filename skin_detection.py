import cv2
from ipywidgets import FileUpload
from IPython.display import display
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import io

def process_image(image_data):
    image = np.array(Image.open(io.BytesIO(image_data)))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    image_ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_ycrcb = np.array([0, 135, 85], dtype=np.uint8)
    upper_ycrcb = np.array([255,180,135], dtype=np.uint8)

    lower_hsv = np.array([0, 30, 60], dtype=np.uint8)
    upper_hsv = np.array([20, 150, 255], dtype=np.uint8)

    mask_ycrcb = cv2.inRange(image_ycrcb, lower_ycrcb, upper_ycrcb)
    mask_hsv = cv2.inRange(image_hsv, lower_hsv, upper_hsv)

    combined_mask = cv2.bitwise_or(mask_ycrcb, mask_hsv)

    combined_mask = cv2.GaussianBlur(combined_mask, (5, 5), 0)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    combined_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_CLOSE, kernel)
    combined_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_OPEN, kernel)

    contours, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        if cv2.contourArea(cnt) < 500:
            cv2.drawContours(combined_mask, [cnt], 0, 0, -1)

    skin = cv2.bitwise_and(image, image, mask=combined_mask)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    skin_rgb = cv2.cvtColor(skin, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(image_rgb)
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title("Image with skin detection")
    plt.imshow(skin_rgb)
    plt.axis('off')

    plt.show()

def on_upload_change(change):
    print("Upload changed:", change)
    if change['new']:
        for filename, file_info in change['new'].items():
            print("Processing file:", filename)
            image_data = file_info['content']
            process_image(image_data)

upload_widget = FileUpload(accept='image/*', multiple=False)
upload_widget.observe(on_upload_change, names='value')

display(upload_widget)

