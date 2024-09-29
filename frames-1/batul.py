from PIL import Image
import os

def extract_frames(gif_path, output_folder):
    with Image.open(gif_path) as img:
        for frame in range(img.n_frames):
            img.seek(frame)
            img.save(os.path.join(output_folder, f"frame_{frame}.png"))

# Example usage:
extract_frames("D:\Batul\mp\Menu.gif", "D:\Batul\mp\Frames")