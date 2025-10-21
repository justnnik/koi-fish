import streamlit as st
import numpy as np
import random
import time

st.set_page_config(page_title="koi fish 🐟", page_icon="🐠", layout="centered")

st.markdown("<h2 style='text-align:center;'>Welcome to Nico's Aquarium 🐟</h2>", unsafe_allow_html=True)
st.write("Here some koi swimming for koi... ✨")

if st.button("Show the koi 💖"):
    placeholder = st.empty()

    height, width = 25, 70
    koi_count = 5
    frame_delay = 0.15

    koi_shape = [
        "   __",
        "><((°>",
        "   ‾‾"
    ]

    koi_positions = [
        [random.randint(0, height - 4), random.randint(0, width - 15), random.choice([-1, 1])]
        for _ in range(koi_count)
    ]

    for frame in range(120):
        # buat kanvas kosong
        canvas = [[" " for _ in range(width)] for _ in range(height)]

        for i, (y, x, direction) in enumerate(koi_positions):
            # gambar ikan di posisi saat ini
            for j, line in enumerate(koi_shape):
                for k, ch in enumerate(line):
                    if 0 <= y + j < height and 0 <= x + k < width and ch.strip():
                        canvas[y + j][x + k] = ch

            # update posisi ikan
            x += direction
            if x <= 0 or x >= width - len(koi_shape[1]):
                direction *= -1
            koi_positions[i] = [y, x, direction]

        # gabungkan jadi string HTML dengan <span> berwarna
        frame_str = ""
        for row in canvas:
            line_html = "".join(
                f"<span style='color:orange'>{ch}</span>" if ch.strip() else "&nbsp;"
                for ch in row
            )
            frame_str += line_html + "<br>"

        placeholder.markdown(
            f"<div style='font-family:monospace; text-align:center; line-height:1;'>{frame_str}</div>",
            unsafe_allow_html=True
        )

        time.sleep(frame_delay)

    st.markdown(
        "<h3 style='text-align:center; color:orange;'>You’re my koi in a calm pond 🧡<br>from Nico 💌</h3>",
        unsafe_allow_html=True
    )
    st.balloons()
