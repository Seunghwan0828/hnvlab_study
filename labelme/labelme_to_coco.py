# import package
import labelme2coco

# set directory that contains labelme annotations and image files
labelme_folder = "/Users/jungseunghwan/Documents/labelme"

# set path for coco json to be saved
save_json_path = "/Users/jungseunghwan/Documents/labelme/test_coco.json"

# convert labelme annotations to coco
labelme2coco.convert(labelme_folder, save_json_path)