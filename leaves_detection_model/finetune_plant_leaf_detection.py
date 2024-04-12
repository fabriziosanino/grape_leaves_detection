from ultralyticsplus import YOLO

model = YOLO("foduucom/plant-leaf-detection-and-classification")

results = model.train(data="conf.yaml", epochs=10)

# The trained model will be saved into the folder 'runs/detect/train/weights'