import sys
import os
import argparse
import subprocess
from moviepy.editor import *

def convert_mp4_to_mp3(mp4_path):
    video = VideoFileClip(mp4_path)
#    mp3_path = os.path.splitext(mp4_path)[0] + '.mp3'
    mp3_path = os.path.join(os.getcwd(), f"{os.path.splitext(os.path.basename(mp4_path))[0]}.mp3")
    video.audio.write_audiofile(mp3_path)
    return mp3_path

def call_denoiser(input_path, output_path):
    script_path = os.path.join('Denoiser-master', 'use_denoiser.py')
    os.system(f'python {script_path} {input_path} {output_path}')

def separate_audio(input_file, output_folder=os.getcwd()):
    # Construct the Spleeter command
    command = [
        "spleeter",
        "separate",
        "-o", output_folder,
        input_file
    ]

    # Run the Spleeter command
    try:
        subprocess.run(command, check=True)
        print("Audio separation completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def main(input_file, denoise):

    mp4_path = input_file
    mp3_path = convert_mp4_to_mp3(mp4_path)
    if denoise:
        denoised_mp3_path = os.path.join(os.getcwd(), f"denoised_{os.path.splitext(os.path.basename(mp3_path))[0]}.mp3")
        call_denoiser(mp3_path, denoised_mp3_path)
        separate_audio(denoised_mp3_path)

    else:
        separate_audio(mp3_path)

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Your script description")

    # Positional arguments
    parser.add_argument("input_file", help="Path to the .mp4 video")

    # Optional boolean argument with a default value of False
    parser.add_argument("--denoise", action="store_true", default=False, help="Denoise audio and remove noises? Do this if the audio is recorded with a lot of noises")

    args = parser.parse_args()
    main(args.input_file, args.denoise)
