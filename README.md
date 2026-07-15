# 🤝 Personalized Networking Assistant

An AI-powered Personalized Networking Assistant that helps users prepare for professional networking events by analyzing event details, identifying key discussion topics, generating networking conversation starters, verifying facts, and managing conversation history.

Built using **FastAPI**, **Streamlit**, **Natural Language Processing (NLP)**, and **Wikipedia API**.

---

# 📌 Features

- 🔍 Analyze professional profiles and networking events
- 🧠 Detect important themes from event descriptions
- 💬 Generate personalized networking conversation starters
- 📚 Verify facts using Wikipedia API
- 📝 Save networking conversation history
- 👍👎 Collect user feedback on generated suggestions
- 🎯 Generate AI-powered networking recommendations
- 📄 Interactive API documentation using Swagger UI
- 🧪 Unit testing using PyTest

---

# 🏗️ Project Architecture

```
                User
                  │
                  ▼
        Streamlit Frontend
                  │
                  ▼
          FastAPI Backend
                  │
        ┌─────────┼─────────┐
        │         │         │
        ▼         ▼         ▼
 Profile     Event Analyzer  Fact Checker
 Analyzer        │              │
        │         ▼              ▼
        │   Topic Generator  Wikipedia API
        │
        ▼
 History Logger
        │
        ▼
 Feedback Logger
        │
        ▼
     JSON Storage
```

---

# 📂 Project Structure

```
personalized-networking-assistant/
│
├── Documentation/
│   ├── 1. Brainstorming & Ideation
│   ├── 2. Requirement Analysis
│   ├── 3. Project Design Phase
│   ├── 4. Project Planning Phase
│   ├── 5. Project Development Phase
│   ├── 6. Project Testing
│   ├── 7. Project Documentation
│   └── 8. Project Demonstration
│
├── services/
│   └── fact_checker.py
│
├── app.py
├── main.py
├── event_analyzer.py
├── topic_generator.py
├── history.json
├── feedback.json
├── test_main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Technologies Used

| Technology | Purpose |
|------------|----------|
| FastAPI | Backend REST API |
| Streamlit | Frontend User Interface |
| Python | Programming Language |
| Wikipedia API | Fact Verification |
| JSON | Data Storage |
| PyTest | Unit Testing |
| Git & GitHub | Version Control |

---

# 🚀 Installation

## 1. Clone Repository

```bash
git clone https://github.com/akshayapeteti/personalized-networking-assistant.git

cd personalized-networking-assistant
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Backend

```bash
uvicorn main:app --reload
```

Backend runs at

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Frontend

```bash
streamlit run app.py
```

Frontend runs at

```
http://localhost:8501
```

---

# 🧪 Running Tests

```bash
pytest
```

Example Output

```
==================== 5 passed ====================
```

---

# 📷 Application Screenshots

## 🏠 Home Page

![Home Page](images/home.png)

---

## 📖 Swagger API Documentation

![Swagger](images/swagger.png)

---

## 🧠 AI Networking Suggestions

![Suggestions](images/suggestions.png)

---

## 💻 Source Code

![Source Code](images/code.png)

---

# 🎥 Project Demo Video

📹 **Watch the complete demonstration here:**

👉 **https://drive.google.com/file/d/10qq5iyRvMOK9mtanUdHdik4a2-m0lv1V/view?usp=drive_link**

---

# 🌟 Future Enhancements

- 🤖 Gemini API Integration
- 🔐 User Authentication
- ☁️ Cloud Deployment (Google Cloud)
- 🗄️ MongoDB/PostgreSQL Database
- 📊 Networking Analytics Dashboard
- 📧 Email Follow-up Generator
- 🌐 LinkedIn Integration
- 🎤 Voice-based Networking Assistant

---

# 👩‍💻 Project Team

**Project:** Personalized Networking Assistant

**Course:** Google Cloud Generative AI Internship

**Institution:** SRM University-AP

---

## ⭐ Team Lead

### Akshaya Peteti

**Roll No:** AP24110011368

**Responsibilities:**
- Project Design
- Backend Development
- FastAPI Development
- Streamlit UI Development
- NLP Integration
- GitHub Repository Management
- Documentation
- Project Demonstration

**GitHub:** https://github.com/akshayapeteti

---

## 👥 Team Members

### Maheswar Amara

**Roll No:** AP24110010683

**GitHub:** https://github.com/AP24110010683

---

### I. Jayani

**Roll No:** AP24110012035

**GitHub:** https://github.com/jayani999

---

### Meghana

**Roll No:** AP24110011235

**GitHub:** https://github.com/meghanakondaveeti-hub

---

# 📜 License

This project was developed as part of the **Google Cloud Generative AI Internship** for educational purposes.