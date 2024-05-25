# -*- coding: utf-8 -*-
"""Doodling.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Dsf0xQQZloEN3GKwaL_CIGok9ZFVqkv_
"""

import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import numpy as np
import cv2

st.title("Doodle to Coordinates")

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fill color with some opacity
    stroke_width=2,
    stroke_color="black",
    background_color="white",
    height=400,
    width=400,
    drawing_mode="freedraw",
    key="canvas",
)

# Process the canvas image
if canvas_result.image_data is not None:
    # Convert the image to grayscale
    image = Image.fromarray(canvas_result.image_data.astype('uint8'), 'RGBA').convert('L')
    image_np = np.array(image)

    # Threshold the image
    _, binary_image = cv2.threshold(image_np, 127, 255, cv2.THRESH_BINARY_INV)

    # Find contours
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Extract coordinates
    coordinates = []
    for contour in contours:
        for point in contour:
            coordinates.append((point[0][0], point[0][1]))

    # Display coordinates
    st.write("Coordinates:", coordinates)

    # Display the processed image
    st.image(binary_image, caption="Processed Doodle")