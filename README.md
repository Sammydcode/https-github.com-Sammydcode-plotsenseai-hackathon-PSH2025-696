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

## ⚙️ Setup Instructions

### 1️⃣ Clone this repository
```bash
https://github.com/Sammydcode/plotsenseai-hackathon--PSH2025-696-.git
cd plotsenseai-hackathon--PSH2025-696-
```
### 2️⃣ Install dependencies

Make sure Python 3.10+ is installed, then run:

```bash
pip install -r requirements.txt
```

If you don’t have a requirements.txt file yet, create one automatically by running this:

```bash
pip freeze > requirements.txt
```

### 3️⃣ Run the app locally
```bash
streamlit run app.py
```

Then open the URL shown in your terminal, e.g. ```http://localhost:8501.```


**Notes:**

- Ensure the file isolation_forest_model.pkl and your dataset (e.g. preprocessed_data.csv) are in the same folder as app.py.

- Make sure your PlotSense API key is set as an environment variable using:

```bash
setx GROQ_API_KEY "your_actual_groq_key_here"
```

(on Windows) or

```bash
export GROQ_API_KEY="your_actual_groq_key_here"
```

(on macOS/Linux)


## Team Members & Roles

- **Samuel Osaruonamen Amadasun** — Data Scientist / Developer

> *Project built and documented by Samuel with support from AI tools (ChatGPT, OpenAI GPT-5) for brainstorming and technical refinement.*


## Video Demo

Watch the demo here:

Demo Video Link

## Social Media Post

Check out my hackathon submission post:

🔗 LinkedIn/Twitter Post


