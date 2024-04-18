from ultralyticsplus import YOLO, render_result
import glob
import os

MODEL_PATH = "D:\\best.pt"

# load model
model = YOLO(MODEL_PATH)

# set model parameters
model.overrides["conf"] = 0.25  # NMS confidence threshold
model.overrides["iou"] = 0.45  # NMS IoU threshold
model.overrides["agnostic_nms"] = False  # NMS class-agnostic
model.overrides["max_det"] = 1000  # maximum number of detections per image

# set image
images_dirs_and_label = [
    {
        "dir": "D:\\grapevine disease images\\Not Annotated\\Grape___Black_rot\\*",
        "lbl": "0",
        "result_folder_path": "D:\\grapevine disease images\\Annotated\\black_rot",
    },
    {
        "dir": "D:\\grapevine disease images\\Not Annotated\\Grape___Esca_(Black_Measles)\\*",
        "lbl": "1",
        "result_folder_path": "D:\\grapevine disease images\\Annotated\\esca",
    },
    {
        "dir": "D:\\grapevine disease images\\Not Annotated\\Grape___healthy\\*",
        "lbl": "2",
        "result_folder_path": "D:\\grapevine disease images\\Annotated\\healthy",
    },
    {
        "dir": "D:\\grapevine disease images\\Not Annotated\\Grape___Leaf_blight_(Isariopsis_Leaf_Spot)\\*",
        "lbl": "3",
        "result_folder_path": "D:\\grapevine disease images\\Annotated\\blight",
    },
]

for element in images_dirs_and_label:
    images = glob.glob(element["dir"])
    os.makedirs(element["result_folder_path"])

    for image in images:
        results = model.predict(image)

        file_name = image.split("\\")[-1].split(".JPG")[0]

        if len(results[0].boxes.xyxyn) == 0:
            print(file_name + " has problem of object detection")
        else:
          with open(element["result_folder_path"] + "\\" + file_name + ".txt", 'w') as file:
              # Write the results in YOLO format
              for row in results[0].boxes.xyxyn:
                  file.write(element["lbl"] + " " + str(row[0].item()) + " " + str(row[1].item()) + " " + str(row[2].item()) + " " + str(row[3].item()) + "\n")

              file.close()
