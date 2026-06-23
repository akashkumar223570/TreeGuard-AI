import streamlit as st
import torch
import torch.nn as nn

from torchvision import models
from torchvision import transforms

from PIL import Image


# -----------------------------
# CONFIG
# -----------------------------

CLASS_NAMES = [
    "Tomato_Bacterial_spot",
    "Tomato_Late_blight",
    "Tomato_Leaf_Mold",
    "Tomato_Septoria_leaf_spot",
    "Tomato_healthy"
]


# -----------------------------
# LOAD MODEL
# -----------------------------

@st.cache_resource
def load_model():

    model = models.mobilenet_v2(
        weights=None
    )

    model.classifier = nn.Sequential(
        nn.Dropout(0.3),
        nn.Linear(
            model.last_channel,
            5
        )
    )

    model.load_state_dict(
        torch.load(
            "models/treeguard_model.pth",
            map_location="cpu"
        )
    )

    model.eval()

    return model


# -----------------------------
# IMAGE TRANSFORM
# -----------------------------

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])


# -----------------------------
# PREDICTION
# -----------------------------

def predict_image(image):

    model = load_model()

    image = image.convert("RGB")

    image = transform(image)

    image = image.unsqueeze(0)

    with torch.no_grad():

        outputs = model(image)

        probabilities = torch.softmax(
            outputs,
            dim=1
        )

        confidence, prediction = torch.max(
            probabilities,
            dim=1
        )

    disease = CLASS_NAMES[
        prediction.item()
    ]

    confidence = round(
        confidence.item() * 100,
        2
    )

    return disease, confidence