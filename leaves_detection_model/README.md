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


