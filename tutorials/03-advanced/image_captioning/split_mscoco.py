import json
import os
from shutil import copyfile


def split_data(json_path, train=True):

    if train:
        dataset = 'train'
    else:
        dataset = 'val'

    with open(json_path) as json_file:
        data = json.load(json_file)
        categories = data['categories']

        image_num = len(data['images'])

        classes = dict()  # Contains 80 classes of MS-COCO, key is class id
        for category in categories:
            classes[category['id']] = category['name']

        for key, value in classes.items():
            if not os.path.exists('{}2014/{}'.format(dataset, value)):
                os.mkdir('{}2014/{}'.format(dataset, value))

        annotations = data['annotations']
        print(image_num, len(annotations))

        annotation_dict = {}
        image_count = 0

        for i, annotation in enumerate(annotations, 1):
            image_id = annotation['image_id']
            file_name = ('COCO_%s2014_%012d.jpg' % (dataset,  image_id))
            category_id = annotation['category_id']

            dst_file = ('{}2014/{}/{}'.format(dataset, classes[category_id], file_name))
            src_file = '/home/dexter/Downloads/{}2014/{}'.format(dataset, file_name)

            if image_id in annotation_dict:  # At least two annotations in an image, should delete this image
                if os.path.exists(dst_file):
                    image_count -= 1
                    os.remove(dst_file)
                continue  # Here to only pick images having just one class / or one annotation
            else:
                annotation_dict[image_id] = 1

            copyfile(src_file, dst_file)

            if os.path.exists('{}2014/{}/{}'.format(dataset, classes[category_id], file_name)):  # If copy successfully
                #  print("File " + '{}2014/{}/{}'.format(dataset, classes[category_id], file_name) + " is copied")
                image_count += 1
            else:
                print("Copy failed!")

            if i%1000 == 0:  # With 1k annotations parsed, we print the number of images having a single class
                print("{}/{} images have been copied!".format(image_count, image_num))

        print("Finish {} splitting dataset from {}".format(dataset, json_path))


#split_data('instances_train2014.json')
split_data('instances_val2014.json', train=False)