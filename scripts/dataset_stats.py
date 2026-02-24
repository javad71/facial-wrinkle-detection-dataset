import os
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Paths
images_dir = '../data/train/images'
labels_dir = '../data/train/labels'

# Get stats
image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.png'))]
label_files = [f for f in os.listdir(labels_dir) if f.endswith('.txt')]

total_images = len(image_files)
total_labels = len(label_files)
print(f"Total images: {total_images}")
print(f"Total label files: {total_labels}")
print(f"Images without labels: {total_images - total_labels}")

# Parse labels for classes and box stats
class_counts = Counter()
box_counts = []
widths = []
heights = []

for label_file in label_files:
    with open(os.path.join(labels_dir, label_file), 'r') as f:
        lines = f.readlines()
        box_counts.append(len(lines))
        for line in lines:
            class_id, _, _, w, h = map(float, line.strip().split())
            class_counts[int(class_id)] += 1
            widths.append(w)
            heights.append(h)

avg_boxes_per_image = np.mean(box_counts) if box_counts else 0
print(f"Average boxes per image: {avg_boxes_per_image:.2f}")
print("Class distribution:", dict(class_counts))

# Visualize
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Class dist
axes[0].bar(class_counts.keys(), class_counts.values())
axes[0].set_title('Class Distribution')
axes[0].set_xlabel('Class ID')
axes[0].set_ylabel('Count')

# Boxes per image hist
axes[1].hist(box_counts, bins=20)
axes[1].set_title('Boxes per Image')
axes[1].set_xlabel('Number of Boxes')
axes[1].set_ylabel('Frequency')

# Box sizes
axes[2].hist(widths, bins=20, alpha=0.5, label='Widths')
axes[2].hist(heights, bins=20, alpha=0.5, label='Heights')
axes[2].set_title('Box Size Distribution (Normalized)')
axes[2].set_xlabel('Size')
axes[2].set_ylabel('Frequency')
axes[2].legend()

plt.tight_layout()
plt.show()

# Save
fig.savefig('dataset_stats.png')
print("Stats visualization saved as 'dataset_stats.png'")