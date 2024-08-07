# Skin-Detection

This project demonstrates a method for detecting skin regions in images using color space transformations and image processing techniques with OpenCV. 

## Features

- Convert images to different color spaces (YCrCb and HSV).
- Apply color thresholds to isolate skin regions.
- Use morphological operations to clean up the mask.
- Detect and remove small contours.
- Display the original and processed images side by side.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- Matplotlib
- PIL (Python Imaging Library)
- ipywidgets

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/skin-detection.git
cd skin-detection
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

Alternatively, you can manually install the required packages:

```bash
pip install opencv-python numpy matplotlib pillow ipywidgets
```

## Usage

1. Launch Jupyter Notebook:

```bash
jupyter notebook
```

2. Open the notebook file where the code is located.

3. Run the cells to initialize the file upload widget.

4. Upload an image using the widget. The script will process the image and display the original and skin-detected images side by side.

## Code Overview

The main function `process_image(image_data)` performs the following steps:

1. Convert the uploaded image from RGB to BGR.
2. Transform the image to YCrCb and HSV color spaces.
3. Apply color thresholds to create masks for skin detection.
4. Combine the masks and apply Gaussian blur.
5. Use morphological operations to close and open gaps in the mask.
6. Remove small contours based on contour area.
7. Apply the mask to the original image to isolate skin regions.
8. Display the original and processed images side by side.

The `on_upload_change(change)` function handles the file upload event and processes the uploaded image.

### Image 1
![Image 1](Output%20Images/image1.png)

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

