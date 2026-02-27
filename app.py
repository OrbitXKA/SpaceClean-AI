import torch
from pathlib import Path
import subprocess
def run_detection(image_path):
    print("Starting Space Debris Detection using YOLOv5...")
      # Run YOLOv5 detect script
    command = [
        "python", "detect.py",
        "--weights", "yolov5s.pt",
        "--source", image_path
    ]
    subprocess.run(command)
    print("Detection complete.")

if _name_ == "_main_":
    image_file = "space.png"
    if Path(image_file).exists():
        run_detection(image_file)
    else:
        print("Image file not found.")
