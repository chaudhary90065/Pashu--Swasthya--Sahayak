import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# Page config
st.set_page_config(page_title="Pashu Swasthya Sahayak", page_icon="🐄", layout="centered")

# Load model (cached so it doesn't reload every time)
@st.cache_resource
def load_model():
    return YOLO('best.pt')  # best.pt isi folder mein honi chahiye

model = load_model()

# App title
st.title("🐄 Pashu Swasthya Sahayak")
st.write("Apne cattle ki photo upload karo aur Lumpy Skin Disease detect karo")

# File uploader
uploaded_file = st.file_uploader("Photo upload karo", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Check Health"):
        with st.spinner("Analyzing..."):
            results = model(image)
            result = results[0]

            if len(result.boxes) == 0:
                st.success("✅ Koi lumpy skin disease detect nahi hui. Animal healthy lag raha hai.")
            else:
                # Get highest confidence detection
                confidences = result.boxes.conf.tolist()
                max_conf = max(confidences)
                num_detections = len(confidences)

                # Simple severity logic based on confidence + number of detections
                if max_conf > 0.6 or num_detections >= 3:
                    severity = "🔴 Urgent"
                    advice = "Turant vet se sampark karein."
                elif max_conf > 0.4 or num_detections >= 2:
                    severity = "🟡 Moderate"
                    advice = "Agle 1-2 din mein vet ko dikhayein."
                else:
                    severity = "🟢 Mild"
                    advice = "Nazar rakhein, agar lakshan badhein to vet se milein."

                st.warning(f"⚠️ Lumpy Skin Disease detect hui!")
                st.write(f"**Severity:** {severity}")
                st.write(f"**Confidence:** {max_conf:.2%}")
                st.write(f"**Suggestion:** {advice}")

                # Show annotated image
                annotated = result.plot()
                st.image(annotated, caption="Detection Result", use_container_width=True)

st.markdown("---")
st.caption("Yeh ek AI-based prototype hai. Final diagnosis ke liye hamesha vet se sampark karein.")