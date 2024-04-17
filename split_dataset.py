import os
import random

def split_dataset(image_dir, output_dir, train_ratio=0.7, val_ratio=0.2, test_ratio=0.1):
    images = [img for img in os.listdir(image_dir) if img.endswith('.jpg')]  # Adjust the extension
    total_images = len(images)
    random.shuffle(images)

    train_size = int(total_images * train_ratio)
    val_size = int(total_images * val_ratio)

    # Split the dataset
    train_images = images[:train_size]
    val_images = images[train_size:train_size + val_size]
    test_images = images[train_size + val_size:]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(os.path.join(output_dir, 'train.txt'), 'w') as f:
      for item in train_images:
        f.write("%s\n" % os.path.splitext(item)[0]) 

    with open(os.path.join(output_dir, 'val.txt'), 'w') as f:
      for item in val_images:
        f.write("%s\n" % os.path.splitext(item)[0]) 
        
    with open(os.path.join(output_dir, 'test.txt'), 'w') as f:
      for item in test_images:
        f.write("%s\n" % os.path.splitext(item)[0])

    return train_images, val_images, test_images

# Usage
image_dir = '/content/drive/MyDrive/GreenStand/Pilot/leaf/images'
output_dir = '/content/drive/MyDrive/GreenStand/Pilot/leaf/splits'
split_dataset(image_dir, output_dir=output_dir)