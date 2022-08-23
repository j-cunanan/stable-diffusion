import tempfile

import streamlit as st
from PIL import Image
import glob
import subprocess

st.title("Text-to-Image")

st.write("This is a demo of a text-to-image model. It takes a text description of an image and generates an image "
         "that matches the description.")

image_file = st.file_uploader("Upload a base image if you want, skip otherwise.",
                              type=['png', 'jpg'],
                              )
text = st.text_input("Enter a description of an image")


if text:
    st.write("Generating image, it may take a minute or two ...")

    folder = text.replace(" ", "_")
    if image_file:
        model_type = "img2img"
        with tempfile.NamedTemporaryFile() as fp:
            fp.write(image_file.getvalue())
            cmd = ["python", "optimizedSD/optimized_img2img.py", "--prompt", text,
                   "--init-img", fp.name, "--strength", "0.8", "--H", "512", "--W", "512", "--small_batch"]
            subprocess.run(cmd,
                           check=True)
    else:
        model_type = "txt2img"
        cmd = ["python", "scripts/txt2img.py", "--prompt", text, "--H", "512", "--W", "512",
               "--seed", "27", "--n_iter", "2", "--n_samples", "3", "--plms", "--skip_grid",
               "--outdir", f"outputs/txt2img-samples/{folder}"]
        subprocess.run(cmd,
                       check=True)

    for filename in glob.glob(f'outputs/{model_type}-samples/{folder}/*.png'):
        st.image(Image.open(filename))
        st.write("Image generated!")
