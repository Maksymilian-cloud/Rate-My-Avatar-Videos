import cv2
import numpy as np

def rgb_to_string(rgb_array):
    """Converts an array of RGB values to a string format."""
    return ' '.join(' '.join(map(str, pixel)) for pixel in rgb_array)

def extract_frames(video_path, output_path, frame_count=100):
    """Extracts frames from the video and saves them in a specified format."""
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    frames = []
    count = 0

    while count < frame_count:
        ret, frame = cap.read()

        if not ret:
            break

        # Convert frame to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Create a string format for the frame
        rgb_string = rgb_to_string(rgb_frame.reshape(-1, 3))

        # Append formatted frame data with "A" delimiter
        frames.append(rgb_string + "A")

        count += 1

    cap.release()

    # Save to output file with .txt extension
    with open(output_path + '.txt', 'w') as file:
        for frame in frames:
            file.write(frame + "N")  # Use "N" to separate frames

    print(f"{len(frames)} frames extracted and saved to '{output_path}.txt'.")

# Specify the video path and output path
video_path = 'input_video.mp4'  # Change this to your video file
output_path = 'frames'  # Output file name (without extension)

extract_frames(video_path, output_path)
