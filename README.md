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

---

# 📚 Citation
dkfsdbfvs
---