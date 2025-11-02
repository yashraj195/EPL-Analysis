# ⚽ EPL Match Predictor

A simple web application that predicts the outcome of English Premier League (EPL) matches using a trained Machine Learning model.  
Built with **Flask (Python)** for the backend and deployed using **Vercel** (frontend) + **Hugging Face Spaces / Render** (for model hosting).

---

## 🚀 Live Demo

🔗 **Frontend (Vercel):** [https://epl-predictor.vercel.app](https://epl-predictor.vercel.app)  

---

## 🧠 About the Project

This app predicts the result of an EPL match (Win/Draw/Loss) based on input features such as:
- Home and Away Team
- Form statistics
- Goals scored / conceded
- Possession, shots, passes, and other match stats

The backend uses a trained **Random Forest Classifier** (stored as `model.pkl`), while the frontend provides a clean and modern user interface to make predictions instantly.

---

## 🧩 Tech Stack

**Frontend (Vercel)**
- HTML5, CSS3, JavaScript
- Responsive UI Design
- Hosted on [Vercel](https://vercel.com)

**Backend (API)**
- Python, Flask
- scikit-learn, pandas, numpy
  

---

## Project Structure
epl-analysis/ model.pkl
├── app.py
├── requirements.txt
└── templates/
    ├── index.html
    └── result.html

## Prediction Logic
If gf_rolling > ga_rolling and venue_codes == 1 → Win  
If gf_rolling < ga_rolling → Loss  
Else → Draw

