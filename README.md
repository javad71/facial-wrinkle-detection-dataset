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

### YOLO Label Format
Each `.txt` label file contains one bounding box per line:
<class_id> <x_center> <y_center> <width> <height>

- All values are normalized to [0, 1] relative to image dimensions
- Coordinates refer to the bounding box center and dimensions

---

## ⚙️ Setup & Requirements

### Install Dependencies
```bash
pip install -r requirements.txt
# Or manually:
pip install opencv-python numpy matplotlib

# Requirements File (requirements.txt)

opencv-python>=4.5.0
numpy>=1.21.0
matplotlib>=3.4.0

## 🛠️ Usage: Analysis & Visualization Scripts

1. Dataset Statistics (dataset_stats.py)
Generates comprehensive dataset analytics including class distribution, bounding box statistics, and visual histograms.

python scripts/dataset_stats.py

### Outputs:

    Console summary of dataset metrics
    dataset_stats.png – Visual summary (class distribution, box-per-image histogram, box size distribution)

2. Annotation Visualization (visualize_detections.py)
Randomly samples images and overlays ground-truth bounding boxes with class labels for quality inspection.

python scripts/visualize_detections.py

Outputs:

    sample_detections.png – Combined preview of 5 annotated samples
    annotated_samples/annotated_*.jpg – High-resolution individual annotated images