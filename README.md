# README for Python Turtle Dot Painting Generator

## Overview
This Python script uses the Turtle Graphics Library and Colorgram to create a dot painting. It extracts color data from an image and uses these colors to draw a grid of dots, mimicking the style of pointillism.

## Features
- Extracts colors from an image using Colorgram.
- Generates a grid of colored dots using Turtle Graphics.
- Customizable number of dots and color extraction.

## Requirements
- Python 3
- Turtle Graphics Library (usually pre-installed with Python).
- Colorgram.py (`pip install colorgram.py`).

## How to Run
1. Ensure you have Python 3 and the necessary libraries installed.
2. Place the image you want to extract colors from in the same directory as the script and rename it to `painting.jpg`.
3. Run the script. A window will display the dot painting.

## Code Explanation
- **Color Extraction**: The script uses Colorgram to extract 30 colors from `painting.jpg`.
- **Turtle Setup**: Initializes the Turtle module for drawing.
- **Dot Painting**: The script uses a for loop to place dots in a grid pattern. The color of each dot is randomly chosen from the extracted colors.
- **User Interaction**: The script ends when the user clicks on the Turtle graphics window.

## Customization
- Change the `painting.jpg` to use different colors.
- Modify `number_of_dots` to change the size of the painting.
- Adjust the range in `colorgram.extract()` to change the number of colors extracted.

## Note
- The script removes the first two extracted colors, assuming they might be overly dominant (like white or black). Adjust this as needed.
- Running the script may take a few moments due to color extraction and the speed of the Turtle graphics.

## License
This project is free to use and modify for personal or educational purposes.