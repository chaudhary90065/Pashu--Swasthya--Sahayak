
[Click here to tr# 🐄 Pashu Swasthya Sahayak

**AI-powered livestock health detector for farmers**

Pashu Swasthya Sahayak is a computer vision system that helps farmers detect Lumpy Skin Disease (LSD) in cattle early by analyzing uploaded photos. Built with YOLOv8 for object detection and deployed as a Streamlit web app, it identifies visible skin lesions, estimates severity, and provides actionable guidance — addressing the real-world problem of delayed veterinary diagnosis in rural farming communities.

## 🔍 The Problem

Animals can't tell farmers when they're sick. By the time visible symptoms are noticed and a vet is consulted, diseases like Lumpy Skin Disease — which caused massive cattle losses across India in recent outbreaks — are often already advanced. This delay leads to increased mortality, reduced milk/meat yield, and financial distress for farmers.

## ✅ The Solution

A farmer takes a photo of their cattle on a phone → uploads it to the app → the model detects visible lesions and returns:
- Whether LSD is detected
- A severity level (Mild / Moderate / Urgent)
- A plain-language recommendation on next steps

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Object Detection Model | YOLOv8 (Ultralytics) |
| Image Processing | OpenCV |
| Web App / Interface | Streamlit |
| Dataset | Roboflow (Cattle Diseases — SLIIT) |
| Training | Kaggle Notebooks (GPU) |
| Deployment | Streamlit Community Cloud |

## 📊 Model Performance

- **mAP50:** ~0.436
- **mAP50-95:** ~0.243
- **Precision:** ~0.583
- **Recall:** ~0.418
- Trained for 70 epochs on a single-class (Lumpy Skin Disease) object detection dataset.

## 🚀 Live Demo

Pashu Swasthya Sahayak](https://pashu--swasthya--sahayak-qs3qcd9zdcsniaydauzu3t.streamlit.app/)

## 📁 Project Structure

```
pashu-swasthya-app/
├── app.py              # Streamlit app
├── best.pt              # Trained YOLOv8 model weights
├── requirements.txt      # Python dependencies
├── packages.txt          # System-level dependencies for cloud deployment
└── README.md
```

## 💻 Run Locally

```bash
git clone https://github.com/chaudhary90065/Pashu--Swasthya--Sahayak.git
cd Pashu--Swasthya--Sahayak
pip install -r requirements.txt
streamlit run app.py
```

## 🔮 Future Scope

- [ ] Multi-class disease detection (FMD, Mastitis, Ringworm, etc.)
- [ ] Multilingual support (Hindi, regional languages)
- [ ] Audio output for results (text-to-speech)
- [ ] Phone number + OTP-based farmer login
- [ ] WhatsApp bot integration for wider accessibility
- [ ] Behavior/posture-based detection for internal conditions (bloat, discomfort)

## 👩‍💻 Author

**Shambhavi Chaudhary**
B.Tech CSE, GITA Autonomous College
[LinkedIn](https://linkedin.com/in/shambhavi-chaudhary-baa8892a3) · [GitHub](https://github.com/chaudhary90065)

## 📄 License

This project is for educational and portfolio purposes.
