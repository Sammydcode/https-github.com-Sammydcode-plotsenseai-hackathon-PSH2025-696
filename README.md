# Credit Card Transaction Anomaly Detector

**USER ID:** PSH2025-696

---

## Project Description
This project, **Credit Card Transaction Anomaly Detector**, is a hybrid AI-powered system designed to detect suspicious or fraudulent credit card transactions in real time.

It combines:
- **Rule-based logic** (simple financial thresholds and risk conditions)
- **Machine learning (Isolation Forest)** for anomaly detection
- **PlotSenseAI integration** for intelligent visualization and automated insights

Users can input key transaction details such as **Amount** and **Transaction Speed**, and the system evaluates the risk level — determining whether the transaction is *legit* or *suspicious* .  

This project was developed as part of the **PlotSense AI Hackathon**, showcasing both **ML (EDA-focused)** and **Dev (extension module)** contributions.

---

## Tech Stack Used
| Category | Tools / Libraries |
|-----------|-------------------|
| Frontend / UI | Streamlit |
| Machine Learning | scikit-learn (Isolation Forest) |
| Visualization | Matplotlib, PlotSenseAI |
| Utilities | Pandas, Joblib, OS |
| Language | Python 3.10+ |

---

## Setup Instructions

### 1️⃣ Clone this repository
```bash
git clone https://github.com/YOUR_USERNAME/plotsenseai-hackathon--PSH2025-696-.git
cd plotsenseai-hackathon--PSH2025-696-
```
### 2️⃣ Install dependencies

Make sure Python 3.10+ is installed, then run:
```bash
pip install -r requirements.txt
```

If you don’t have a requirements.txt file yet, create one automatically by running:
```bash
pip freeze > requirements.txt
```

### 3️⃣ Download datasets

The project uses two datasets:

- Raw dataset

- Preprocessed dataset

You can download them from Google Drive:

- Raw dataset: [https://drive.google.com/file/d/1vBYfrHlbqbaCmixBFdSxU_jR5o9ElFF0/view?usp=drive_link]

- Preprocessed dataset: [https://drive.google.com/file/d/1I7sTD3zthe1nLJq6GKchSNQiX6DWstxN/view?usp=drive_link]

Place both files in the same folder as app.py.

4️⃣ Set PlotSense API Key

Before running the app, make sure your PlotSense API key is set as an environment variable:

Windows:
```bash
setx GROQ_API_KEY "your_actual_groq_key_here"
```

macOS / Linux:
```bash
export GROQ_API_KEY="your_actual_groq_key_here"
```

5️⃣ Run the app locally
```bash
streamlit run app.py
```

Open the URL shown in your terminal e.g., ```http://localhost:8501``` to access the app.

## Team Members & Roles

- **Samuel Osaruonamen Amadasun** — Data Scientist / Developer

> *Project built and documented by Samuel with support from AI tools (ChatGPT, OpenAI GPT-5) for brainstorming and technical refinement.*


## Video Demo

Watch the demo here:

[https://youtu.be/RMOajjFoLQE]

## Social Media Post

Check out my hackathon submission post:

🔗 LinkedIn/Twitter Post


