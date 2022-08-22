import streamlit as st
from PIL import Image
import glob
import subprocess


st.title("Text-to-Image")

st.write("This is a demo of a text-to-image model. It takes a text description of an image and generates an image "
         "that matches the description.")


text = st.text_input("Enter a description of an image")

if text:
    st.write("Generating image, it may take a minute or two ...")

    subprocess.run(["python", "optimizedSD/optimized_txt2img.py", "--prompt", text, "--H", "512", "--W", "512",
                    "--seed", "27", "--n_iter", "1", "--n_samples", "4"],
                   check=True)
    folder = text.replace(" ", "_")
    for filename in glob.glob(f'outputs/txt2img-samples/samples/{folder}/*.png'):
        st.image(Image.open(filename))
        st.write("Image generated!")
