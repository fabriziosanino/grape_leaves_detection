# Grape Leaves Detection

## Change bbox label values(convert_labels.py)
### This code code will substituite all the lables values with the value TO_LABEL
1. Set **TO_LABEL** constant with the value to use
2. Set **PATH_TO_LABLES**


## Start finetuning plant-leaf-detection-and-classification (finetune_plant_leaf_detection.py)

1. Insert into the dataset folder the images and labels maintaining the current folder's structure
2. Modify the **path** varible in the *conf.yaml* file
3. If needed, modify the variables in the *.comet.config* file

## Test model prediction (test_prediction.py)
1. Set **MODEL_PATH** constant 
2. Set **image** path in which to set the bboxes

## Annotate very simple images. The output is in YOLO format (annotation_YOLO_format.py)
![Image example](./readme_example/0a06c482-c94a-44d8-a895-be6fe17b8c06___FAM_B.Rot%205019.JPG) 

This script can be used only with very simple images (like a leaf with a static background) in which the leaf 
are already classified but they need to have a box on it. The images need to be classified into the folder 
(i.e. esca folder -> only images classified as esca). The model write a box on the leaf, then the label 
is assotiated staticaly based on the classification done. 
1. Set **MODEL_PATH** constant. The model must only create bbox on leaves, the classification is not needed
2. Set the *images_dirs_and_label* variabile with:
  - **dir**: path to the directory that contains images of a specific class
  - **lbl**: integer label to associate to that class
  - **result_folder_path**: path to the directory that will contains the annotations. The folder struct follows the images one



