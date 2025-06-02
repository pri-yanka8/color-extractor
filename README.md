Image Color Palette Extractor 🎨

This is a simple and visually fun web app that lets you upload any image and instantly get a 5-color palette extracted using KMeans clustering. It’s built using Gradio for the UI and scikit-learn for color analysis.

🚀Features

🖼️ Upload any image (PNG, JPG, etc.)
🧠 Uses KMeans clustering to find the 5 most dominant colors
🌈 Returns color blocks alongside their HEX codes
⚡ Fast and easy to use thanks to Gradio’s interactive UI

---

🛞How It Works

The image is resized to 150x150 to reduce processing time

Image pixels are flattened and fed into a KMeans clustering model

The top 5 color clusters are converted into HEX color codes

Each color is displayed as a block with its corresponding HEX code

---

💻Tech Stack

Gradio – for building the web-based UI
Pillow – to handle image resizing and manipulation
NumPy – for efficient image array handling
scikit-learn – for applying KMeans clustering to extract dominant colors

---

How to Run

Install dependencies
pip install gradio scikit-learn pillow numpy

Run the Python script
python color_palette_extractor.py

A local Gradio app will launch in your browser
Upload an image and enjoy your custom palette!

---

⚡Future Enhancements

📁 Drag-and-drop image support
🎯 Allow user to select number of colors (k value)
📋 Copy-to-clipboard button for HEX codes
📊 Show RGB values alongside HEX

