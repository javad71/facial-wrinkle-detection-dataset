# Facial Wrinkle Detection Dataset

> Dataset for the arXiv paper: **"A Deep Learning-Based Method for Facial Wrinkle Detection"**

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![YOLO Format](https://img.shields.io/badge/format-YOLO-orange.svg)](https://github.com/ultralytics/ultralytics)

---

## 📊 Dataset Overview

This repository provides a curated dataset for facial wrinkle detection tasks, formatted for YOLO-based object detection models. It includes high-quality facial images annotated with bounding boxes across 9 distinct wrinkle categories.

### Key Statistics

| Metric | Value |
|--------|-------|
| **Total Images** | 2,142 |
| **Total Label Files** | 2,142 |
| **Images Without Labels** | 0 |
| **Average Bounding Boxes per Image** | 16.95 |
| **Total Annotations** | ~36,308 |

### Class Distribution

| Class ID | Wrinkle Type | Count | Percentage |
|----------|--------------|-------|------------|
| 0 | `bunny_line` | 361 | 1.0% |
| 1 | `chin` | 1,237 | 3.4% |
| 2 | `crows_feet` | 6,016 | 16.6% |
| 3 | `forehead` | 11,015 | 30.3% |
| 4 | `frown_line` | 4,151 | 11.4% |
| 5 | `gummy_smile` | 7,970 | 22.0% |
| 6 | `masseter` | 2,976 | 8.2% |
| 7 | `sad_smile` | 2,253 | 6.2% |
| 8 | `smoker_lines` | 329 | 0.9% |

> 💡 **Note**: Class imbalance is present. Consider applying stratified sampling or class-weighted loss functions during training.

---

# ⚙️ Setup & Requirements

## Install Dependencies

```bash
pip install opencv-python numpy matplotlib
```
---

# 🛠️ Usage: Analysis & Visualization Scripts
1. Dataset Statistics (dataset_stats.py)
Generates comprehensive dataset analytics including class distribution, bounding box statistics, and visual histograms.
```bash
python scripts/dataset_stats.py
```
Outputs:
- Console summary of dataset metrics
- dataset_stats.png – Visual summary (class distribution, box-per-image histogram, box size distribution)

2. Annotation Visualization (visualize_detections.py)
Randomly samples images and overlays ground-truth bounding boxes with class labels for quality inspection.
```bash
python scripts/visualize_detections.py
```
Outputs:
- annotated_samples/annotated_*.jpg – High-resolution individual annotated images

---

## 🧪 Integration with YOLO Models
This dataset is ready-to-use with Ultralytics YOLOv8/v11:
1. Create a dataset.yaml configuration file:
```bash
path: ./facial-wrinkle-detection-dataset/data
train: train/images
val: train/images  # Update if validation split is added
nc: 9
names: ['bunny_line', 'chin', 'crows_feet', 'forehead', 'frown_line', 
        'gummy_smile', 'masseter', 'sad_smile', 'smoker_lines']
```  

2. Train with YOLOv8:
```bash
yolo detect model=yolov8n.pt data=dataset.yaml epochs=100 imgsz=640
```

---

# 📚 Citation

If you use this dataset in your research, citing this repository:

@misc{javad2026facialwrinkledataset,
  author = {Javad},
  title = {facial-wrinkle-detection-dataset},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/yourusername/facial-wrinkle-detection-dataset}
}

---

## ❓ Support & Contributing
We welcome community contributions! Please open an issue if you:
- 🐞 Discover annotation errors or inconsistencies  
- 💡 Suggest new preprocessing, augmentation, or evaluation scripts  
- 🔌 Need help integrating with YOLOv8/v11, Detectron2, or other frameworks  
- 📈 Want to contribute a validation/test split or additional metadata

---

### 📜 License
This dataset is released under the MIT License.
Note: Ensure compliance with any underlying image source licenses before commercial use.

    🧓📸 Good luck with your facial wrinkle detection research!
    For questions or collaboration inquiries, please open a GitHub issue or contact the maintainers.