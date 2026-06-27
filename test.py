import cv2
from ultralytics import YOLO

print("================================")
print("Blackjack Vision Analyzer")
print("================================")
print("OpenCV:", cv2.__version__)

model = YOLO("yolo11n.pt")

print("Modelo cargado correctamente")