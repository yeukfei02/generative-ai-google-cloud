import streamlit as st
import time
import io
import base64
from PIL import Image
from services.generate_wallpaper_api import generate_wallpaper_api


def convert_base64_image_to_local_file(base64_image, i):
    img = Image.open(io.BytesIO(
        base64.decodebytes(bytes(base64_image, "utf-8"))))
    img.save(f"image-{i + 1}.png")


st.title("Generate Wallpaper")

st.write("")

input = st.text_area(
    "Wallpaper description",
    "concept art of an endless empty calm waveless ocean, bright blue sky, painting style, highly detailed, brush strokes, 8k",
    height=200
)

image_count = st.number_input(
    "Image count",
    value=1,
    max_value=3
)

token = st.text_area(
    "Google cloud access token",
    "",
    placeholder="gcloud auth print-access-token"
)


submit_button_clicked = st.button("Submit", type="primary")
if submit_button_clicked:
    if input and image_count and token:
        print(f"input = {input}")
        print(f"image_count = {image_count}")
        print(f"token = {token}")

        generate_wallpaper_results = generate_wallpaper_api(
            input, image_count, token)
        if generate_wallpaper_results:
            with st.spinner('Loading...'):
                time.sleep(2)

                for i, item in enumerate(generate_wallpaper_results):
                    base64_image = item.get("bytesBase64Encoded")
                    convert_base64_image_to_local_file(base64_image, i)
                    st.image(f"image-{i + 1}.png")
