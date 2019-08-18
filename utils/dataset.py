from torch.utils.data import Dataset
import os
import logging


class FlickrDataset(Dataset):
    """ MIRFLICKR-25K dataset """

    def __init__(self, images_dir, text_dir, label_dir):
        # get images list
        image_list = {}
        for img in os.listdir(images_dir):
            img_id = int(img.replace('im', '').replace('.jpg', ''))
            image_list[img_id] = os.path.join(images_dir, img)
        # get text list
        text_list = {}
        for txt in os.listdir(text_dir):
            txt_id = int(txt.replace('tags', '').replace('.txt', ''))
            text_list[txt_id] = os.path.join(text_dir, txt)
        self.data_dict = {}

        self.label_set = []
        for label_file in os.listdir(label_dir):
            label = label_file.replace('.txt', '')
            if label not in self.label_set:
                label_id = len(self.label_set)
                self.label_set.append(label)
            else:
                label_id = self.label_set.index(label)
            label_path = os.path.join(label_dir, label_file)
            with open(label_path) as f:
                img_ids = f.readlines()
            for img_id in img_ids:
                img_id = int(img_id)
                if self.data_dict.get(img_id):
                    self.data_dict.get(img_id)['labels'].append(label_id)
                else:
                    self.data_dict[img_id] = {
                        'labels': [label_id],
                        'img': image_list[img_id],
                        'tags': text_list[img_id]
                    }

    def __len__(self):
        return len(self.data_dict)

    def __getitem__(self, index):
        return list(self.data_dict.items())[index][1]


if __name__ == '__main__':
    data_dir = '/home/dejie/data/mirflickr/'
    image_dir = os.path.join(data_dir, 'images')
    text_dir = os.path.join(data_dir, 'tags')
    label_dir = os.path.join(data_dir, 'annotations')
    flickr_dataset = FlickrDataset(image_dir, text_dir, label_dir)
    print(len(flickr_dataset))
    print(flickr_dataset[0])
    print(flickr_dataset.label_set[37])
