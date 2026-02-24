import cv2
import numpy as np
import os
import random
import matplotlib.pyplot as plt  # only needed if you want preview

# ────────────────────────────────────────────────
# CONFIGURATION
# ────────────────────────────────────────────────
images_dir = '../data/train/images'
labels_dir = '../data/train/labels'
output_dir  = 'annotated_samples'           # folder where images will be saved

# Create output folder if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Your class names
class_names = [
    'bunny_line', 'chin', 'crows_feet', 'forehead', 
    'frown_line', 'gummy_smile', 'masseter', 
    'sad_smile', 'smoker_lines'
]

# Number of random samples to process
num_samples = 5

# Box and text style
BOX_COLOR = (0, 255, 0)      # green
BOX_THICKNESS = 3
TEXT_COLOR = (0, 255, 0)
TEXT_SCALE = 0.7
TEXT_THICKNESS = 2
# ────────────────────────────────────────────────

def draw_yolo_boxes(image_path, label_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Cannot read image: {image_path}")
        return None

    h, w, _ = img.shape

    if os.path.exists(label_path):
        with open(label_path, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) != 5:
                    continue
                try:
                    class_id, cx, cy, bw, bh = map(float, parts)
                    x1 = int((cx - bw/2) * w)
                    y1 = int((cy - bh/2) * h)
                    x2 = int((cx + bw/2) * w)
                    y2 = int((cy + bh/2) * h)

                    # Draw rectangle
                    cv2.rectangle(img, (x1, y1), (x2, y2), BOX_COLOR, BOX_THICKNESS)

                    # Add label text
                    label = class_names[int(class_id)] if int(class_id) < len(class_names) else f'class_{int(class_id)}'
                    cv2.putText(
                        img, 
                        label, 
                        (x1, max(y1 - 10, 20)),  # avoid going above image
                        cv2.FONT_HERSHEY_SIMPLEX,
                        TEXT_SCALE,
                        TEXT_COLOR,
                        TEXT_THICKNESS
                    )
                except ValueError:
                    print(f"Skipping invalid line in {label_path}: {line.strip()}")
    else:
        print(f"No label file found for: {os.path.basename(image_path)}")

    return img  # returns BGR image


# ────────────────────────────────────────────────
# MAIN LOGIC
# ────────────────────────────────────────────────

image_files = [f for f in os.listdir(images_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

if not image_files:
    print("No images found in", images_dir)
    exit()

# Select samples
if len(image_files) <= num_samples:
    samples = image_files
else:
    samples = random.sample(image_files, num_samples)

print(f"Processing {len(samples)} sample images...\n")

for i, img_file in enumerate(samples, 1):
    img_path = os.path.join(images_dir, img_file)
    label_file = os.path.splitext(img_file)[0] + '.txt'
    label_path = os.path.join(labels_dir, label_file)

    print(f"[{i}/{len(samples)}] Processing: {img_file}")

    annotated_img = draw_yolo_boxes(img_path, label_path)

    if annotated_img is not None:
        save_path = os.path.join(output_dir, f"annotated_{img_file}")
        success = cv2.imwrite(save_path, annotated_img)
        if success:
            print(f"   → Saved: {save_path}")
        else:
            print(f"   → Failed to save: {save_path}")

    print()  # empty line between samples

print(f"\nAll done! Check folder: {os.path.abspath(output_dir)}")
print("You can open these images to inspect annotations closely.")