from ultralyticsplus import YOLO

if __name__=="__main__":

    model = YOLO("foduucom/plant-leaf-detection-and-classification")

    results = model.train(data="conf.yaml", epochs=1000)

    # The trained model will be saved into the folder 'runs/detect/train/weights'