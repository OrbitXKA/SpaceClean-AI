!git clone https://github.com/ultralytics/yolov5
%cd yolov5
!pip install -r requirements.txt
!cp space.png /content/yolov5/
!ls
!python detect.py --weights yolov5s.pt --source space.png
from IPython.display import Image, display
display(Image(filename='runs/detect/exp/space.png'))
