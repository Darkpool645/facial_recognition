from ultralytics import YOLO

model = YOLO('yolov8n.pt')

results = model.train(
    data='C:\\Users\\angel\\PycharmProjects\\facial_recognition\\dataset\\data.yaml',
    epochs=10,
    imgsz=640, 
    batch=16,
    name='utez_model'
)

model.save('utes_model.pt')
