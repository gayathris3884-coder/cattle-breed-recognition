# 🐄 PashuPehchan - Cattle & Buffalo Breed Recognition

An AI-powered deep learning system that automatically identifies Indian cattle and buffalo breeds using MobileNetV2 transfer learning and TensorFlow.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13%2B-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🎯 Features

- **Automatic Breed Classification** - Identifies 9 Indian cattle and buffalo breeds with high accuracy
- **MobileNetV2 Transfer Learning** - Efficient model suitable for production deployment
- **Web Interface** - Beautiful Streamlit application with modern UI
- **Real-time Predictions** - Upload an image and get instant breed identification
- **Confidence Scores** - Displays confidence levels for predictions
- **Breed Information** - Detailed information about each breed including origin, milk yield, and characteristics
- **Mobile Friendly** - Responsive design works on desktop and mobile devices

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| **Training Accuracy** | 82.5% |
| **Validation Accuracy** | 75.92% |
| **Test Accuracy** | 72.0% |
| **Total Training Images** | 1,997 |
| **Supported Breeds** | 9 |
| **Model Size** | ~90 MB |
| **Architecture** | MobileNetV2 |
| **Framework** | TensorFlow/Keras |

---

## 🐄 Supported Breeds

### Indigenous Cattle
1. **Gir** - Dairy breed from Gir Forest, Gujarat (6-8 L/day)
2. **Sahiwal** - Premium dairy breed from Punjab (8-12 L/day)
3. **Red Sindhi** - Tick-resistant breed from Sindh (5-7 L/day)
4. **Tharparkar** - Drought-hardy breed from Rajasthan (4-6 L/day)

### Exotic Cattle
5. **Holstein Friesian** - High-yield dairy breed (20-30 L/day)
6. **Jersey** - Premium butterfat milk breed (12-18 L/day)

### Buffalo
7. **Murrah** - High milk-yielding buffalo from Haryana (10-16 L/day)
8. **Jaffrabadi** - Largest buffalo breed from Gujarat (8-12 L/day)
9. **Nili Ravi** - High-fat milk buffalo from Punjab (9-14 L/day)

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/cattle-breed-recognition.git
cd cattle-breed-recognition
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Web Application
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 📁 Project Structure

```
cattle-breed-recognition/
│
├── app.py                      # Main Streamlit web application
├── train.py                    # Model training script
├── fine_tune.py               # Fine-tuning script
├── evaluate.py                # Model evaluation script
├── predict.py                 # Single image prediction
│
├── models/
│   ├── best_model.keras       # Best model checkpoint
│   └── fine_tuned_model.keras # Final fine-tuned model
│
├── dataset/                   # (Not included, download from source)
│   ├── train/
│   ├── valid/
│   └── test/
│
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── .gitignore                # Git ignore file
│
└── screenshots/              # Demo screenshots
    ├── app_demo.png
    └── prediction_result.png
```

---

## 🛠️ Usage

### Web Application (Recommended)
```bash
streamlit run app.py
```
- Upload cattle/buffalo images
- Get instant breed predictions
- View confidence scores
- Browse breed directory

### Command Line Prediction
```bash
python predict.py --image path/to/image.jpg
```

### Training Your Own Model
```bash
python train.py --epochs 50 --batch_size 32
```

### Evaluate Model
```bash
python evaluate.py
```

---

## 💻 Technology Stack

| Component | Technology |
|-----------|-----------|
| **Deep Learning** | TensorFlow 2.13+ |
| **Model Architecture** | MobileNetV2 |
| **Web Framework** | Streamlit |
| **Image Processing** | Pillow, OpenCV |
| **Data Science** | NumPy, Pandas, Scikit-learn |
| **Visualization** | Matplotlib |

---

## 📥 Dataset

The model is trained on the **Indian Bovine Breeds Dataset** from Roboflow.

### Download Dataset
```bash
# From Roboflow (requires account)
# Download and extract to ./dataset folder
```

**Dataset Details:**
- Total Images: ~2,000
- Breeds: 9
- Split: Train (60%) / Validation (20%) / Test (20%)
- Image Size: 224x224 pixels
- Format: JPG

## 🎓 Model Training Details

### Architecture
- **Base Model**: MobileNetV2 (pre-trained on ImageNet)
- **Custom Layers**: Global Average Pooling → Dense(512) → Dropout(0.3) → Dense(9)
- **Activation**: ReLU (hidden), Softmax (output)
- **Loss Function**: Categorical Crossentropy
- **Optimizer**: Adam (lr=0.001)

### Data Augmentation
- Random rotation (±20°)
- Random zoom (0.8-1.2x)
- Random horizontal flip
- Random brightness/contrast adjustment

### Training Configuration
```python
Epochs: 50
Batch Size: 32
Initial LR: 0.001
LR Scheduler: ReduceLROnPlateau
Early Stopping: Patience=10
```

---

## � Screenshots

### 🏠 Application Home - Modern UI with Gradient Header
![App Home](https://via.placeholder.com/1200x400?text=PashuPehchan+Home+Screen)
- Beautiful blue gradient header with animations
- Upload area with drag-and-drop support
- Model information card
- Breed directory browser

### 🎯 Prediction Result - 99.1% Confidence
![Prediction Result](https://via.placeholder.com/1200x600?text=Prediction+Result+Example)
- High-confidence breed prediction
- Real-time image display
- Detailed breed information (origin, milk yield, ICAR code)
- Characteristics description
- Progress bar with confidence visualization

### 📚 Breed Directory - Browse All 9 Breeds
![Breed Directory](https://via.placeholder.com/600x400?text=Breed+Directory)
- Filter by cattle type (Indigenous/Exotic/Buffalo)
- Breed origin and classification
- Color-coded tags for quick identification

---

### Training Metrics
```
✅ Training Accuracy: 82.5%
✅ Validation Accuracy: 75.92%
✅ Test Accuracy: 72.0%
✅ Model Size: ~90 MB
```

### Confusion Matrix Analysis
- Highest accuracy: Murrah (96% precision)
- Most confused breeds: Nili Ravi ↔ Jaffrabadi (buffalo breeds)

### Inference Time
- Average prediction time: ~200ms per image
- Suitable for real-time applications

---

## 🎨 Modern UI/UX Features

The Streamlit app includes:
- 🎨 Modern dark theme with gradients
- ⚡ Smooth animations and transitions
- 📱 Responsive design
- 🎯 Real-time predictions
- 📊 Confidence visualization
- 📚 Breed information cards
- 🔍 Breed directory browser

---

## 📝 Model Files

### `best_model.keras`
- Best performing model during training
- Saved at peak validation accuracy
- Size: ~90 MB

### `fine_tuned_model.keras`
- Final fine-tuned model (used in production)
- Better generalization on test set
- Size: ~90 MB

---

## 🔍 How It Works

1. **Image Upload** → User uploads a cattle/buffalo image
2. **Preprocessing** → Image resized to 224×224 and normalized
3. **Feature Extraction** → MobileNetV2 backbone extracts features
4. **Classification** → Custom dense layers predict breed
5. **Post-processing** → Confidence scores calculated and displayed
6. **Results** → Breed name, category, confidence, and information shown

---

## 🚨 Limitations

- Model trained on Indian breeds only
- Performance may vary with different lighting/angles
- Best results with clear, well-lit images
- May struggle with mixed breed or unclear images

---

## 📄 Requirements

```
tensorflow>=2.13.0
numpy>=1.24.0
pillow>=10.0.0
streamlit>=1.28.0
pandas>=2.0.0
scikit-learn>=1.3.0
matplotlib>=3.7.0
opencv-python>=4.8.0
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Add new breeds
- Improve documentation

---

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourUsername)
- Email: gaya

---

## 🙏 Acknowledgments

- Dataset: Roboflow Indian Bovine Breeds Dataset
- Architecture: MobileNetV2 (Google)
- Framework: TensorFlow & Streamlit
- Inspiration: Agricultural AI for livestock management

---

## 📞 Support

If you encounter any issues:
1. Check existing GitHub Issues
2. Review the troubleshooting section below
3. Create a new Issue with details

### Troubleshooting

**Issue: Model not found**
```
Solution: Ensure models/ folder contains fine_tuned_model.keras
```

**Issue: High memory usage**
```
Solution: Reduce batch size or use smaller input images
```

**Issue: Slow predictions**
```
Solution: Use GPU acceleration or optimize model with TensorFlow Lite
```

---

## 🎯 Future Improvements

- [ ] Add more breeds (Pan-Asian)
- [ ] Model optimization with TensorFlow Lite
- [ ] Mobile app with Flutter
- [ ] Real-time video prediction
- [ ] Multi-model ensemble
- [ ] API deployment with FastAPI
- [ ] Cloud deployment (AWS/GCP)

---

**Made with ❤️ for agricultural AI**

---

## 📸 How to Add Real Screenshots

Replace placeholder images in README with actual screenshots:

### Capture Screenshot 1: Home Screen
```bash
# Run app and take screenshot of home page
streamlit run app.py
# Screenshot: Full page (with sidebar and main area)
# Save as: screenshots/01_app_home.png
```

### Capture Screenshot 2: Prediction Result
```bash
# Upload any cattle/buffalo image
# Screenshot: Prediction result with 99%+ confidence
# Save as: screenshots/02_prediction_result.png
```

### Capture Screenshot 3: Breed Directory
```bash
# Click "Browse all breeds" expander
# Screenshot: Breed directory expanded
# Save as: screenshots/03_breed_directory.png
```

Then update README image URLs to:
```markdown
![App Home](screenshots/01_app_home.png)
![Prediction](screenshots/02_prediction_result.png)
![Directory](screenshots/03_breed_directory.png)
```

---

## 🏷️ GitHub Topics & Badges

Add to your repository settings:

**Topics:**
- machine-learning
- tensorflow
- deep-learning
- computer-vision
- streamlit
- cattle-classification
- agriculture-ai
- image-classification
- transfer-learning

**Badges to add to README:**
```markdown
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13%2B-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![License](https://img.shields.io/badge/License-MIT-green)
```
