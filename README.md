# Helmet Detection & Electronic Challan System

> **An intelligent automated system for detecting motorcycle helmet violations and generating electronic challans using advanced computer vision.**

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Usage](#usage)
- [Development Roadmap](#development-roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

---

## 🎯 Overview

The **Helmet Detection & Electronic Challan System** is a comprehensive traffic management solution that leverages cutting-edge YOLOv8 object detection and OpenCV image processing to automatically identify motorcycle riders without helmets. The system captures evidence, logs violations, and is architected for seamless integration with notification systems (SMS/Email), database backends, and automated challan generation in subsequent phases.

**Key Highlights:**
- Real-time helmet detection using YOLOv8 neural networks
- Automatic violation detection and evidence capture
- Intelligent cooldown mechanism to minimize false positives
- Modular, production-ready code architecture
- Scalable design for future enhancements

---

## ✨ Features

### Currently Implemented
- ✅ **Person Detection** - Robust person detection using YOLOv8
- ✅ **Helmet Detection** - Multi-model support (placeholder and pretrained models)
- ✅ **Violation Logging** - Automatic capture and storage of violation evidence
- ✅ **Cooldown System** - Prevents repeated alerts for the same violation
- ✅ **Frame Annotation** - Visual "NO HELMET" labels on detected violations
- ✅ **Evidence Management** - Organized storage of violation images
- ✅ **Modular Architecture** - Clean, maintainable codebase with separation of concerns

### Planned Features (Roadmap)
- 🔜 Database integration for violation logging
- 🔜 SMS/Email notification system
- 🔜 Automated electronic challan generation
- 🔜 Web-based violation management dashboard
- 🔜 License plate recognition integration

---

## 📦 Requirements

### System Requirements
- **Python:** 3.9 or higher (tested on 3.11+)
- **Operating System:** Windows, macOS, or Linux
- **RAM:** Minimum 4GB (8GB+ recommended)
- **GPU:** Optional (CUDA-capable GPU recommended for real-time processing)

### Python Dependencies
All required packages are listed in `requirements.txt`. Key dependencies include:
- **OpenCV (cv2)** - Computer vision and image processing
- **YOLOv8** - Object detection framework
- **NumPy** - Numerical computing
- **Pillow** - Image handling

---

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd helmet_challan_system
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the Helmet Detection Model
Download a YOLOv8 helmet detection model and place it in the `models/` directory:

```bash
# Create models directory if it doesn't exist
mkdir models

# Download pretrained model (or use your own)
# Place the model file at: models/helmet_model.pt
```

**Model Options:**
- Use a pretrained YOLO helmet detection model for production
- Alternatively, start with `yolov8n.pt` (nano model) for development

### 5. Verify Installation
```bash
python test_camera.py
```

This script verifies that your camera is functioning correctly before running the main system.

---

## 📂 Project Structure

```
helmet_challan_system/
│
├── app/
│   ├── main.py                    # Main application entry point
│   ├── config.py                  # Configuration settings
│   ├── challan/                   # Challan generation module (planned)
│   ├── database/                  # Database integration module (planned)
│   ├── detection/
│   │   ├── helmet_detector.py     # Helmet detection logic
│   │   └── __pycache__/
│   ├── notifications/             # Notification system (planned)
│   └── utils/                     # Utility functions
│
├── data/
│   └── evidence_images/           # Evidence image storage
│
├── models/
│   └── helmet_model.pt            # Pretrained YOLOv8 helmet detection model
│
├── violations/                    # Captured violation images and logs
│
├── requirements.txt               # Python dependencies
├── test_camera.py                 # Camera testing utility
├── yolov8n.pt                     # YOLOv8 nano model (optional)
├── README.md                      # This file
└── .gitignore                     # Git ignore rules
```

---

## ⚙️ Configuration

Edit `app/config.py` to customize system behavior:

```python
# Model configuration
MODEL_PATH = "models/helmet_model.pt"
CONFIDENCE_THRESHOLD = 0.5

# Detection settings
COOLDOWN_SECONDS = 5              # Prevent repeated alerts
FRAME_WIDTH = 1280
FRAME_HEIGHT = 720

# Output paths
VIOLATIONS_DIR = "violations/"
EVIDENCE_DIR = "data/evidence_images/"
```

---

## 💻 Usage

### Start the Detection System
```bash
python app/main.py
```

### Controls
| Key | Action |
|-----|--------|
| `q` | Quit the application |
| `s` | Save current frame as evidence |
| `p` | Pause/Resume detection |

### Output
- **Console:** Detection results and violation logs
- **Violations Folder:** Evidence images with timestamps
- **Log Files:** Detailed violation records for database integration

---

## 🗺️ Development Roadmap

### Phase 1: Core Detection (✅ Complete)
- Real-time helmet detection
- Violation capture and evidence storage

### Phase 2: Data Management (🔄 In Progress)
- Database schema for violations
- Structured violation logging

### Phase 3: Notifications (📋 Planned)
- SMS alert integration
- Email notifications
- Push notifications

### Phase 4: Challan Generation (📋 Planned)
- Automated challan creation
- Fine calculation
- Document generation

### Phase 5: Management Dashboard (📋 Planned)
- Web-based violation management
- Real-time monitoring
- Analytics and reporting

---

## 🔧 Development Notes

### Performance Optimization
- Recommended use of YOLOv8 nano model (`yolov8n.pt`) for real-time processing on standard hardware
- GPU acceleration is optional but highly recommended for multi-stream processing
- Adjust confidence thresholds based on your environment and accuracy requirements

### Troubleshooting

| Issue | Solution |
|-------|----------|
| Camera not detected | Ensure no other application is using the camera; restart the system |
| Slow detection | Reduce frame resolution in `config.py` or use a smaller model |
| Model not found | Verify `helmet_model.pt` exists in the `models/` directory |
| Low accuracy | Retrain model with domain-specific data or adjust confidence threshold |

### Testing
```bash
# Test camera functionality
python test_camera.py

# Run with debug mode (if configured)
python app/main.py --debug
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Commit changes: `git commit -m "Add your feature"`
3. Push to branch: `git push origin feature/your-feature`
4. Submit a pull request

**Current Development Branch:** `feature/helmet-logic`

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

---

## 📞 Support

For issues, questions, or suggestions:

- **Issues:** Create a GitHub issue with detailed description
- **Documentation:** Refer to inline code comments
- **Contact:** [Your contact information]

---

**Last Updated:** February 2026  
**Version:** 1.0.0 (Beta)
We will be working on improvements....

