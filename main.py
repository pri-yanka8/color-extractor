import gradio as gr
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

def extract_colors(image):

    image = image.resize((150, 150))
    img_data = np.array(image)
    img_data = img_data.reshape((-1, 3))  

    kmeans = KMeans(n_clusters=5, random_state=42)
    kmeans.fit(img_data)
    colors = kmeans.cluster_centers_.astype(int)

    hex_colors = ['#%02x%02x%02x' % tuple(color) for color in colors]

    color_blocks = []
    for hex_color in hex_colors:
        block = Image.new("RGB", (100, 100), hex_color)
        color_blocks.append((block, hex_color)) 

    return color_blocks

with gr.Blocks() as demo:
    gr.Markdown("# 🎨 Image Color Palette Extractor")
    gr.Markdown("Upload an image and get your color palette!")

    img = gr.Image(type="pil")
    btn = gr.Button("Extract Colors")
    gallery = gr.Gallery(label="Extracted Colors", columns=5, rows=1) 

    btn.click(fn=extract_colors, inputs=img, outputs=gallery)

demo.launch()
