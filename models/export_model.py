from ultralytics import YOLO

# Load a model
model = YOLO('models/yolov8n.pt')  # load a custom trained

# Export the model
model.export(format='onnx')  # ONNX模型
# model.export(format='engine') #TRT模型
