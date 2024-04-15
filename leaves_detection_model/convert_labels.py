import glob
import fileinput
'''
"categories": [
    {
      "id": 0,
      "name": "esca"
    },
    {
      "id": 1,
      "name": "healthy"
    },
    {
      "id": 2,
      "name": "pvl_esca"
    },
    {
      "id": 3,
      "name": "pvl_healthy"
    },
    {
      "id": 4,
      "name": "pvl_unknown"
    },
    {
      "id": 5,
      "name": "unknown"
    }
'''
TO_LABEL = "0" 
PATH_TO_LABELS = "C:/Users/Alessandro Pecora/OneDrive - Politecnico di Torino/progetti/DIVINE/label_studio_model/grape_leaves_detection/leaves_detection_model/raw_data_only_leaf/labels/*"

annotations_list = glob.glob(PATH_TO_LABELS)

for annotation in annotations_list:
  with fileinput.FileInput(annotation, inplace=True) as file:
    for line in file:
      parts = line.split(' ')
      # label=int(parts[0])
      # if label==2: #pvl_esca to esca
      #   parts[0]="0"
      # elif label==3:
      #   parts[0]="1"
      # elif label==5 or label==4:
      #   parts[0]="0"
      parts[0]="0"
 
      new_line = ' '.join(parts)
      print(new_line, end='')




