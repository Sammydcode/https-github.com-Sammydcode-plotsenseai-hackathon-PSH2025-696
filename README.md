# Credit Card Transaction Anomaly-Detector

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
git clone https://github.com/YOUR_USERNAME/plotsenseai-hackathon-PSH2025-696.git
cd plotsenseai-hackathon-PSH2025-696
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

### 4️⃣ Set PlotSense API Key

To use this project, you’ll need an API key from Grocq.
Follow the steps below:

- Get your API key

- Go to the Grocq website.

- Sign in or create an account.

- Navigate to your Developer Settings → API Keys section.

- Copy your secret API key.

- Create a .env file in the root directory of your project.
```This file will securely store your key so it doesn’t appear in your public code.```

- Add your API key to the .env file like this:

```bash
GROCQ_API_KEY=your_actual_api_key_here
```
**Important Notes:**
   - Do **not** include spaces around the `=` sign.  
     Correct: `GROCQ_API_KEY=123456789abcdef`  
     Wrong: `GROCQ_API_KEY = 123456789abcdef`
   - Do **not** use quotes around your key.  
     Correct: `GROCQ_API_KEY=123456789abcdef`  
     Wrong: `GROCQ_API_KEY="123456789abcdef"`

### 5️⃣ Run the app locally

```bash
streamlit run app.py
```

Open the URL shown in your terminal e.g., ```http://localhost:8501``` to access the app.

## Team Members & Roles

- **Samuel Osaruonamen Amadasun** — Data Scientist / Developer

> *Project built and documented by Samuel with support from AI tools (ChatGPT, OpenAI GPT-5) for brainstorming and technical refinement.*


## Video Demo

Watch the demo here:

[![Watch the video](https://img.youtube.com/vi/<RMOajjFoLQE>/0.jpg)](https://youtu.be/RMOajjFoLQE)
[https://youtu.be/RMOajjFoLQE]

## Social Media Post

Check out my hackathon submission post:

X: [https://x.com/AmadasunSamuel/status/1978257583031861659]

Linkedin: [https://www.linkedin.com/posts/samuel-amadasun-273109374_plotsenseai-machinelearning-datascience-activity-7384032648316301312-PAO9?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFyQijcBOtjr9cATdbDv6OPKJ5K2M68eHjQ]


