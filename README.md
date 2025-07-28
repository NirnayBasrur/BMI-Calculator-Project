# BMI Calculator Project

A smart BMI calculator with:

- Unit switching (kg/cm and lbs/in)
- BMI visualization over time
- CSV export of tracked data
- Local health chatbot
- Support for single-user tracking

---

## Features

- Track your BMI with a clean and interactive UI  
- Switch between metric and imperial units  
- AI chatbot (local or OpenAI-powered) for personalized health tips  
- Export your BMI history as CSV  
- Visual insights into BMI trends over time  
- Private user data with support for offline mode  

---

## Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **AI/Chatbot:** Local response engine (OpenAI API ready)  
- **Data Storage:** Local CSV files  
- **Visualization:** Matplotlib  

---

## Setup Instructions

Get the Smart BMI Tracker up and running on your local machine in just a few steps.

### 1. Clone the Repository
```bash
git clone https://github.com/NirnayBasrur/BMI-Calculator-Project.git
cd BMI-Calculator-Project
```

### 2. (Optional but Recommended) Create a Virtual Environment
**For Windows:**
```bash
python -m venv venv
.env\Scriptsctivate
```

**For macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App Locally
```bash
streamlit run app.py
```

---

> Tip: Open VS Code, navigate to the project root, activate your virtual environment, and run the commands above inside the integrated terminal.
