<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=32&pause=1000&color=2D9E47&center=true&vCenter=true&width=600&lines=🍃+TreeGuard+AI;Plant+Disease+Detection;Powered+by+Deep+Learning" alt="Typing SVG" />

# 🍃 TreeGuard AI
### AI-Powered Plant Disease Detection & Health Advisory System

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Groq](https://img.shields.io/badge/Groq_API-00A67E?style=for-the-badge&logo=groq&logoColor=white)](https://groq.com)
[![License](https://img.shields.io/badge/License-Educational-green?style=for-the-badge)](LICENSE)

> Upload a leaf photo → Get instant disease detection, treatment advice, PDF report & AI Doctor chat

</div>

---

## 📋 Table of Contents

| # | Section |
|---|---------|
| 1 | [🚨 Problem Statement](#-problem-statement) |
| 2 | [💡 Proposed Solution](#-proposed-solution) |
| 3 | [🌟 Key Features](#-key-features) |
| 4 | [🏗️ System Architecture](#%EF%B8%8F-system-architecture) |
| 5 | [⚙️ Technologies Used](#%EF%B8%8F-technologies-used) |
| 6 | [🧠 Model Development](#-model-development) |
| 7 | [📂 Dataset](#-dataset) |
| 8 | [🔬 Training Pipeline](#-training-pipeline) |
| 9 | [🎛️ Fine-Tuning](#%EF%B8%8F-fine-tuning) |
| 10 | [📈 Model Performance](#-model-performance) |
| 11 | [📸 Screenshots](#-screenshots) |
| 12 | [🚀 Installation](#-installation) |
| 13 | [📖 How to Use](#-how-to-use) |
| 14 | [🔮 Future Plans](#-future-plans) |
| 15 | [👨‍💻 Developer](#-developer) |

---

## 🚨 Problem Statement

> **Plant diseases cause 20–40% loss in global crop production every year.**

Farmers and plant owners face serious challenges every day:

| Problem | Impact |
|---------|--------|
| ❌ Hard to identify diseases in early stage | Disease spreads uncontrolled |
| ❌ No access to agricultural experts nearby | Wrong or no treatment applied |
| ❌ Incorrect treatment methods used | Wastes money and chemicals |
| ❌ Delayed diagnosis | Massive crop yield loss |
| ❌ Expensive laboratory testing required | Not affordable for small farmers |
| ❌ No 24/7 advisory service available | Farmers left without guidance |

Traditional disease diagnosis **requires expert knowledge, manual inspection, and is expensive and slow** — not suitable for millions of small-scale farmers.

---

## 💡 Proposed Solution

**TreeGuard AI** is an intelligent web application that uses **Deep Learning + AI** to solve this problem automatically.

The user simply uploads a leaf photo and the system does everything:

```
📷 Upload Leaf Photo
        ↓
🧠 AI Detects Disease (CNN Model)
        ↓
🎯 Confidence Score Calculated
        ↓
⚠️  Severity Level Assessed
        ↓
💊 Treatment & Prevention Provided
        ↓
🤖 AI Doctor Answers Follow-up Questions
        ↓
🔊 Voice Output + 📄 PDF Report Generated
```

**Result:** Any farmer anywhere can diagnose plant diseases in under 5 seconds — for free — without needing an expert.

---

## 🌟 Key Features

<table>
<tr>
<td width="50%">

### 🦠 Disease Detection
Detects multiple plant diseases from a single leaf image using a trained CNN model in under 5 seconds.

### 🎯 Confidence Score
Shows a percentage confidence level for every prediction so you know how reliable the result is.

### ⚠️ Severity Assessment
Automatically categorises disease severity as **Low / Medium / High Risk** based on confidence level.

### 💊 Treatment Suggestions
Provides actionable, disease-specific treatment plans including chemical and organic options.

### 🛡️ Prevention Tips
Suggests preventive measures to stop the disease from spreading or recurring in future.

</td>
<td width="50%">

### 🤖 AI Plant Doctor
Interactive chatbot powered by **Llama 3.3 70B** (via Groq API) for personalised plant-health Q&A.

### 🔊 Voice Assistant
Converts AI responses to speech using **Edge-TTS** — great for farmers who prefer listening.

### 📄 PDF Report
Generates a professional downloadable PDF with all results, treatments, and prevention info.

### 📊 Analytics Dashboard
Visual charts and statistics showing total scans, healthy rate, disease rate, and scan history.

### 🕒 Scan History
Saves all previous scans locally so you can track plant health over time.

</td>
</tr>
</table>

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        USER INTERFACE                        │
│              Streamlit Web App (HTML + CSS)                  │
└──────────────────────────┬──────────────────────────────────┘
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
   │  🧠 CNN     │  │ 🤖 Groq LLM │  │ 📊 Analytics│
   │  PyTorch    │  │ Llama 3.3   │  │  Plotly     │
   │  Model      │  │ AI Doctor   │  │  Dashboard  │
   └──────┬──────┘  └──────┬──────┘  └─────────────┘
          │                │
          ▼                ▼
   ┌─────────────┐  ┌─────────────┐
   │ ⚠️ Severity  │  │ 🔊 Edge-TTS │
   │  Analyser   │  │  Voice Out  │
   └──────┬──────┘  └─────────────┘
          │
          ▼
   ┌─────────────┐
   │ 📄 ReportLab│
   │  PDF Report │
   └─────────────┘
```

### Component Breakdown

| Layer | Tool | Purpose |
|-------|------|---------|
| 🖥️ Frontend | Streamlit + HTML/CSS | User interface, pages, chat, charts |
| 🧠 AI Model | CNN (PyTorch) | Classifies leaf image into disease categories |
| 💬 LLM | Llama 3.3 via Groq | AI Plant Doctor chatbot |
| 🔊 Voice | Edge-TTS | Converts text responses to MP3 audio |
| 📊 Charts | Plotly | Interactive visualisations |
| 📄 Report | ReportLab | Generates PDF documents |
| 💾 Storage | Local JSON | Saves past scan history |

---

## ⚙️ Technologies Used

### 🖥️ Frontend / UI
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)

### 🐍 Backend
![Python](https://img.shields.io/badge/Python_3.10+-3776AB?style=flat-square&logo=python&logoColor=white)

### 🧠 AI & Deep Learning
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![Groq](https://img.shields.io/badge/Groq_API-00A67E?style=flat-square)
![Llama](https://img.shields.io/badge/Llama_3.3_70B-7B2D8B?style=flat-square)

### 🖼️ Computer Vision
![Pillow](https://img.shields.io/badge/Pillow-3776AB?style=flat-square)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![torchvision](https://img.shields.io/badge/torchvision-EE4C2C?style=flat-square)

### 📊 Data & Visualisation
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)

### 📄 Reports & Voice
![ReportLab](https://img.shields.io/badge/ReportLab-PDF-red?style=flat-square)
![EdgeTTS](https://img.shields.io/badge/Edge--TTS-Voice-blue?style=flat-square)

---

## 🧠 Model Development

TreeGuard AI uses a **Convolutional Neural Network (CNN)** — a type of Deep Learning model specially designed to understand images.

### 🔍 What is a CNN? (Simple Explanation)

Think of a CNN like teaching a human eye to spot disease patterns, but at machine speed:

```
Raw Leaf Image
      ↓
Conv Layer 1 → Detects edges and colours
      ↓
Conv Layer 2 → Detects textures and patterns
      ↓
Conv Layer 3 → Detects disease-specific shapes
      ↓
Fully Connected → Classifies disease type
      ↓
Softmax Output → "Tomato Late Blight — 94.3%"
```

**Example thought process:**
> Detects "yellow spots" → recognises "pattern of spots on leaf edges" → concludes **"Bacterial Spot disease — 91% confidence"**

---

## 📂 Dataset

The model was trained on a plant disease image dataset containing **thousands of labelled leaf images** across multiple species and disease types.

### Disease Classes

| Icon | Disease | Description |
|------|---------|-------------|
| 🍅 | Tomato Bacterial Spot | Small dark spots with yellow rings |
| 🍅 | Tomato Late Blight | Water-soaked lesions turning brown/black |
| 🍅 | Tomato Leaf Mold | Pale spots on top, grey mould beneath |
| 🍅 | Tomato Septoria Leaf Spot | Small circular spots with dark brown borders |
| 🍅 | Tomato Early Blight | Dark brown spots with concentric rings |
| 🍎 | Apple Scab | Olive/black scabby patches on leaves |
| ⚫ | Black Rot | Dark circular lesions, fruit rot |
| 🌲 | Cedar Apple Rust | Bright orange spots on upper leaf surface |
| 🌫️ | Powdery Mildew | White powdery coating on leaf surface |
| 🌿 | Healthy Leaf | Normal healthy green leaf — no disease |

### Data Split Strategy

```
Total Dataset
├── 80% → Training Set   (model learns from this)
├── 10% → Validation Set (checks learning progress)
└── 10% → Test Set       (final honest evaluation)
```

> **Why split?** Splitting ensures the model is tested on images it has **never seen before**, giving a fair and honest performance score.

---

## 🔬 Training Pipeline

### Step-by-Step Training Process

**Step 1 — Load Dataset**
```python
dataset = ImageFolder("data/train", transform=transforms)
loader  = DataLoader(dataset, batch_size=32, shuffle=True)
```

**Step 2 — Image Preprocessing**
```python
transforms.Compose([
    transforms.Resize((224, 224)),   # Resize all images to same size
    transforms.ToTensor(),           # Convert to tensor
    transforms.Normalize(            # Normalise pixel values
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])
```

**Step 3 — Data Augmentation**
```python
transforms.Compose([
    transforms.RandomHorizontalFlip(),   # Randomly flip images
    transforms.RandomRotation(15),       # Random rotation ±15°
    transforms.ColorJitter(              # Adjust brightness/contrast
        brightness=0.3, contrast=0.3
    )
])
```
> Augmentation teaches the model to recognise diseases at different angles and lighting conditions.

**Step 4 — Training Loop**
```python
for epoch in range(num_epochs):
    model.train()
    for images, labels in train_loader:
        optimizer.zero_grad()           # Clear previous gradients
        outputs = model(images)         # Forward pass — make prediction
        loss = criterion(outputs, labels) # Calculate how wrong we are
        loss.backward()                  # Backpropagation
        optimizer.step()                 # Update model weights

    # Check on validation data each epoch
    val_acc = evaluate(model, val_loader)
    print(f"Epoch {epoch} | Val Accuracy: {val_acc:.2f}%")

    # Save the best model
    if val_acc > best_accuracy:
        torch.save(model.state_dict(), "best_model.pth")
        best_accuracy = val_acc
```

**Step 5 — Deploy for Prediction**
```python
model.load_state_dict(torch.load("best_model.pth"))
model.eval()

def predict_image(image):
    tensor = preprocess(image).unsqueeze(0)
    with torch.no_grad():
        output = model(tensor)
        prob   = torch.softmax(output, dim=1)
        confidence, predicted = torch.max(prob, 1)
    return class_names[predicted], round(confidence.item() * 100, 2)
```

---

## 🎛️ Fine-Tuning

Fine-tuning means taking the trained model and making it **smarter and more accurate** through careful adjustments.

> **Simple Analogy:** Like taking a student who already knows biology and giving them extra focused lessons specifically about plant diseases.

### Techniques Used

#### 1️⃣ Learning Rate Optimisation
```python
# Start with a base learning rate
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Reduce learning rate when improvement plateaus
scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
    optimizer, mode='max', factor=0.5, patience=3
)
```
> Too large LR → model overshoots optimal weights  
> Too small LR → training is very slow  
> Scheduler → adjusts it automatically 🎯

#### 2️⃣ Early Stopping
```python
patience = 5        # Stop if no improvement for 5 epochs
best_val_acc = 0
no_improve_count = 0

for epoch in range(100):
    val_acc = evaluate(model, val_loader)
    if val_acc > best_val_acc:
        best_val_acc = val_acc
        no_improve_count = 0
        torch.save(model.state_dict(), "best_model.pth")
    else:
        no_improve_count += 1
        if no_improve_count >= patience:
            print("Early stopping triggered!")
            break
```

#### 3️⃣ Transfer Learning
```python
# Load a pre-trained model (already knows shapes, textures, edges)
model = torchvision.models.resnet50(pretrained=True)

# Freeze base layers — keep their knowledge
for param in model.parameters():
    param.requires_grad = False

# Only train the final classification layer for our diseases
model.fc = nn.Linear(model.fc.in_features, num_classes)
```

> **Why Transfer Learning?**  
> Instead of training from scratch on millions of images, we use a model that already understands image features — and only teach it the last step (disease classification). This is **faster, cheaper, and more accurate**.

#### 4️⃣ Weight Optimisation with Adam
```python
# Adam optimizer adapts learning rate for each weight individually
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001,
    weight_decay=1e-4  # L2 regularisation to prevent overfitting
)
```

---

## 📈 Model Performance

Performance is measured on the **test set** — images the model has **never seen** during training.

| Metric | Score | What It Means |
|--------|-------|---------------|
| ✅ **Accuracy** | `XX%` | Out of 100 images, how many were classified correctly |
| 🎯 **Precision** | `XX%` | When model says "disease X", how often is it correct |
| 🔍 **Recall** | `XX%` | Out of all actual disease cases, how many did model catch |
| ⚖️ **F1 Score** | `XX%` | Balanced score combining Precision and Recall |

> 📝 **Replace `XX%`** with your actual training results.  
> A score above **85%** is considered excellent for multi-class plant disease detection.

### Confusion Matrix (Example)

```
              Predicted
              Healthy  Bacterial  Late Blight  Leaf Mold
Actual  Healthy   [95]      [2]         [2]        [1]
   Bacterial      [3]      [91]         [4]        [2]
  Late Blight     [1]       [3]        [93]        [3]
    Leaf Mold     [2]       [2]         [2]       [94]
```

---

## 📸 Screenshots

### 🏠 Home Page — Upload & Detect
> *(Add your screenshot: `assets/screenshots/home.png`)*

```
[ Screenshot Placeholder ]
Upload leaf image → Click "Analyze Leaf" → Get instant results
```

### 🦠 Detection Result
> *(Add your screenshot: `assets/screenshots/result.png`)*

```
[ Screenshot Placeholder ]
Disease Name | Confidence % | Risk Level | Download PDF
```

### 🤖 AI Doctor Chat
> *(Add your screenshot: `assets/screenshots/ai_doctor.png`)*

```
[ Screenshot Placeholder ]
Ask any plant health question → Get AI-powered answers → Hear response as voice
```

### 📊 Analytics Dashboard
> *(Add your screenshot: `assets/screenshots/analytics.png`)*

```
[ Screenshot Placeholder ]
Total Scans | Healthy Rate | Disease Rate | Pie Chart | History
```

> 💡 **Tip:** Replace the placeholders above with:
> ```markdown
> ![Home Page](assets/screenshots/home.png)
> ```

---

## 🚀 Installation

### Prerequisites
- Python `3.10` or higher
- `pip` package manager
- Groq API Key (free at [groq.com](https://groq.com))

### Step 1 — Clone the Repository
```bash
git clone https://github.com/akashkumar223570/TreeGuard-AI.git
cd TreeGuard-AI
```

### Step 2 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Add Your API Key
Create `.streamlit/secrets.toml` and add:
```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

### Step 4 — Run the App
```bash
streamlit run app.py
```

Open your browser at **`http://localhost:8501`** 🎉

---

## 📖 How to Use

| Step | Action | Description |
|------|--------|-------------|
| 1️⃣ | **Upload Image** | Go to Home page → click "Upload Leaf Image" → select JPG/PNG photo |
| 2️⃣ | **Analyse** | Click **"Analyze Leaf"** button and wait 2–5 seconds |
| 3️⃣ | **Read Results** | View disease name, confidence %, risk level, treatment & prevention |
| 4️⃣ | **Download Report** | Click **"Download PDF"** to save a full report |
| 5️⃣ | **Ask AI Doctor** | Go to AI Doctor page → ask follow-up questions in natural language |
| 6️⃣ | **Track History** | Visit Analytics page to see all past scans and visual statistics |

### 💬 AI Doctor Tips
- Use quick-action buttons: `💊 Treatment` · `🛡 Prevention` · `⏳ Recovery` · `🌱 Organic`
- For general questions (not about the scanned plant) start your message with `/`
- Click **"🔊 Hear AI Doctor"** to listen to the response as audio

---

## 🔮 Future Plans

- [ ] 📱 **Mobile Application** — Native Android & iOS app with camera integration
- [ ] 🌿 **More Plant Species** — Expand to 50+ plants including wheat, rice, corn, grapes
- [ ] 📷 **Real-Time Camera Detection** — Live detection without uploading a file
- [ ] 🌍 **Multi-Language Support** — Hindi, Tamil, Punjabi and other regional languages
- [ ] 📅 **Disease Progression Prediction** — Predict how fast a disease will spread
- [ ] ☁️ **Cloud Database** — Store scan history across devices and locations
- [ ] 🗺️ **Disease Heatmap** — Regional map showing disease outbreaks by location
- [ ] 🔔 **Alert System** — Notify farmers when high-risk diseases are detected in their area

---

## 👨‍💻 Developer

<div align="center">

**Akash Kumar**  
B.Tech Student | AI & Data Science Enthusiast

[![GitHub](https://img.shields.io/badge/GitHub-akashkumar223570-181717?style=for-the-badge&logo=github)](https://github.com/akashkumar223570)

</div>

---

## 📜 License

This project is developed for **educational and research purposes**.

---

<div align="center">

Made with ❤️ using **Streamlit + PyTorch**

🌿 Powered by **TreeGuard AI** · 🤖 LLM by **Groq + Llama 3.3** · 📄 Reports by **ReportLab**

⭐ If this project helped you, please give it a star on GitHub!

</div>
