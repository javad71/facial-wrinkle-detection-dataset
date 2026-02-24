# facial-wrinkle-detection-dataset
Dataset for the arXiv paper 'A Deep Learning-Based Method for Facial Wrinkle Detection'

## Dataset Analysis & Visualization
This repository contains Python scripts to help explore and visualize the **Facial Wrinkle Detection** dataset (YOLO format).

- **Total images**: 2142
- **Total label files**: 2142
- **Images without labels**: 0
- **Average bounding boxes per image**: 16.95
- **Classes** (wrinkle types):

| Class ID | Wrinkle Type     | Count  |
|----------|------------------|--------|
| 0        | bunny_line       | 361    |
| 1        | chin             | 1237   |
| 2        | crows_feet       | 6016   |
| 3        | forehead         | 11015  |
| 4        | frown_line       | 4151   |
| 5        | gummy_smile      | 7970   |
| 6        | masseter         | 2976   |
| 7        | sad_smile        | 2253   |
| 8        | smoker_lines     | 329    |

**Total annotations**: ~36,308 bounding boxes

### Folder Structure (relevant parts)
facial-wrinkle-detection-dataset/
├── data/
│   ├── train/
│   │   ├── images/          ← all training images (.jpg / .png)
│   │   └── labels/          ← corresponding YOLO .txt label files
├── scripts/
│   ├── dataset_stats.py
│   └── visualize_detections.py
├── annotated_samples/       ← (generated) individual annotated images
└── README.md


#### Requirements
Install the required packages:

```bash
pip install opencv-python numpy matplotlib

##### Usage – Analysis Scripts
1. Dataset Statistics
Shows counts, class distribution, average boxes per image, histograms of boxes-per-image and box size distribution.

python scripts/dataset_stats.py

Output:

Console summary (as shown in Overview above)
Saves: dataset_stats.png

2. Visualize Annotations
Randomly selects 5 images, draws all ground-truth bounding boxes with class names, and saves them.

python scripts/visualize_detections.py

Output:
Combined preview saved as sample_detections.png
Individual high-resolution annotated images saved in:
scripts/annotated_samples/annotated_*.jpg

You can open the annotated_samples/ folder to inspect detailed annotations, zoom in, and check label quality for specific images.

###### Citation
If you use this dataset in your research, please cite:

@article{yourname2025wrinkledetection,
  title={A Deep Learning-Based Method for Facial Wrinkle Detection},
  author={Your Name and Co-authors},
  journal={arXiv preprint arXiv:xxxx.xxxxx},
  year={2025},
  url={https://arxiv.org/abs/xxxx.xxxxx}
}

Also consider citing this repository:

Javad (2026). facial-wrinkle-detection-dataset.
https://github.com/yourusername/facial-wrinkle-detection-dataset

####### Contact / Questions
Feel free to open an issue if:

You find annotation errors
You want more preprocessing / augmentation scripts
You need help integrating with YOLOv8 / YOLOv11 training

Good luck with your wrinkle detection research! 🧓📸