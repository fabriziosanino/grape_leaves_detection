import glob
import fileinput

TO_LABEL = "0" 
PATH_TO_LABELS = ".\\dataset\\labels\\train\\*"

annotations_list = glob.glob(PATH_TO_LABELS)

for annotation in annotations_list:
  with fileinput.FileInput(annotation, inplace=True) as file:
    for line in file:
      parts = line.split(' ')
      parts[0] = TO_LABEL
      new_line = ' '.join(parts)
      print(new_line, end='')
